import abc

# Class Pintu adalah interface yang akan digunakan oleh subclass
class Pintu:
    @classmethod
    @abc.abstractmethod
    def warna_pintu(self) -> str:
        pass

class PintuKayu(Pintu):
    @classmethod
    def warna_pintu(self) -> str:
        return "Coklat"

class PintuKaca(Pintu):
    @classmethod
    def warna_pintu(self) -> str:
        return "Bening"

class Rumah(Pintu):
    def __init__(self, pintu: Pintu):
        self.pintu = pintu

    @classmethod
    def warna_pintu(self) -> str:
        return self.pintu.warna_pintu()

def main():
    rumah_saya = Rumah(PintuKayu)
    print(rumah_saya.warna_pintu())

if __name__ == "__main__":
    main()