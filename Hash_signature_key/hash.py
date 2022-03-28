import hashlib, binascii
import pandas as pd

# Oringal plain text
text = 'Firstname Lastname'
text_bytes = text.encode("utf8")
print ('text =', text)
print('===============================================================================')

# Hashed using RIDEMP160
ridemp160 = hashlib.new('ripemd160', text_bytes)
print("RIDEMP160(text) =", ridemp160.hexdigest())
print('===============================================================================')

# Hashed using SHA256
hash256 = hashlib.sha256(text_bytes)
print("SHA256(text) =", hash256.hexdigest())
print('===============================================================================')

# You can change just one letter in the text
# Do you see any change in hashed values?
