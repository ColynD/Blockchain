import hashlib


class Block:
    block_hash: object

    def __init__(self, prev_hash, tx):
        self.txs = tx
        self.prev_hash1 = prev_hash
        string_hash = "".join(tx) + prev_hash
        self.block_hash = hashlib.sha256(string_hash.encode()).hexdigest()

# hash = hashlib.sha256("secret message".encode()).hexdigest()
# print(hash)