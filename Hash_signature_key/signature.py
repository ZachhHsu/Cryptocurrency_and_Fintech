
from Crypto.PublicKey import RSA
from hashlib import sha512

# Generate key pairs
keyPair = RSA.generate(bits=1024)               
keyModulus = keyPair.n
publicKey = keyPair.e
privateKey = keyPair.d
print('Public key =', hex(publicKey))
print('Private key =', hex(privateKey))

msg = 'Here is my 1 BTC for you'
print('Oringal message =', msg)

# To sign the message
msg_bytes = bytes(msg, 'utf-8')
hash = int.from_bytes(sha512(msg_bytes).digest(), byteorder='big')
print('Hash value of msg =', hash)

# pow() calculates exponentiation with a modulus, same as (signature = hash ** privateKey % keyModulus), but much faster
signature = pow(hash, privateKey, keyModulus)
print('Signature =', hex(signature))

# Hash again to verify the signature
# +++ Your Code Below +++
hashfromsignature = pow(signature, publicKey, keyModulus)
print('Is this valid signature:', hash == hashfromsignature)


# Tamper signature and verify again 
msg_hack = 'No money for you' 
msg = bytes(msg_hack, 'utf-8')
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashfromsignature = pow(signature, publicKey, keyModulus)
print('Is this valid signature:', hash == hashfromsignature)




