import asyncio
from blockchain.blockchain import BlockChain
from blockchain.block.transaction import Transaction


async def main():
    print("블록체인 시작, 제네시스블록 생성")

    blockchain = BlockChain()
    await blockchain.create_genesis_block()

    print("트랜잭션 A to B 1")
    blockchain.create_transaction(Transaction(sender="A", receiver="B", amount=1));
    print("트랜잭션 B to C 1")
    blockchain.create_transaction(Transaction(sender="B", receiver="C", amount=1));

    await blockchain.mine_pending_transaction()

    print("트랜잭션 C to D 1")
    blockchain.create_transaction(Transaction(sender="C", receiver="D", amount=1));
    print("트랜잭션 D to E 1")
    blockchain.create_transaction(Transaction(sender="D", receiver="E", amount=1));

    await blockchain.mine_pending_transaction()

    for chain in blockchain.chain:
        print(chain.get_block_information())

asyncio.run(main())
