import hashlib
import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []  # The blockchain
        self.current_transactions = []  # List of current transactions
        # Create the genesis block (the first block)
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        # Create a new block and add it to the chain
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block

    def get_previous_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        # Simple Proof of Work algorithm
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Hash the new proof and check if it starts with '0000'
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        # Add a new transaction to the current list of transactions
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        # Return the index of the block that will store this transaction
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        # Check if the blockchain is valid
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            # Check if the hash of the block is valid
            if block.previous_hash != previous_block.hash:
                return False

            # Validate proof of work
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] != '0000':
                return False

            # Move to the next block
            previous_block = block
            block_index += 1

        return True
