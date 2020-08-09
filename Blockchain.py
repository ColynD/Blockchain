import hashlib
from Block import Block
from Blockchain_lib import tx_rand, miner_rand
from datetime import datetime

mining_difficulty = 2
mining_difficulty_str = '0'.zfill(mining_difficulty)
print("Mining Difficulty: " + str(mining_difficulty) + " (hash begins with " + mining_difficulty_str + ")")
solve_times = []
Blocks = []
Current_BlockID = 0

previous_hash = '0'.zfill(64)
genesis_block = Block(previous_hash, ["(50 Mined BTC --> Satoshi)"])
print("Block " + str(Current_BlockID).zfill(3) +
      " | Hash: " + previous_hash + " | Inputs: " + ', '.join(genesis_block.txs))

previous_hash = genesis_block.block_hash
while Current_BlockID < 10:
    nonce = 1
    current_block = Block(previous_hash, [tx_rand(), tx_rand(), "50 BTC --> " + miner_rand(), str(nonce)])
    start_time = datetime.now()
    while current_block.block_hash[:mining_difficulty] != mining_difficulty_str:
        current_block = Block(previous_hash, ["Nonce_" + str(nonce).zfill(8), "(50 Mined BTC -> " + miner_rand() + ")",
                                              tx_rand(), tx_rand(), tx_rand(), tx_rand(), tx_rand()])
        # print("Nonce_" + str(nonce).zfill(8) + ": " + current_block.block_hash)
        nonce += 1
    Current_BlockID += 1
    solve_time = (datetime.now() - start_time).total_seconds()
    print(" | ".join(["Block " + str(Current_BlockID).zfill(3),
                      "Hash: " + current_block.block_hash,
                      "Inputs: " + previous_hash + ", " + ', '.join(current_block.txs),
                      "Time: " + str(solve_time) + " sec"]))
    solve_times.append(solve_time)
    previous_hash = current_block.block_hash

print(solve_times)
