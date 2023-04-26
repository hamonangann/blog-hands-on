def faktorial(user_input: str) -> str:
    if not user_input.isnumeric():
        return "Harap masukkan input numerik (0-9)"

    # Cast user_input string to integer
    user_input = int(user_input)

    result = 1
    for i in range(1, user_input+1):
        result *= i
    
    return "Nilai faktorialnya adalah " + str(result)