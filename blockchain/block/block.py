import time
import hashlib


class Block():
    nonce = 0
    hash = ""

    def __init__(self, index: int, previous_hash: bytes, transactions: list):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions

    def get_block_information(self):
        transaction_str_list = []

        for transaction in self.transactions:
            transaction_str_list.append(str(transaction))

        block_info = {
            "index": self.index,
            "nonce": self.nonce,
            "hash": self.hash,
            "previous hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": transaction_str_list
        }

        return block_info
    
    async def mine(self):
        while(self.hash[:4] != "0000"):
            self.hash = await self.calc_hash()
            self.nonce = self.nonce + 1

    async def calc_hash(self):
        data = self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.nonce)

        return hashlib.sha256(data.encode()).hexdigest()
