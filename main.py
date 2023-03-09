import caesar
import atbash

def main():
    caesarEncryption = caesar.CeaserEncryption()
    atbashEncryption = atbash.AtbashEncryption()

    message = "hello my name is philip, i am currently doing a codenation course"
    print(f"original message: {message}")

    encrypted = atbashEncryption.encrypt(message)
    print(f"encrypted message: {encrypted}")

    decrypted = atbashEncryption.decrypt(encrypted)
    print(f"decrypted message: {decrypted}")


if __name__ == '__main__':
    main()