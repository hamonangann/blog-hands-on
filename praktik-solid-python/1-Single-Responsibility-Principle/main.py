# Class-based SRP. Uncomment kode di bawah untuk menggunakannya
class Penghitung:
    @classmethod
    def hitung(self, x: int) -> int:
        result = 1
        for i in range(1, x+1):
            result *= ic
        return result

class Validator:
    @classmethod
    def validasi(self, user_input: str) -> bool:
        return user_input.isnumeric()

class IoHandler:
    @classmethod
    def io(self, user_input: str) -> str:
        if not Validator.validasi(user_input):
            return "Harap masukkan input numerik (0-9)"
        return "Nilai faktorialnya adalah " + str(Penghitung.hitung(int(user_input)))

def main():
    user_input = input("Masukkan bilangan yang ingin dihitung faktorialnya: ")
    print(IoHandler.io(user_input))


# Function-based SRP. Uncomment kode di bawah untuk menggunakannya

# def hitung(x: int) -> int:
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result

# def validasi(user_input: str) -> bool:
#     return user_input.isnumeric()

# def io(user_input: str) -> str:
#     if not validasi(user_input):
#         return "Harap masukkan input numerik (0-9)"
#     return "Nilai faktorialnya adalah " + str(hitung(int(user_input)))

# def main():
#     user_input = input("Masukkan bilangan yang ingin dihitung faktorialnya: ")
#     print(io(user_input))


# Main invoker

if __name__ == '__main__':
    main()
