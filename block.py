import hashlib
from proof_of_work import ProofOfWork
import time
import json
from typing import Sequence
from transaction import Transaction

class Block:

    def __init__(self, transactions: Sequence[Transaction], previous_hash=''):

        self.previous_hash = previous_hash
        self.transactions = transactions
        self.time_stamp = time.time()
        self.block_hash = ''
        self.nonce = 0

    def calculate_hash(self) -> str:

       string_to_hash = str(self.transactions) + self.previous_hash + str(self.time_stamp) + str(self.nonce)

       return hashlib.sha256(string_to_hash.encode()).hexdigest()

    def increase_nonce(self) -> None:

        self.nonce += 1

    def assign_hash(self) -> str:
        self.block_hash = self.calculate_hash()
        return self.block_hash

    def mine_block(self, difficulty) -> None:

        print(f'\nMining Block {self.block_hash}')

        self.assign_hash()
        proof_of_work = ProofOfWork(self.block_hash, difficulty)
        proof_of_work.hashBlock(self.increase_nonce, self.assign_hash)

    def __str__(self) -> str:
        
        return f'{self.previous_hash}|{self.transactions}|{self.time_stamp}|{self.block_hash}'