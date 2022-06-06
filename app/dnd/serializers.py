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
    range = RangeField(source="spell.range")
    area = AreaField(source="spell.area")
    duration = DurationField(source="spell.duration")

    elements = ElementSerializer(many=True, queryset=Element.objects.all())
    effects = EffectSerializer(many=True)
    conditions = ConditionSerializer(many=True)
    classes = Dnd_ClassSerializer(many=True)
    components = Spell_ComponentSerializer(many=True)

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
            'duration',
            'school',
            'attack_save',
            'effects',
            'elements',
            'conditions',
            'description',
            'classes'            
        ]