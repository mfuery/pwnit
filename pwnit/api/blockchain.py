
from mastercardapicore import RequestMap, Config, OAuthAuthentication
from mastercardblockchain import Status

from pwnit.local_settings import CREDS


class Blockchain:
    """Bidirectional communication with Mastercard Blockchain API"""

    def __init__(self, consumer_key=None, key_store_path=None, key_alias=None, keystore_password=None):
        self.consumer_key = consumer_key if consumer_key else CREDS['consumer_key']
        self.key_store_path = key_store_path if key_store_path else CREDS['key_store_path']
        self.key_alias = key_alias if key_alias else CREDS['key_alias']
        self.keystore_password = keystore_password if keystore_password else CREDS['keystore_password']
        self.oauth = OAuthAuthentication(self.consumer_key, self.key_store_path, self.key_alias, self.keystore_password)

        Config.setAuthentication(self.oauth)
        Config.setDebug(True)  # Enable http wire logging
        Config.setSandbox(True)

    def test_credentials(self):
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

