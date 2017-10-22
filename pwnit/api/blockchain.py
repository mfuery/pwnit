
from mastercardapicore import RequestMap, Config, OAuthAuthentication
from mastercardblockchain import Status


class Blockchain:
    def __init__(self, consumer_key, key_store_path='.', key_alias='keyalias', key_password='keystorepassword'):
        self.consumer_key = consumer_key
        self.key_store_path = key_store_path
        self.key_alias = key_alias
        self.key_password = key_password

    def test_credentials(self):
        auth = OAuthAuthentication(self.consumer_key, self.key_store_path, 'keyalias', 'keystorepassword')
        Config.setAuthentication(auth)
        Config.setDebug(True)  # Enable http wire logging
        Config.setSandbox(True)

        map_obj = RequestMap()
        response = Status.query(map_obj)
        return response

        print("applications[0]--> %s") % response.get("applications[0]")  # applications[0]-->MA99
        print("current.ref--> %s") % response.get(
            "current.ref")  # current.ref-->3ee7d7608368f4133da7c45d7d5f0518d89d540891849b35cfe5ec08e298755d
        print("current.slot--> %s") % response.get("current.slot")  # current.slot-->1503661406
        print("genesis.ref--> %s") % response.get(
            "genesis.ref")  # genesis.ref-->92510aeb361b62e982cfabafc56d5b666f29107fb0c5309030b883f702916e80
        print("genesis.slot--> %s") % response.get("genesis.slot")  # genesis.slot-->1503599076
        print("network--> %s") % response.get("network")  # network-->1513115205
        print("version--> %s") % response.get("version")  # version-->0.5.0

        print("HttpStatus: %s") % e.getHttpStatus()
        print("Message: %s") % e.getMessage()
        print("ReasonCode: %s") % e.getReasonCode()
        print("Source: %s") % e.getSource()

