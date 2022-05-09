from rest_framework import viewsets
from dnd.models import Effect, Element, Condition, Dnd_Class, Spell, Spell_Component
from dnd.serializers import Dnd_ClassSerializer, ElementSerializer, EffectSerializer, ConditionSerializer, Spell_ComponentSerializer, SpellSerializer

class ElementViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing element instances
    """
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
    lookup_field = 'id'
    pagination_class = None


class EffectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing element instances
    """
    serializer_class = EffectSerializer
    queryset = Effect.objects.all()
    lookup_field = 'id'
    pagination_class = None


class ConditionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing condition instances
    """
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
    lookup_field = 'id'
    pagination_class = None


class Dnd_ClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing condition instances
    """
    serializer_class = Dnd_ClassSerializer
    queryset = Dnd_Class.objects.all()
    lookup_field = 'id'
    pagination_class = None


class Spell_ComponentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing spell component instances
    """
    serializer_class = Spell_ComponentSerializer
    queryset = Spell_Component.objects.all()
    lookup_field = 'id'
    pagination_class = None


class SpellViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing spell instances
    """
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()
    lookup_field = 'id'
    pagination_class = None
