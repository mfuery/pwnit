from django.http import HttpResponse
from django.views.generic import TemplateView
from mastercardapicore import APIException

from pwnit.api.blockchain import Blockchain
from pwnit.local_settings import CREDS


class Api(TemplateView):
    template_name = 'blockchain/api.html'

    def get_context_data(self, **kwargs):
        context = super(Api, self).get_context_data(**kwargs)

        bc = Blockchain(CREDS['consumer_key'], CREDS['p12_path'], CREDS['key_alias'], CREDS['keystore_password'])
        try:
            context['response'] = bc.test_credentials
        except APIException as e:
            context['error'] = e

        return context
