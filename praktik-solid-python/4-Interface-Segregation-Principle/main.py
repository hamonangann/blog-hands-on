import abc

class HewanBerkaki(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def jalan(self) -> str:
        pass

class HewanBersayap(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def terbang(self) -> str:
        pass

class Burung(HewanBerkaki, HewanBersayap):
    @classmethod
    def jalan(self) -> str:
        return "Cip cip berjalan"

    @classmethod
    def terbang(self) -> str:
        return "Cip cip terbang"

class Kucing(HewanBerkaki):
    @classmethod
    def jalan(self) -> str:
        return "Meow meow berjalan"

def main():
    burung = Burung()
    kucing = Kucing()
    print(burung.terbang())
    print(kucing.jalan())

if __name__ == "__main__":
    main()