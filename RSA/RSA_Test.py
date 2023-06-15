from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as PK

def gen_RSA_Key(userName):
    privateKey = RSA.generate(2048)
    priKey = privateKey.exportKey('PEM')
    print("%s private Key: %s" % (userName, priKey))
    pubKey = privateKey.publickey()
    print("%s public Key: %s" % (userName, pubKey.exportKey('PEM')))
    return priKey, pubKey


def rsaEncrypt(message, pubKey):
    rsaCipher = PK.new(pubKey)
    ciphertext = rsaCipher.encrypt(message)
    return ciphertext


def rsaDecrypt(encrypted, priKey):
    privateKey = RSA.importKey(priKey)
    rsaCipher = PK.new(privateKey)
    plaintext = rsaCipher.decrypt(encrypted)
    return plaintext

def main():
    message = b'Information Security and Programming, Hwang Ju-Won'
    print("Message: ", message.decode())

    #앨리스와 밥의 RSA 키 쌍 생성
    alice_priKey, alice_pubKey = gen_RSA_Key('alice')
    bob_priKey, bob_pubKey = gen_RSA_Key('bob')

    #앨리스가 밥에게 메시지를 암호화하여 보냄
    #앨리스는 밥의 public Key 사용하여 암호화

    encrypted = rsaEncrypt(message, bob_pubKey)
    print("RSA_Encrypt(message, bob_pubKey) Ciphertext: ", encrypted.hex())

    #네트워크에서 앨리스가 발신한 암호화된 메시지 밥이 수신
    #밥의 개인키를 이용하여 해독
    decrypted = rsaDecrypt(encrypted, bob_priKey)
    print("RSA_Decrypt: ", decrypted.decode())


if __name__ == "__main__":
    main()