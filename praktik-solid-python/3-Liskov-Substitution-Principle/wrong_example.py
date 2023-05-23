# Wahana class to be overriden
class Wahana:
    def get_harga(self) -> int:
        return 1000

    def get_maksimal_umur(self) -> int:
        return 99

class OdongOdong(Wahana):
    def __init__(self, harga, maksimal_umur):
        self.harga = harga
        self.maksimal_umur = maksimal_umur

    def get_harga(self) -> int:
        return self.harga
    
    def get_maksimal_umur(self) -> int:
        return self.maksimal_umur

class RollerCoaster(Wahana):
    def __init__(self, harga):
        self.harga = harga

    def get_harga(self) -> int:
        return self.harga
    
    def get_maksimal_umur(self) -> None:
        raise Exception("Tidak ada maksimal umur")

def main():
    odong_odong = OdongOdong(5000, 12)
    roller_coaster = RollerCoaster(20000)

    print(odong_odong.get_harga())
    print(odong_odong.get_maksimal_umur())
    print(roller_coaster.get_harga())
    print(roller_coaster.get_maksimal_umur())

if __name__ == "__main__":
    main()