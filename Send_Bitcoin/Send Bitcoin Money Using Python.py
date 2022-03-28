# More info on 'bit' library -> https://ofek.dev/bit/index.html
# Check your bitcoin balance -> https://blockstream.info/testnet/

import bit

# Generate wallet for payer
#key_1 = bit.PrivateKeyTestnet()
#wallet_1 = key_1.to_wif()
#print('My Wallet =', wallet_1)

# Verify transaction
# https://blockstream.info/testnet/

# Convert wallet ID to private/public key and address
wallet_1 = 'cQXpPpJek79XH9e3rsH7BTngH2D8Qt37yyjDzVEbHMuf3tcqSfGx'
key_1 = bit.wif_to_key(wallet_1)
addr_1 = key_1.address
print('My Address 1 =', addr_1)

addr_2 = 'mmDhGZUsBjqDExPJtVpPKpmZppd6xWN8w9'
print("Professor's Bitcoin Address =", addr_2)

# Beg God for bitcoins (0.001 BTC which is 100,000 satoshi)
# https://testnet-faucet.mempool.co/

# Check the payer's balance
print('Balance in Bitcoin =', key_1.get_balance('btc'))

# Verify transaction
# https://blockstream.info/testnet/

# Send money (1 satoshi only which is 0.00000001 BTC) to payee at addr_2
tx_hash = key_1.send([(addr_2, 1, 'satoshi')])
print('Transaction Hash =', tx_hash)

# Check the payer's balance
print('Balance in Bitcoin =', key_1.get_balance('btc'))

# Verify transaction
# https://blockstream.info/testnet/
