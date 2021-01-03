import json 
from web3 import Web3
ganache_url= 'http://127.0.0.1:7545'
infura_url='https://mainnet.infura.io/v3/fef16b16c8b1494593c726bdc91e8920'
web3=  Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
account_1=Web3.toChecksumAddress('0xD96Ddfd2eAAB473BAD903bF9B70b09FB61b20019')

account_2=Web3.toChecksumAddress('0xA7c2d785cd210463576F5652182dcAEc0B169d5E')

private_key='61c654e29f0430cca05c1d0a97dff5d458ae7d06503a123652e31dd5a1c69579'
## ger nonce
nonce= web3.eth.getTransactionCount(account_1)
## build a transaction 
tx= {
'nonce': nonce,
'to': account_2,
'value': web3.toWei(1,'ether'),
'gas': 2000000,
'gasPrice': web3.toWei('50','gwei')
}

print('hello')
##sign the transaction
signed_tx= web3.eth.account.signTransaction(tx,private_key)

##bradcast transaction
tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)
##get hash
print(tx_hash)

