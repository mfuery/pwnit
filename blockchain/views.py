from django.views.generic import TemplateView
from mastercardapicore.core.exceptions import APIException

from pwnit.api.blockchain import Blockchain


class Api(TemplateView):
    template_name = 'blockchain/api.html'

    def get_context_data(self, **kwargs):
        context = super(Api, self).get_context_data(**kwargs)

        bc = Blockchain()
        try:
            response = bc.status()
            context['response'] = {
                'applications': response.get('applications'),
                'current.ref': response.get('current.ref'),
                'current.slot': response.get('current.slot'),
                'genesis.ref': response.get('genesis.ref'),
                'genesis.slot': response.get('genesis.slot'),
                'network': response.get('network'),
                'version': response.get('version'),
            }
        except APIException as e:
            context['error'] = {
                'HttpStatus': e.getHttpStatus(),
                'Message': e.getMessage(),
                'ReasonCode': e.getReasonCode(),
                'Source': e.getSource()
            }

        return context
