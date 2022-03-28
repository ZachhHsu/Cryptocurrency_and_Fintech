

import hashlib,base58,binascii,ecdsa,codecs

# Generate Private Key
PrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
print("Private Key =", PrivateKey.to_string().hex())

# Generate Public Key from private key
PublicKey = '04' +  PrivateKey.get_verifying_key().to_string().hex()
print("Public Key =", PublicKey)

# Hash public key using SHA256
hash256 = hashlib.sha256(binascii.unhexlify(PublicKey)).hexdigest()
print("SHA256(Public Key) =", hash256)

# Hash again using RIDEMP160
ridemp160 = hashlib.new('ripemd160', binascii.unhexlify(hash256))
print("RIDEMP160(SHA256(Public Key)) =", ridemp160.hexdigest())

# Add 00 at the begining (Prepended value)
prepended = '00' + ridemp160.hexdigest()
print("Prepend RIDEMP160(SHA256(ECDSA Public Key)) =", prepended)

# Hash twice again using SHA256 to generate Checksum
hash_once = hashlib.sha256(binascii.unhexlify(prepended)).hexdigest()
hash_double = hashlib.sha256(binascii.unhexlify(hash_once)).hexdigest()
print("Double SHA256 Hash =", hash_double)

# Get first 4 bytes as Checksum
cheksum = hash_double[:8]
print("Checksum(first 4 bytes) =", cheksum)

# Append Checksum to the prepended value
appended = prepended + cheksum
print("Append Checksum to RIDEMP160(SHA256(ECDSA Public Key)) =", appended)

# Encode with Base58
address = base58.b58encode(binascii.unhexlify(appended))
print("Bitcoin Address =", address.decode('utf8'))
