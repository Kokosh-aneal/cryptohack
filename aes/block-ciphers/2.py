import codecs
import requests


def encrypt(plaintext):
    plain_hex = plaintext.encode().hex()
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + plain_hex
    r = requests.get(url)
    r_data = r.json()
    return r_data.get("ciphertext", None)


def pad_flag_guess(guess):
    padding = "A" * (16 - len(guess) % 16)
    padded_guess = padding + guess + padding
    return padded_guess


if __name__ == "__main__":
    letters = "abcdefghijklmnopqrstuvwxyz1234567890_{}"
    flag = "crypto{"

    while flag[-1:] != "}":  # we know the flag ends with a '}'.
        for l in letters:
            flag_guess = flag + l
            padded_guess = pad_flag_guess(flag_guess)
            # print(padded_guess)
            ciphertext = encrypt(padded_guess)
            # print(ciphertext)
            # input()

            guess_output_size = 2 * ((16 - len(flag_guess) % 16) + len(flag_guess))
            # print(guess_output_size)
            encrypted_guess = ciphertext[:guess_output_size]
            # print(encrypted_guess)
            encrypted_flag = ciphertext[guess_output_size:guess_output_size*2]
            # print(encrypted_flag)
            if encrypted_guess == encrypted_flag:
                flag = flag_guess
                # print(l, end="", flush=True) 
                break
    
    print(flag)  