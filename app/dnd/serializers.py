from rest_framework import serializers
from dnd.models import Dnd_Class, Effect, Element, Condition, Spell, Spell_Component
from dnd.fields import RangeField, AreaField, DurationField


class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = [
            'id',
            'name'
        ]


class EffectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Effect
        fields = [
            'id',
            'name'
        ]

#TODO check if __all__ can be used in place of id, name, description


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'


class Dnd_ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dnd_Class
        fields = [
            'id',
            'name',
        ]


class Spell_ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell_Component
        fields = [
            'id',
            'name',
        ]

class SpellSerializer(serializers.ModelSerializer):
    spell_range_tuple = serializers.SerializerMethodField()
    spell_range = RangeField(spell_range_tuple)


    elements = ElementSerializer(many=True, read_only=True)
    effects = EffectSerializer(many=True, read_only=True)
    conditions = ConditionSerializer(many=True, read_only=True)
    classes = Dnd_ClassSerializer(many=True, read_only=True)
    components = Spell_ComponentSerializer(many=True, read_only=True)

    class Meta:
        model = Spell
        fields = [
            'id',
            'name',
            'level',
            'is_concentration',
            'is_ritual',
            'casting_time',
            'spell_range',
            'spell_area',
            'area_shape',
            'components',
            'spell_duration',
            'school',
            'attack_save',
            'effects',
            'elements',
            'conditions',
            'description',
            'classes'            
        ]

    def get_spell_range_tuple(self, obj):
        return (obj.range_num, obj.range_str)