from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator



class Element(models.Model):
    name = models.CharField(max_length=32)


class Effect(models.Model):
    name = models.CharField(max_length=16)


class Condition(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='')


class Dnd_Class(models.Model):
    name = models.CharField(max_length=32)


class Spell_Component(models.Model):
    name = models.CharField(max_length=16)


class Spell(models.Model):

    name = models.CharField(max_length=256)
    level = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(9),
            MinValueValidator(0)
        ]
    )

    is_concentration = models.BooleanField(default=False)
    is_ritual = models.BooleanField(default=False)

    class CastTimeType(models.TextChoices):
        ACTION = 'action', _('Action')
        BONUS_ACTION = 'bonus', _('Bonus Action')
        REACTION = 'reaction', _('Reaction')
        MINUTE = 'minute', _('1 Minute')
        TEN_MINUTES = '10 minutes', _('10 Minutes')
        HOUR = 'hour', _('1 Hour')
        EIGHT_HOURS = '8 hours', _('8 Hours')
        TWELVE_HOURS = '12 hours', _('12 Hours')
        TWENTY_FOUR_HOURS = '24 hours', _('24 Hours')
        OTHER = 'other', _('other')

    casting_time = models.CharField(
        max_length=16,
        choices=CastTimeType.choices,
        default=CastTimeType.ACTION,
    )

    range_num = models.PositiveIntegerField(default=0)

    class RangeType(models.TextChoices):
        SELF = 'self', _('Self')
        TOUCH = 'touch', _('Touch')
        FEET = 'feet', _('Feet')
        MILES = 'miles', _('Miles')
        SIGHT = 'sight', _('Sight')
        UNLIMITED = 'unlimited', _('Unlimited')

    range_str = models.CharField(
        max_length=16,
        choices=RangeType.choices,
        default=RangeType.SELF
    )
    
    area_num = models.PositiveIntegerField(default=0)

    class AreaType(models.TextChoices):
        FEET = 'feet', _('Feet')
        MILES = 'miles', _('Miles')
        INFINITY = 'infinity', _('Infinity')
    
    area_str = models.CharField(
        max_length=16,
        choices=AreaType.choices,
        default=AreaType.FEET
    )

    #alt + 0178 = ²
    class ShapeType(models.TextChoices):
        CONE = 'cone', _('Cone')
        SPHERE = 'sphere', _('Sphere')
        SQUARE = 'square', _('Square')
        LINE = 'line', _('Line')
        FEET2 = 'feet2', _('Feet²')
        FLAT_SQUARE = 'flat_square', _('Flat Square')
        CYLINDER = 'cylinder', _('Cylinder')

    area_shape = models.CharField(
        max_length=16,
        choices = ShapeType.choices,
        blank=True,
        null=True
    )

    components = models.ManyToManyField(Spell_Component)

    duration_num = models.PositiveIntegerField(default=0)
    
    class TimeType(models.TextChoices):
        INSTANTANEOUS = 'instantaneous', _('Instantaneous')
        ROUNDS = 'rounds', _('Rounds')
        MINUTES = 'minutes', _('Minutes')
        HOURS = 'hours', _('Hours')
        DAYS = 'days', _('Days')
        SPECIAL = 'special', _('Special')
        UNTIL_DISPELLED = 'until_dispelled', _('Until Dispelled')
        UNTIL_DISPELLED_OR_TRIGGERED = 'until_dispelled_or_triggered', _('Until Dispelled or Triggered')
    
    duration_str = models.CharField(
        max_length=16,
        choices = TimeType.choices,
        default= TimeType.ROUND
    )

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

    class AttackSaveType(models.TextChoices):
        STR = 'str', _('STR')
        DEX = 'dex', _('DEX')
        CON = 'con', _('CON')
        INT = 'int', _('INT')
        WIS = 'wis', _('WIS')
        CHA = 'cha', _('CHA')
        MELEE = 'melee', _('Melee')
        RANGED = 'ranged', _('Ranged')

    attack_save = models.CharField(
        max_length=8,
        choices = AttackSaveType.choices,
        blank=True,
        null=True
    )

    effects = models.ManyToManyField(Effect)
    elements = models.ManyToManyField(Element, blank=True)
    conditions = models.ManyToManyField(Condition, blank=True)

    description = models.TextField(default='')
        
    classes = models.ManyToManyField(Dnd_Class)
