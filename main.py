from menu import menuText
import caesar
import atbash
import keyword_c
import affine

def main():
    print(menuText)
    caesarEncryption = caesar.CeaserEncryption()
    atbashEncryption = atbash.AtbashEncryption()
    affineEncryption = affine.AffineEncryption()
    keywordEncryption = keyword_c.KeywordEncryption()

    # message = "hello my name is philip and i am doing a codenation course"
    # print(f"original message: {message}")

    # encrypted = affineEncryption.encrypt(message)
    # print(f"encrypted message: {encrypted}")

    # decrypted = caesarEncryption.decrypt("axeeh fr gtfx bl iabebi", 7)
    # print(f"decrypted message: {decrypted}")

    encrypted = keywordEncryption.encrypt("hello my name is blake encrypted as a hedgehog", "hedgehog")
    print(encrypted)
    print(keywordEncryption.decrypt(encrypted, "hedgehog"))

if __name__ == '__main__':
    main()