class Guns:
    def __init__(self, bullets):
        self.bullets = bullets

    def shot(self):
        pass

    def reload(self):
        pass


class Pistol(Guns):
    def shot(self):
        print('Пистолетный выстрел')


class Ak(Guns):
    def shot(self):
        print('Калашный выстрел')


def manyShots(gun):
    for i in range(gun.bullets):
        gun.shot()


pistol = Pistol(3)
manyShots(pistol)
ak = Ak(5)
manyShots(ak)
