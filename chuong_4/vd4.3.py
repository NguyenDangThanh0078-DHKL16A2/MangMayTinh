import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

data1 = "Giao dịch 1"
data2 = "Giao dịch 2"

hash1 = calculate_hash(data1)
hash2 = calculate_hash(data2)

print(f"Hash của '{data1}': {hash1}")
print(f"Hash của '{data2}': {hash2}")

import wed3