class ColorValue:
    AVAILABLE_VARIANTS = ['white', 'black']

    def __set_name__(self, inctance, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, value, self.name)
        else:
            raise ValueError('value must be \'white\' or \'black\'')

    def __check_value(self, value):
        return value in self.AVAILABLE_VARIANTS
