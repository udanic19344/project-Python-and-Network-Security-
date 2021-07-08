import hashlib

result = hashlib.md5(b'ShapeAI')
print(" The byte equivalent of hash is: ", end= " ")
print(result.digest())
