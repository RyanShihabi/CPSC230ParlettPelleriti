# Encrypt function with parameters for a text file and a map file
def encrypt(file, map_file):
    # using a dictionary to connect encrypted and decrypted letters
    encrypt_map = {}
    # grabbing text line by line
    text_list = []

    # reading map file
    with open(map_file, "r") as m:
        for cipher in m:
            # grabbing letter to grab and replace
            original, new = cipher.split()
            # adding keys to dictionary to later encrypt
            encrypt_map[original] = new
    # closing map file
    m.close()

    # reading the text file
    with open(file, "r") as f:
        # grabbing all lines
        lines = f.readlines()
        # iterate through each line
        for line in lines:
            text = ""
            # iterate through each letter in the line
            for letter in line:
                # check if letter is in dictionary
                if letter in encrypt_map:
                    # append encrypted letter
                    text += encrypt_map[letter]
                else:
                    # append current letter if not in dictionary
                    text += letter
            # print(text)
            # add encrypted line to the list
            text_list.append(text)

    # close file
    f.close()

    # open encrypted text file with write permissions
    with open("encrypted.txt", "w") as f:
        # write every line in the text list to the file
        for line in text_list:
            f.write(line)
    # close text file
    f.close()

# Decrypt function with parameters for a text file and a map file
def decrypt(file, map_file):
    decrypt_map = {}
    text_list = []

    with open(map_file, "r") as m:
        for cipher in m:
            original, new = cipher.split()
            # creating a new decrypt dictionary with reversed keys
            decrypt_map[new] = original
    m.close()

    # reading encrypted file
    with open(file, "r") as f:
        # repearing the process of encrypt but with the decrypt dictionary
        lines = f.readlines()
        for line in lines:
            text = ""
            for letter in line:
                if letter in decrypt_map:
                    text += decrypt_map[letter]
                else:
                    text += letter
            # print(text)
            text_list.append(text)

    f.close()

    # writing lines to unencrypted text file
    with open("unencrypted.txt", "w") as f:
        for line in text_list:
            f.write(line)
    f.close()


def main():
    # testing encrypt and decrypt functions
    encrypt("file.txt", "replace.txt")
    decrypt("encrypted.txt", "replace.txt")

if __name__ == "__main__":
    main()
