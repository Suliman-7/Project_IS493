# Encryption alphabet

alphabet_letters_list = {'a': '00',

              'b': '01',

              'c': '02',

              'd': '03',

              'e': '04',

              'f': '05',

              'g': '06',

              'h': '07',

              'i': '08',

              'j': '09',

              'k': '10',

              'l': '11',

              'm': '12',

              'n': '13',

              'o': '14',

              'p': '15',

              'q': '16',

              'r': '17',

              's': '18',

              't': '19',

              'u': '20',

              'v': '21',

              'w': '22',

              'x': '23',

              'y': '24',

              'z': '25',

              ' ': '32'}

# Decryption alphabet

alphabet_d = {n: c for c, n in alphabet_letters_list.items()}


# Euclidian Algorithm: Find GCD of two numbers

def gcd(a, b):
    if (b == 0):

        return abs(a)

    else:

        return gcd(b, a % b)


# Generate encryption keys, e, and d

def generate_keys(p, q):
    # Part of public key (N)

    n = p * q

    # Part of private key (e)

    N0 = (p - 1) * (q - 1)

    # Part of public key

    # Find e: first integer relatively prime to N0

    for i in range(2, N0):

        if gcd(i, N0) == 1:
            e = i

            break

    # Part of private key

    # Find d: multiplicative inverse of e % N0

    for i in range(0, N0):

        if ((e * i) % N0) == 1:
            d = i

            break

    return n, e, d


# Encrypt character

def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)


# Decrypt character

def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)


# Split word into characters

def split(word):
    return [char for char in word]


# Encrypt message

def encrypt_message(msg, N, e):
    # Messages

    plaintext = msg.lower().split()

    encrypted = []

    # Exncrypt message

    for word in plaintext:
        # Split word into characters

        chars = split(word)

        # Create list of encrypted characters

        encrypted_chars = [encrypt(alphabet_letters_list[char], N, e) for char in chars]

        # Add encrypted word to list

        encrypted_word = " ".join(encrypted_chars)

        encrypted.append(encrypted_word)

    # Join encrypted words with space characters

    encrypted = f" {encrypt(alphabet_letters_list[' '], N, e)} ".join(encrypted)

    return encrypted


# Decrypt message

def decrypt_message(msg, N, d):
    # Messages

    encrypted = msg.split()

    decrypted = []

    plaintext = []

    # Decrypt

    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Decipher message

    for char in decrypted:
        plaintext.append(alphabet_d[char])

    plaintext = "".join(plaintext)

    return plaintext


# Option Menu

def options():
    print("Options:\n\
    0 - Generate Key Pair\n\
    1 - Encrypt message in terminal\n\
    2 - Decrypt message in terminal\n")

# User interface


while True:

    # Show options

    options()

    # Get selection from user

    selection = input()

    # Generate key pair

    if selection == "0":

        # Get prime numbers

        p = int(input("Enter the first prime number: "))

        q = int(input("Enter the second prime number: "))

        print()

        try:

            # Generate values for encryption / decryption

            N, e, d = generate_keys(p, q)

            # Show keys

            print(f"Public key:\nN: {N}\ne: {e}\n")

            print(f"Private key:\nN: {N}\nd: {d}\n")



        except:

            print("Error: Invalid Primes\n")





    # Encrypt message in terminal

    elif selection == "1":

        # Get public key

        N = int(input("Enter public key N: "))

        e = int(input("Enter public key e: "))

        print()

        # Get message from user

        message = input("Enter message to encrypt:\n")

        # Print encrypted message

        print(f"\nEncrypted message:\n{encrypt_message(message, N, e)}\n")



    # Decrypt message in terminal

    elif selection == "2":

        # Get private key

        N = int(input("Enter private key N: "))

        d = int(input("Enter private key d: "))

        print("")

        # Get encrypted message from user

        message = input("Enter message to decrypt:\n")

        # Print decrypted message

        try:

            print(f"\nDecrypted message:\n{decrypt_message(message, N, d)}\n")

        except:

            print("Error: Invalid Private Key\n")



    # Input validation

    else:

        print("Invalid choice\n")

    # Option to exit

    Exit = input("Make another selection?\n\
            'Y' to continue\n\
            any other key to exit\n").upper()

    print()

# Make another selection
    if Exit == "Y":
        continue

 #Exit

    else:
        break



options()



