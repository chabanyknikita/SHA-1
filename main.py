import hashlib

mystring = input('Enter String to hash (SHA-1): ')
# new str and mystring in bytes and algoritm hash sha1
hash_object = hashlib.sha1(mystring.encode())
# return data in 16 format
print(hash_object.hexdigest())
