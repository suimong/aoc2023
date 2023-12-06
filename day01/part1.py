from pathlib import Path

number_set_literal: set[str] = set(str(x) for x in range(10))

def get_first_digit(cipher: str) -> int:
    for char in cipher:
        if char in number_set_literal:
            return int(char)
    raise ValueError(f"There's no number in this str: {cipher}")

def decipher(cipher: str) -> int:
    first_digit = get_first_digit(cipher)
    last_digit = get_first_digit(reversed(cipher))

    return first_digit * 10 + last_digit

if __name__ == "__main__":
    inputs_file = Path(__file__).parent / "inputs.txt"
    ciphers = inputs_file.read_text().splitlines()
    result = sum([decipher(cipher) for cipher in ciphers])
    print(result)