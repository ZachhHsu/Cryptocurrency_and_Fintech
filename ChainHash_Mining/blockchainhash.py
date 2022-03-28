import hashlib as hl
import pandas as pd
import pprint as pp

# Generate hash value from a text (string)
def sha256_hash(text):
    hash_value = hl.sha256(text.encode("ascii")).hexdigest()
    return hash_value
    
# Two transactions in Block 1 with their hash values being their transacton IDs
tx1 = {'TxIn': 'Alice_1.00BTC', 'TxOut': 'Bob_0.98BTC', 'Fee': '0.02BTC'}
tx2 = {'TxIn': 'Bob_0.50BTC', 'TxOut': 'John_0.49BTC', 'Fee': '0.01BTC'}
tx1_hash = sha256_hash(str(tx1))
tx2_hash = sha256_hash(str(tx2))
block1 = {'height': 2, 'previousblockhash': '0123456789abcdefghijklmnopqrstuvwxyz', tx1_hash: tx1, tx2_hash:tx2}
print('Block 1 =')
pp.pprint(block1)

# Calcualte the hash value of the entire block 1
block1_hash = sha256_hash(str(block1))
print('-------------------------------------------------------------------------------')
print('Block 1 Hash =', block1_hash)
print('-------------------------------------------------------------------------------')

# Another two transactions in Block 2 with their hash values being their transacton IDs
tx3 = {'TxIn': 'John_0.10BTC', 'TxOut': 'Alice_0.06BTC', 'Fee': '0.04BTC'}
tx4 = {'TxIn': 'Bob_0.20BTC', 'TxOut': 'Alice_0.10BTC', 'Fee': '0.10BTC'}
tx3_hash = sha256_hash(str(tx3))
tx4_hash = sha256_hash(str(tx4))
block2 = {'height': 3, 'previousblockhash': block1_hash, tx3_hash: tx3, tx4_hash: tx4}
print('Block 2 =')
pp.pprint(block2)

# Calcualte the hash value of the entire block 2
block2_hash = sha256_hash(str(block2))
print('-------------------------------------------------------------------------------')
print('Block 2 Hash =', block2_hash)
print('-------------------------------------------------------------------------------')