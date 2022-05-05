from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator



class Element(models.Model):
    name = models.CharField(max_length=32)


class Effect(models.Model):
    name = models.CharField(max_length=64)
    elemental = models.BooleanField(default=False)
    conditional = models.BooleanField(default=False)


class Condition(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='')


class Dnd_Class(models.Model):
    name = models.CharField(max_length=32)


class Spell(models.Model):

    name = models.CharField(max_length=256)
    level = models.IntegerField(
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)
        ]
    )

    #TODO needs to parse other into actual time?
    class ActionType(models.TextChoices):
        ACTION = 'action', _('Action')
        BONUS_ACTION = 'bonus', _('Bonus Action')
        REACTION = 'reaction', _('Reaction')
        OTHER = 'other', _('other')

    casting_time = models.CharField(
        max_length=8,
        choices=ActionType.choices,
        default=ActionType.ACTION,
    )

    #TODO range(int, -1 self, 0 touch, otherwise range, need to account for fake infinite aka full plane) and real inf (everything)
    #TODO area (int only)
    #TODO area shape
    range = models.IntegerField()

    #TODO V,S,M * 
    components = models.CharField(max_length=16)

    #TODO instantaneous vs 1 round, 1 minute, 10 minutes, 1 hour etc.
    duration = models.IntegerField()

    class SchoolType(models.TextChoices):
        ABJURATION = 'abjuration', _('Abjuration')
        CONJURATION = 'conjuration', _('Conjuration')
        DIVINATION = 'divination', _('Divination')
        ENCHANTMENT = 'enchantment', _('Enchantment')
        EVOCATION = 'evocation', _('Evocation')
        ILLUSION = 'illusion', _('Illusion')
        NECROMANCY = 'necromancy', _('Necromancy')
        TRANSMUTATION = 'transmutation', _('Transmutation')

    school = models.CharField(
        max_length=16,
        choices = SchoolType.choices
    )

    class SaveType(models.TextChoices):
        STR = 'str', _('STR')
        DEX = 'dex', _('DEX')
        CON = 'con', _('CON')
        INT = 'int', _('INT')
        WIS = 'wis', _('WIS')
        CHA = 'cha', _('CHA')
        NONE = 'none', _('None')

    attack_save = models.CharField(
        max_length=4,
        choices = SaveType.choices
    )

    effect = models.ForeignKey(Effect, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Element)
    conditions = models.ForeignKey(Condition, on_delete=models.CASCADE)

    description = models.TextField(default='')
        
    classes = models.ManyToManyField(Dnd_Class)
