from transaction import Transaction
from block import Block

import json

class BlockChain:

    def __init__(self) -> None:
        
        self.blockchain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self) -> Block:

        return Block([Transaction("00000000000", "111111111111", 0)], "00000")

    def get_latest_block(self) -> Block:

        return self.blockchain[-1]                                                
        
    def mine_pending_transaction(self, mining_reward_address) -> None:

        block: Block = Block(self.pending_transactions)
        block.mine_block(self.difficulty)

        print(f'Block successfully mined {block.block_hash}')
        self.blockchain.append(block)

        self.pending_transactions = [
            Transaction(None, mining_reward_address, self.mining_reward)
        ]

    def create_transaction(self, transaction: Transaction) -> None:

        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address) -> float:

        balance: float = 0

        for block in self.blockchain:

            for trans in block.transactions:

                if trans.from_address == address:

                    balance -= trans.amount

                if trans.to_address == address:

                    balance += trans.amount

        return balance


    def is_chain_valid(self) -> bool:

        block_chain_size = len(self.blockchain) - 1

        for _ in (number + 1 for number in range(block_chain_size)):

            current_block: Block = self.blockchain[_]
            previous_block: Block = self.blockchain[_ - 1]

            if current_block.block_hash != current_block.calculate_hash():

                return False

            if current_block.previous_hash != previous_block.block_hash:

                return False

        return True

    def to_json(self):

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)    