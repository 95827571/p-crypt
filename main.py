import caesar

def main():
    caesarEncryption = caesar.CeaserEncryption()

    message = "abcde"
    print(f"original message: {message}")

    encrypted = caesarEncryption.encrypt(message, 17)
    print(f"encrypted message: {encrypted}")

    decrypted = caesarEncryption.decrypt(encrypted, 17)
    print(f"decrypted message: {decrypted}")


if __name__ == '__main__':
    main()