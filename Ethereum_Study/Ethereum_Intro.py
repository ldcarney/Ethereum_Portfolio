#This is my introduction to the Ethereum Protocol - covering the basics and connecting to a simulated node
from web3 import Web3 

#Ether to wei
wei = Web3.toWei(1, 'ether')
print(f'1 ether is equal to {wei} wei')

#500000000 wei to gwei
gwei = Web3.fromWei(500000000, 'gwei')
print(f'500000000 wei is equal to {gwei} gwei')

#Simulated Node
w3 = Web3(Web3.EthereumTesterProvider())

#Check Connection to Node
print('Connection Status:', w3.isConnected())

#Show simulated accounts
print('Accounts:', w3.eth.accounts)

#Display balance of first account
balance1 = w3.eth.get_balance(w3.eth.accounts[0])
#Convert Balance to Ether
toEther = w3.fromWei(balance1, 'ether')
print(f'The balance of the first account is equal to: {toEther} ether' )

#Look at Block Data
print('\n Block Data:', w3.eth.get_block('latest'))

#--------------TRANSACTION-----------------
#Sending 3 Ether from one account to another
tx_hash = w3.eth.sendTransaction({
	'from': w3.eth.accounts[0],
	'to': w3.eth.accounts[1],
	'value': w3.toWei(3, 'ether')
	})

#Typically would need to wait for the transaction to be mined
#w3.eth.waitForTransactionReceipt(tx_hash)

#View Transaction
print('\n Transaction:', w3.eth.getTransaction(tx_hash))
print('')

#Check Balances of two acounts involved to ensure transaction executed accurately 
print('Account Balance of sender:', w3.eth.get_balance(w3.eth.accounts[0]))
print('Account Balance of receiver:', w3.eth.get_balance(w3.eth.accounts[1]))





