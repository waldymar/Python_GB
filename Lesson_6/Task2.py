class Road:
    def param(self, _length, _width, ms, tls):
        self._length = length
        self._width = width
        calc = self._width * self._length * ms * tls
        print(f"При введенных параметрах, масса асфальта равняется {int(calc / 1000)} тонн")


length = int(input("Введите длину дороги: "))
width = int(input("Введите ширину дороги: "))
ms = int(input("Введите массу асфальта для покрытия одного м2 дороги асфальтом (в кг): "))
tls = int(input("Введите толщину полотна (в см): "))
pr = Road()
pr.param(length, width, ms, tls)
