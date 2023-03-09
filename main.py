import caesar
import atbash
import affine

def main():
    caesarEncryption = caesar.CeaserEncryption()
    atbashEncryption = atbash.AtbashEncryption()
    affineEncryption = affine.AffineEncryption()

    message = "hello my name is philip and i am doing a codenation course"
    print(f"original message: {message}")

    encrypted = affineEncryption.encrypt(message)
    print(f"encrypted message: {encrypted}")

    decrypted = affineEncryption.decrypt(encrypted)
    print(f"decrypted message: {decrypted}")


if __name__ == '__main__':
    main()