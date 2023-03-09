from menu import menuText
import caesar
import atbash
import affine

def main():
    print(menuText)
    caesarEncryption = caesar.CeaserEncryption()
    atbashEncryption = atbash.AtbashEncryption()
    affineEncryption = affine.AffineEncryption()

    # message = "hello my name is philip and i am doing a codenation course"
    # print(f"original message: {message}")

    # encrypted = affineEncryption.encrypt(message)
    # print(f"encrypted message: {encrypted}")

    decrypted = caesarEncryption.decrypt("axeeh fr gtfx bl iabebi", 7)
    print(f"decrypted message: {decrypted}")


if __name__ == '__main__':
    main()