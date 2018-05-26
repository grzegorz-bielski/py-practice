class Animal():

    def __init__(self, age):
        self.__age = age
        self.__isAlive = True

    def get_hp(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_age(self, age):
        return self.__age
