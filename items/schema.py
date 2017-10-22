from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from items.models import Item


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        filter_fields = ['name']
        interfaces = (relay.Node, )


class Query(AbstractType):
    item = relay.Node.Field(ItemNode)
    all_items = DjangoFilterConnectionField(ItemNode)

