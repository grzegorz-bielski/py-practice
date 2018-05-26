from .Animal import Animal


class Enemy(Animal):
    __hp = 200

    def __init__(self, atkl, atkh, age):
        super(Enemy, self).__init__(age)
        self.atkl = atkl
        self.atkh = atkh

    def get_atkh(self):
        return self.atkh

    def get_atkl(self):
        return self.atkl

    def takeHit(self, hit):
        self.__hp -= hit
        return self.__hp
