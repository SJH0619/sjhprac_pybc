from .block.block import Block


class BlockChain():
    chain = [];
    pending_transaction = [];

    def get_lastest_block(self):
        return self.chain[len(self.chain)-1]
    
    async def create_genesis_block(self):
        genesis_block = Block("0", [])
        await genesis_block.mine()

        self.chain.append(genesis_block)

    def create_transaction(self, transaction):
        self.pending_transaction.append(transaction)
    
    async def mine_pending_transaction(self):
        block = Block(self.get_lastest_block().hash, self.pending_transaction)
        await block.mine()

        self.chain.append(block)
        self.pending_transaction = []
