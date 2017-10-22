from django.test import TestCase

from pwnit.api.blockchain import Blockchain


class BlockchainIntegrationTestCase(TestCase):
    def setUp(self):
        self.bc = Blockchain()

    def test_status(self):
        response = self.bc.status()
        definition = response.get('definition')
        self.assertTrue("TM04" in response.get('applications'))
        self.assertEqual(definition.get('encoding'), 'base64')

    def test_query_node(self):
        response = self.bc.query_node()
        self.assertTrue(len(response.get('address')) > 0)

    def test_app_read(self):
        response = self.bc.app_read()
        definition = response.get('definition')
        self.assertEqual(definition.get('encoding'), 'base64')
        self.assertTrue(len(definition.get('messages')) > 0)

    def test_app_update(self):
        response = self.bc.app_update('item.proto', 0.1, 'TM04')
        definition = response.get('definition')
        self.assertEqual(definition.get('encoding'), 'base64')

    def test_get_block_list(self):
        response = self.bc.get_block_list()

        # dir(response)
        # self.assertEqual()

    def test_get_genesis_block(self):
        r = self.bc.get_genesis_block()
        genesis = r.get('genesis')
        self.assertTrue(len(genesis.ref) > 0)

    def test_get_block(self):
        r = self.bc.get_block()
        current = r.get('current')
        self.assertTrue(len(current.ref) > 0)

