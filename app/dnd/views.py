from rest_framework import viewsets
from dnd.models import Effect, Element, Condition, Dnd_Class
from dnd.serializers import Dnd_ClassSerializer, ElementSerializer, EffectSerializer, ConditionSerializer

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
