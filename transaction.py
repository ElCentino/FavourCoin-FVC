import hashlib

class Transaction:

    def __init__(self, from_address, to_address, amount) -> None:
        
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount

    def calculate_hash(self):

        return hashlib.sha256(self.from_address + self.to_address + str(self.amount))

    def sign_transaction(self):

        pass