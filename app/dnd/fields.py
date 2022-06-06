from rest_framework.serializers import Field, ValidationError

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
