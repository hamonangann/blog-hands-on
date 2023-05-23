class Warung:
    def __init__(self, sedia: [str]) -> None:
        self.sedia = sedia
    
    def get_sedia(self) -> [str]:
        return self.sedia

# WarungKopi adalah subclass atau anak dari Warung
class WarungKopi(Warung):
    def __init__(self, sedia: [str], jumlah_kursi: int) -> None:
        super().__init__(sedia)
        self.jumlah_kursi = jumlah_kursi
    
    def get_jumlah_kursi(self) -> int:
        return self.jumlah_kursi

def main():
    warung = Warung(["Obat", "Sabun", "Sampo", "Snack"])
    warung_kopi = WarungKopi(["Kopi Tubruk", "Kopi Joss"], 20)

    print(warung.get_sedia())
    print(warung_kopi.get_sedia())
    print(warung_kopi.get_jumlah_kursi())

if __name__ == "__main__":
    main()