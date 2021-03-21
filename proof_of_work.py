
class ProofOfWork:

    def __init__(self, block_hash, difficulty) -> None:
        
        self.difficulty = difficulty
        self.block_hash = block_hash

    def hashBlock(self, _increase_nonce=None, _recalculate_hash=None):

        while(self.block_hash[0: self.difficulty] != ''.join(["0" for _ in range(self.difficulty)])):
            
            if _increase_nonce:
                _increase_nonce()
            
            if _recalculate_hash:
                self.block_hash = _recalculate_hash()