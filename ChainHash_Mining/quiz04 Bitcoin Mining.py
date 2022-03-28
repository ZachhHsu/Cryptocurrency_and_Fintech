# Quiz 4: Bitcoin Mining

import hashlib as hl
import time as ti
import pprint as pp

# Generate hash value from a text (string)
def sha256_hash(text):
    hash_value = hl.sha256(text.encode("ascii")).hexdigest()
    return hash_value

# Given the block data and the required number of leading zeros,
# can you generate a hash value with this number of leading zeros
# by changing the value of NONCE? 
def mine(block, num_zeros):
    required_str = '0' * num_zeros
    print('You must generate a hash value with this leading string =', required_str)
    # +++ Your Code Below +++
    for nonce in range(99999):
        block['nonce'] = nonce
        hash_val = sha256_hash(str(block))
        leading_str = hash_val[:num_zeros]
        if leading_str == required_str:
            print('I found Nonce =', nonce)
            return block
    # +++ Your Code Above +++
    print('NONCE not found and my computer is exhausted!')
    return

# Two transactions in the block with their hash values being their transacton identifications
tx1 = {'TxIn': 'Alice_1.00BTC', 'TxOut': 'Bob_0.98BTC', 'Fee': '0.02BTC'}
tx2 = {'TxIn': 'Bob_0.50BTC', 'TxOut': 'John_0.49BTC', 'Fee': '0.01BTC'}
tx1_hash = sha256_hash(str(tx1))
tx2_hash = sha256_hash(str(tx2))
this_block = {'height': 2, 'previousblockhash': '0000000000000000000000000000abcdefghijklmnopqrstuvwxyz0123456789', tx1_hash: tx1, tx2_hash:tx2}
pp.pprint(this_block)

# Let's say, you need to have three leading ZEROs in the hash value: '000...'
difficulty = 10
time_begin = ti.time()
mined_block = mine(this_block, difficulty)
print()
pp.pprint(mined_block)
print()
time_end = ti.time()
time_taken = time_end - time_begin
print("Mining process took", round(time_taken,2), "seconds")
