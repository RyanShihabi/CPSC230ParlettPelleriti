def encrypt(file, map_file):
    encrypt_map = {}
    text_list = []

    with open(map_file, "r") as m:
        for cipher in m:
            original, new = cipher.split()
            encrypt_map[original] = new
    m.close()

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            text = ""
            for letter in line:
                if letter in encrypt_map:
                    text += encrypt_map[letter]
                else:
                    text += letter
            print(text)
            text_list.append(text)

    f.close()

    with open("encrypted.txt", "w") as f:
        for line in text_list:
            f.write(line)
    f.close()

def decrypt(file, map_file):
    decrypt_map = {}
    text_list = []

    with open(map_file, "r") as m:
        for cipher in m:
            original, new = cipher.split()
            decrypt_map[new] = original
    m.close()

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            text = ""
            for letter in line:
                if letter in decrypt_map:
                    text += decrypt_map[letter]
                else:
                    text += letter
            print(text)
            text_list.append(text)

    f.close()

    with open("unencrypted.txt", "w") as f:
        for line in text_list:
            f.write(line)
    f.close()


def main():
    encrypt("file.txt", "replace.txt")
    decrypt("encrypted.txt", "replace.txt")

if __name__ == "__main__":
    main()
