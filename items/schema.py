from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from items.models import Item


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        filter_fields = ['name', 'owner', 'asset']
        interfaces = (relay.Node, )


class Query(AbstractType):
    item = relay.Node.Field(ItemNode)
    all_items = DjangoFilterConnectionField(ItemNode)

    # def resolve_all_items(self, info, **kwargs):
    #     owner = kwargs.get('owner')
    #     if owner is not None:
    #         return Item.objects.filter(owner=owner)
    #     return Item.objects.all()

