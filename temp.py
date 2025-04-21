import hashlib

# encrypter  adında bir şifreleme sinifi
class Encrypter:
    
    def __init__(self,metin):
        self.metin = metin
    
    def md5(self):
        sifre = hashlib.md5((self.metin).encode())
        return sifre.hexdigest()
    def sha1(self):
        sifre = hashlib.sha1((self.metin).encode())
        return sifre.hexdigest()
    
    def sha256(self):
        sifre = hashlib.sha256((self.metin).encode())
        return sifre.hexdigest()
    
    def sha512(self):
        sifre = hashlib.sha512((self.metin).encode())
        return sifre.hexdigest()
    
deneme = Encrypter("Sifrelenecek Metin")
print(deneme.md5())
print(deneme.sha1())
print(deneme.sha256())
print(deneme.sha512())