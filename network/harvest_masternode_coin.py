
from clove.network.bitcoin import Bitcoin


class HarvestMasternodeCoin(Bitcoin):
    """
    Class with all the necessary HC network information based on
    http://www.github.com/HarvestMasternodecoin/Harvestcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'harvest-masternode-coin'
    symbols = ('HC', )
    nodes = ('107.170.198.173', '192.81.214.238', '159.203.35.209', )
    port = 12116
    message_start = b'\x1d\x7e\xa6\x2d'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class HarvestMasternodeCoinTestNet(HarvestMasternodeCoin):
    """
    Class with all the necessary HC testing network information based on
    http://www.github.com/HarvestMasternodecoin/Harvestcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-harvest-masternode-coin'
    seeds = ()
    port = 20114
    message_start = b'\x1d\x7e\xa6\x2c'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
