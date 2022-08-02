import hashlib


s = 'Python Bootcamp'
s = bytes(s, 'UTF-8')
hashed = hashlib.md5(s)
print(hashed.hexdigest())
