from jsonschema import ValidationError
from rest_framework.serializers import Field

RANGE_DICT = {
    -1: "Unlimited",
    -2: "Sight",
    -3: "Self",
    0: "Touch"
}

DURATION_DICT = {
    0: "Instant",
    -1: "Until Dispelled",
    -2: "Until Dispelled or Triggered",
    -3: "Special"
}

#TODO convert to numbers only. -1 = self, 0 = touch, then in feet. each mile is 5000 feet. codes for sight = -2, unlimited = -3
class RangeField(Field):

    def to_representation(self, value):
        if value <=0 and value >= -3:
            return RANGE_DICT[value]
        elif  value < -3:
            raise ValidationError("Range Out of Bounds")
        else:
            return range_convert(value)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

#TODO convert to nums, -1 for infinity, else in feet, each 5000 feet = mile
class AreaField(Field):
    def to_representation(self, value):
        if value == -1:
            return "Infinity"
        elif value < -1:
            raise ValidationError("Area Out of Bounds")
        else:
            return range_convert(value)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

#TODO convert to nums, 0 = instant, -1 for UD, -2 for UDoT, -3 for special.
#TODO else in rounds. 10 rounds = minute. 600 rounds = hour. days?14400?
class DurationField(Field):
    def to_representation(self, value):
        if value < -3:
            raise ValidationError("Duration Out of Bounds")
        elif value >= -3 and value <= 0:
            return DURATION_DICT[value]
        if value == 1:
            return "1 Round"
        elif value == 10:
            return "1 Minute"
        elif value == 600:
            return "1 Hour"
        elif value == 15000:
            return "1 Day"
        elif value > 1 and value < 10:
            return "% d Rounds"%(value)
        elif value > 10 and value < 600:
            return "%d Minutes"%(value//10)
        elif value > 600 and value < 15000:
            return "%d Hours"%(value//600)
        else:
            return "%d Days"%(value//15000)

    def to_internal_value(self, data):
        return super().to_internal_value(data)


def range_convert(value):
    if value < 1:
        return "0"
    if value == 1:
        return "1 Foot"
    elif value >= 5000 and value < 10000:
        return "1 Mile"
    elif value < 5000:
        return "%d Feet"%(value)
    else:
        return "%d Miles"%(value//5000)
