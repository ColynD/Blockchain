import random


def tx_rand(): return "TxID_" + str(random.randint(1, 100)).zfill(3)


def miner_rand(): return "Miner_" + str(random.randint(1, 5)).zfill(2)
