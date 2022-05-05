from rest_framework.serializers import ModelSerializer
from dnd.models import Dnd_Class, Effect, Element, Condition


class ElementSerializer(ModelSerializer):

    class Meta:
        model = Element
        fields = [
            'id',
            'name'
        ]


class EffectSerializer(ModelSerializer):

    class Meta:
        model = Effect
        fields = [
            'id',
            'name',
            'elemental',
            'conditional'
        ]


class ConditionSerializer(ModelSerializer):

    class Meta:
        model = Condition
        fields = [
            'id',
            'name',
        ]


class Dnd_ClassSerializer(ModelSerializer):

    class Meta:
        model = Dnd_Class
        fields = [
            'id',
            'name',
        ]
