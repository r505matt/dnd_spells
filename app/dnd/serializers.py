from rest_framework.serializers import ModelSerializer
from dnd.models import Dnd_Class, Effect, Element, Condition, Spell, Spell_Component


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
            'name'
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


class Spell_ComponentSerializer(ModelSerializer):

    class Meta:
        model = Spell_Component
        fields = [
            'id',
            'name',
        ]

class SpellSerializer(ModelSerializer):

    class Meta:
        model = Spell
        fields = [
            'id',
            'name',
            'level',
            'is_concentration',
            'is_ritual',
            'casting_time',
            'range',
            'area',
            'area_shape',
            'components',
            'duration_num',
            'duration_str',
            'school',
            'attack_save',
            'effects',
            'elements',
            'conditions',
            'description',
            'classes'            
        ]