class Pet:

    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        years = self.__age // 12
        months = self.__age % 12

        if years == 0:
            return f"{months} month(s)"
        elif months == 0:
            return f"{years} year(s)"
        else:
            return f"{years} year(s) and {months} month(s)"