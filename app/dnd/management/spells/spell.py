class Spell:
    
    def __init__(self, spell_name):
        self.name = spell_name
    
    @property
    def level(self):
        return self._level

    @property
    def concentration(self):
        return self._concentration
    
    @property
    def ritual(self):
        return self._ritual
    
    @property
    def casting_time(self):
        return self._casting_time

    @property
    def range(self):
        return self._range

    @property
    def area(self):
        return self._area

    @property
    def area_shape(self):
        return self._area_shape

    @property
    def components(self):
        return self._components

    @property
    def duration(self):
        return self._duration

    @property
    def school(self):
        return self._school

    @property
    def attack_save(self):
        return self._attack_save

    @property
    def damage_effect(self):
        return self._damage_effect

    @property
    def description(self):
        return self._description

    @property
    def tags(self):
        return self._tags

    @property
    def classes(self):
        return self._classes

        
    @level.setter
    def level(self, value):
        self._level = value 
    
    @concentration.setter
    def concentration(self, value):
        self._concentration = value

    @ritual.setter
    def ritual(self, value):
        self._ritual = value

    @casting_time.setter
    def casting_time(self, value):
        self._casting_time = value

    @range.setter
    def range(self, value):
        self._range = value

    @area.setter
    def area(self, value):
        self._area = value

    @area_shape.setter
    def area_shape(self, value):
        self._area_shape = value

    @components.setter
    def components(self, value):
        self._components = value

    @duration.setter
    def duration(self, value):
        self._duration = value

    @school.setter
    def school(self, value):
        self._school = value

    @attack_save.setter
    def attack_save(self, value):
        self._attack_save = value

    @damage_effect.setter
    def damage_effect(self, value):
        self._damage_effect = value

    @description.setter
    def description(self, value):
        self._description = value

    @tags.setter
    def tags(self, value):
        self._tags = value

    @classes.setter
    def classes(self, value):
        self._classes = value
