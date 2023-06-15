from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from Crypto import Random


def aesEncrypt(message, key, iv):
    cipher_Encrypt = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher_Encrypt.encrypt(message)
    return ciphertext


def aesDecrypt(encrypted, key, iv):
    cipher_Decrypted = AES.new(key, AES.MODE_OFB, iv)
    plaintext = cipher_Decrypted.decrypt(encrypted)
    return plaintext


def aesEncryptWithSHA512(message, key, iv):
    hash_Func = SHA512.new()
    hash_Func.update(message)
    hashOfMsg = hash_Func.digest()
    print("SHA512(msg):", hashOfMsg.hex())
    return aesEncrypt(hashOfMsg + message, key, iv)


def aesDecryptWithSHA512(encryptedWithSHA512, key, iv):
    decryptedTemp = aesDecrypt(encryptedWithSHA512, key, iv)
    decryptedSHA512 = decryptedTemp[:64]
    decryptedMsg = decryptedTemp[64:]
    return decryptedSHA512, decryptedMsg


def verifySHA512(decryptedSHA512, decryptedMsg):
    hash_Func = SHA512.new()
    hash_Func.update(decryptedMsg)
    if hash_Func.hexdigest() == decryptedSHA512.hex():
        return True
    else:
        return False



def main():
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    message = b'게이볼그 삭제해 씹년아'

    key = Random.new().read(KEY_SIZE)
    iv = Random.new().read(BLOCK_SIZE)

    print("AES key: ", key)
    print("IV: ", iv)

    # encrypted = aesEncrypt(message, key, iv)
    # print("Encrypted: ", encrypted.hex())

    encryptedWithSHA512 = aesEncryptWithSHA512(message, key, iv)
    print("Encrypted E(H(M)+M): ", encryptedWithSHA512.hex())

    # decrypted = aesDecrypt(encrypted, key, iv)
    # print("Decrypted: ", decrypted.decode())

    decryptedSHA512, decryptedMsg = aesDecryptWithSHA512(encryptedWithSHA512, key, iv)
    print("Decrypted SHA512: ",decryptedSHA512.hex())
    print("Decrypted Message: ",decryptedMsg)
    
    if(verifySHA512(decryptedSHA512, decryptedMsg)):
        print("Integrity OK, Correct Hash")
    else:
        print("Incorrect Hash")



if __name__ == "__main__":
    main()