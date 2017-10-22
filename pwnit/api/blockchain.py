from base64 import b64encode

import os
from mastercardapicore import RequestMap, Config, OAuthAuthentication
from mastercardblockchain import Status, Block, App, Node, TransactionEntry

from blockchain.proto.item_pb2 import Item
from pwnit.local_settings import CREDS, BASE_DIR


class Blockchain:
    """Bidirectional communication with Mastercard Blockchain API"""

    def __init__(self, consumer_key=None, key_store_path=None, key_alias=None, keystore_password=None, app_id=None):
        self.consumer_key = consumer_key if consumer_key else CREDS['consumer_key']
        self.key_store_path = key_store_path if key_store_path else CREDS['key_store_path']
        self.key_alias = key_alias if key_alias else CREDS['key_alias']
        self.keystore_password = keystore_password if keystore_password else CREDS['keystore_password']
        self.oauth = OAuthAuthentication(self.consumer_key, self.key_store_path, self.key_alias, self.keystore_password)

        Config.setAuthentication(self.oauth)
        Config.setDebug(True)  # Enable http wire logging
        Config.setSandbox(True)

        self.app_id = CREDS['app_identifier']

    def status(self):
        """Gets general metadata about the current state of the blockchain network. Useful for building dashboards.

        :return: Response Reference
            Parameter	Example
            network
            For the main chain, this id should always be the integer 1513115205.
            1513115205
            version
            Note that this is returned as a semantically versioned string. Versions of messages should be able to be transmitted on the binary protocol as 32-bit integers. e.g. The version "1.0.0" represents the actual big-endian byte array [1,0,0,0] which is equivalent to a uint32 value of
            0.5.0
            witnesses[]
            The blockchain addresses of the audit nodes currently engaged in processing block confirmations
            applications[]
            The application identifiers available at this node
            ['MA99']
            genesis
            Basic information about first block in the chain on this network
            See child attributes
            genesis​.slot
            The slot number of the first block in the chain on this network
            1502882325
            genesis​.ref
            Hash of the first block in the chain on this network
            671d13640e28b3befe225a48a9b919a3ba424db0b8807ee57661b61a7555f763
            current
            Basic information about the current block which is last confirmed block in the chain on this network
            See child attributes
            current​.slot
            The slot number of the last confirmed block
            1502893442
            current​.ref
            Hash of the last confirmed block
            747443ae8d73dbb381770cea820ec6a0e9548b299c8d2aadb12f113e949158e7
            alerts[]
            Informational alerts such as upcoming version or network configuration changes
        """
        map_obj = RequestMap()
        response = Status.query(map_obj)
        return response

        # From API documentation...
        # print("applications[0]--> %s") % response.get("applications[0]")  # applications[0]-->MA99
        # print("current.ref--> %s") % response.get(
        #     "current.ref")  # current.ref-->3ee7d7608368f4133da7c45d7d5f0518d89d540891849b35cfe5ec08e298755d
        # print("current.slot--> %s") % response.get("current.slot")  # current.slot-->1503661406
        # print("genesis.ref--> %s") % response.get(
        #     "genesis.ref")  # genesis.ref-->92510aeb361b62e982cfabafc56d5b666f29107fb0c5309030b883f702916e80
        # print("genesis.slot--> %s") % response.get("genesis.slot")  # genesis.slot-->1503599076
        # print("network--> %s") % response.get("network")  # network-->1513115205
        # print("version--> %s") % response.get("version")  # version-->0.5.0
        #
        # print("HttpStatus: %s") % e.getHttpStatus()
        # print("Message: %s") % e.getMessage()
        # print("ReasonCode: %s") % e.getReasonCode()
        # print("Source: %s") % e.getSource()

    def provision_node(self):
        """Provisions a Blockchain node for your application.

        """
        mapObj = RequestMap()
        mapObj.set("network", "Z0NE")
        mapObj.set("application.name", "MA99")
        mapObj.set("application.description", "")
        mapObj.set("application.version", 0)
        mapObj.set("application.definition.format", "proto3")
        mapObj.set("application.definition.encoding", "base64")
        mapObj.set("application.definition.messages",
                   "Ly8gU2ltcGxlIG5vdGFyeSBhcHBsaWNhdGlvbg0KDQpzeW50YXggPSAicHJvdG8zIjsNCg0KcGFja2FnZSBFMTAyOw0KDQptZXNzYWdlIE1lc3NhZ2Ugew0KCWJ5dGVzIGFydGlmYWN0UmVmZXJlbmNlID0gMTsNCn0=")
        mapObj.set("invitations[0]", "john.doe@abc.com")
        mapObj.set("invitations[1]", "jane.doe@xyz.com")

        response = Node.provision(mapObj)
        print("address--> %s") % response.get("address")  # address-->CNkNVuVnQ4WigadrQKcNuTa1JkAJFWF9S8
        print("authority--> %s") % response.get("authority")  # authority-->ShgddyMCV6oBL7putekmJkYzXbGuoyggA8
        print("type--> %s") % response.get("type")  # type-->customer
        return response

    def query_node(self):
        """This call gets information about your local blockchain node, the applications that it understands,
        and its connections to other peers in the network. """
        mapObj = RequestMap()
        response = Node.query(mapObj)
        return response

    def app_read(self, app_id=None):
        self.app_id = app_id if not self.app_id else CREDS['app_identifier']
        response = App.read(self.app_id)
        return response

    def app_update(self, message_definition_filename='item.proto', message_version=1.0, app_identifier=None):
        """When you are permissioned onto the network, you will be issued one or more `id`s to use. You may then send
        or update configurations of the transaction message types you wish to use. These are specified using Protocol
        Buffer version 3 files as specified [here](https://developers.google.com/protocol-buffers/docs/proto3) This
        specification may be sent either as the canonical JSON transform or the native `.proto` file encoded as hex,
        base58 or base64.

        Parameter	Required	Example
        id
        This is the application id. You can get a list of applications your Blockchain node is part of by using the Status/query API
        Required	MA99
        name
        This is your application identifier and will be used to partition your Blockchain instance. This value MUST match the package name in your protocol buffer definition.
        Required	MA99
        description
        Description of your Blockchain application
        Optional	My Blockchain Application
        version
        Version of your Blockchain application
        Optional	1
        definition
        Required	See child attributes
        definition​.format
        Format of your message defintion. Must be "proto3"
        Required	proto3
        definition​.encoding
        Encoding scheme used to encode your protocol buffer message definition
        Required	base64
        definition​.messages
        Your protocol buffer message definition
        Required	Ly8gU2ltcGxlIG5vdGFyeSBhcHBsaWNhdGlvbg0KDQpzeW50YXggPSAicHJvdG8zIjsNCg0KcGFja2FnZSBFMTAwOw0KDQptZXNzYWdlIE1lc3NhZ2Ugew0KCWJ5dGVzIGFydGlmYWN0UmVmZXJlbmNlID0gMTsNCn0=
        """
        f = open(os.path.join(BASE_DIR, 'blockchain', 'proto', message_definition_filename), 'rb')
        msg_def = b64encode(f.read()).decode()

        mapObj = RequestMap()
        mapObj.set("id", app_identifier)
        mapObj.set("name", app_identifier)
        mapObj.set("description", "")
        mapObj.set("version", message_version)
        mapObj.set("definition.format", "proto3")
        mapObj.set("definition.encoding", "base64")
        mapObj.set("definition.messages", msg_def)
        request = App(mapObj)
        response = request.update()
        return response

    def create_entry(self):
        pass

    def retrieve_entry(self):
        pass

    def update_node(self):
        pass

    def retrieve_block(self):
        pass

    def retrieve_last_confirmed_block(self):
        pass

    def read_block(self, id):
        """A specific block may be retrieved by its hash key. This is useful when navigating the chain.

        id  Id can be the slot or the hash of the block to retrieve
            Example: 1503574734
        """
        response = Block.read(id)
        return response

    def get_block_list(self, from_block=0, to_block=0):
        """By default, this call returns the last confirmed block, since the `from` and `to` parameters will both
        default to the last confirmed slot number. To get a range of blocks, use the `from` and `to` parameters.
        Specifying only the `from` parameter will get a range of blocks up to the current slot. Note that this also
        means that specifying `to` without `from` will result in an error since that will mean a negative range. For
        each returned item, the data will contain header information from the block binary, and references to the
        block entries via the merkle roots. Note that the maximum range request allowed is 600 entries.
        """
        responseList = Block.listByCriteria()
        response = responseList.get("list[0]")
        return response

    def get_genesis_block(self):
        """"
        current":{"ref":"dee26af2b5500baa3b929a6641478ac7d8059eaada847f0391216a2fe59ac10f","slot":1508665398},
        "genesis":{"ref":"d157345cb480f4e02ab0daaeed6b0ad6d78b9c5683d524e1edbff07f0cb1284e","slot":1508435744}
        """
        return self.get_block_list().get('genesis')

    def get_block(self, ref_id=None):
        """"
        :param id optional if none specified, returns the current block
            Id can be the slot or the hash of the block to retrieve
            Example: 1503574734
            Required
        :returns response
            Example:
            b'[{"authority":"RBYki6PSXiHys8stYNLJnw6q6DPforRJbtF7KiSrRJQ97EmFSJkR7tmzGxVDeHX2DbZpdg2DMR5325DUjyVqEmew",
            "hash":"91f9003c7d456c6482553c52ef87147556107151cfb173a741f2f8f49c12b9d9",
            "nonce":"5493722113237126872",
            "partitions":[],
            "previous_block":"f18c131303dfd3a461b1f623cd4637a56cd81c2388575d9c8c94b9e412f5f3f4",
            "signature":"381yXZ2S7fVoZXYqvfoaeTUEYM7CLx1YXm6t2fz5cWuzoH1wgdW43ZqDmSYPTj9qYnm1P6moCKBWTdYxv15rYuygKDxsB5Ug",
            "slot":1508667383,
            "version":1}]'
        """
        if not ref_id:
            current_block = self.get_block_list().get('current')
            ref_id = current_block.get('ref')
        response = Block.read(ref_id)
        return response

    # @todo
    def transact(self, item):
        """Saves this item transaction to the blockchain

        :param item: Item model
        :return:
        """
        item_block = self.get_block(item.uuid)
        item_msg = Item()
        item_msg.item_name = item.name

        mapObj = RequestMap()
        mapObj.set("app", self.app_id)
        mapObj.set("encoding", "base64")
        mapObj.set("value", b64encode(item_msg))

        response = TransactionEntry.create(mapObj)
        print("hash--> %s") % response.get(
            "hash")  # hash-->1e6fc898c0f0853ca504a29951665811315145415fa5bdfa90253efe1e2977b1
        print("slot--> %s") % response.get("slot")  # slot-->1503662624
        print("status--> %s") % response.get("status")  # status-->pending
        return response

    # @todo
    def get_transaction(self, hash):
        """Returns full detail of the value of the blockchain entry referenced by the specified khashey, if it has been
         previously recorded by your node's key-value store (database).

        :param hash
            The hash of the entry to retrieve
            Example: 1e6fc898c0f0853ca504a29951665811315145415fa5bdfa90253efe1e2977b1
            Required

        :return response
            Parameter	Example
            hash
            Hash of the value written onto the chain. Can be used to lookup the entry.
            50cbc906b2d5e4e795b9aa79ad35e7b9989839a0a0fc95b2ecd063529db365fd
            slot
            Slot the entry is written to
            1502899441
            status
            Status of the entry on the chain.
            confirmed
            value
            Hex representation of the value written onto the chain.
            0a0d5465737420446f63756d656e74
         """
        id = CREDS['app_identifier']
        map = RequestMap()
        map.set("hash", hash)
        response = TransactionEntry.read(id, map)
        print("hash--> %s") % response.get(
            "hash")  # hash-->1e6fc898c0f0853ca504a29951665811315145415fa5bdfa90253efe1e2977b1
        print("slot--> %s") % response.get("slot")  # slot-->1503594631
        print("status--> %s") % response.get("status")  # status-->confirmed
        print("value--> %s") % response.get("value")  # value-->0a0f4d41393920446f63756d656e742031
        return response

    # @todo
    def sync_blockchain_to_db(self):
        done = False

        while not done:
            # b = Block(uuid=, previous_block=, contents=)
            pass

    # @todo
    def sync_db_to_blockchain(self):
        # Check message version
        app = self.app_read()
