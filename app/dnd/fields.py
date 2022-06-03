from rest_framework.serializers import Field

class RangeField(Field):
    def to_representation(self, value):
        return super().to_representation(value)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

class AreaField(Field):
    def to_representation(self, value):
        return super().to_representation(value)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

class DurationField(Field):
    def to_representation(self, value):
        return super().to_representation(value)

    def to_internal_value(self, data):
        return super().to_internal_value(data)


def singularize(word):
    pass