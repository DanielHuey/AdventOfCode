import hashlib

# print(hashlib.algorithms_available)

input:str="ckczppom"
index:int=0

while True:
    sash = hashlib.md5(f"{input}{index}".encode("utf8"))
    if sash.hexdigest().startswith("000000"):
        print(f'{index}: "{sash.hexdigest()}"')
        break
    index+=1