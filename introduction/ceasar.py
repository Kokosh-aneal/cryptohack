import string

# import words from linux dictionary
dicts = []
with open('/usr/share/dict/words') as f:
    dicts = f.readlines()

def main():
    print("Ceasar cipher solver")
    msg = Message("Oy IkGyGx CuXqOtM")
    msg.decrypt()


class Message:
    def __init__(self, msg=""):
        self.msg = msg
        self.solutions = []

    # TODO
    def encrypt(self):
        print("Encrypting: ", self.msg)

    def decrypt(self):
        print("Decrypting: ", self.msg)
        decrypted_msg = []
        for i in range(25):
            tmp_dec_msg = self.shift_msg(i)
            rate = 0
            for w in tmp_dec_msg.split():
                if w.lower()+"\n" in dicts:
                    rate+=1000+len(w)
            self.solutions.append(Solution(tmp_dec_msg, rate, i))

        max_rate = max(self.solutions, key=lambda x: x.rate)
        print("RATE:", max_rate.rate, "| KEY:",max_rate.key, "| MSG:", max_rate.msg)
            

    def shift_msg(self, key=3):
        encrypted_msg = self.msg
        alphabet_low = string.ascii_lowercase
        alphabet_up = string.ascii_uppercase
        decrypted_msg = ""

        for c in encrypted_msg:
            # Check if alpha
            if c in alphabet_low or c in alphabet_up:
                if c.islower():
                    pos = alphabet_low.find(c)
                    new_pos = (pos - key) % 26
                    new_c = alphabet_low[new_pos]
                    decrypted_msg += new_c
                else:
                    pos = alphabet_up.find(c)
                    new_pos = (pos - key) % 26
                    new_c = alphabet_up[new_pos]
                    decrypted_msg += new_c
            else:
                decrypted_msg += c

        return decrypted_msg
    
    def __str__(self):
        return self.msg
    

class Solution:
    def __init__(self, msg="", rate=0, key=3):
        self.msg = msg
        self.rate = rate
        self.key = key

    def __str__(self):
        return self.msg


if __name__ == "__main__":
    main()