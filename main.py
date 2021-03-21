from time import time
from transaction import Transaction
from blockchain import BlockChain

import time

FVC: BlockChain = BlockChain()

FVC.create_transaction(Transaction('address1', 'address2', 10))
FVC.create_transaction(Transaction('address1', 'address2', 50))

print('\nStarting miner....')

FVC.mine_pending_transaction('favours-address')

print(f"\nFavour's balance is {FVC.get_balance_of_address('favours-address')}")

print('\nStarting miner....')

FVC.mine_pending_transaction('favours-address')

print(f"\nFavour's balance is {FVC.get_balance_of_address('favours-address')}")

print('\nSending 50 FVCs to address2')
FVC.create_transaction(Transaction('favours-address', 'address2', 100))

FVC.mine_pending_transaction('favours-address')

print(f"\nFavour's balance is {FVC.get_balance_of_address('favours-address')}")
print(f"\nAddress2 balance is {FVC.get_balance_of_address('address2')}")




