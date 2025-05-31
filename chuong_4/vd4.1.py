import hashlib

data1 = "Blockchain là công nghệ nền tảng"
data2 = "blockchain là công nghệ nền tảng"

hash1 = hashlib.sha256(data1.encode()).hexdigest()
hash2 = hashlib.sha256(data2.encode()).hexdigest()

print("Hash 1:", hash1)
print("Hash 2:", hash2)