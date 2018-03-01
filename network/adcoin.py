
from clove.network.bitcoin import Bitcoin


class AdCoin(Bitcoin):
    """
    Class with all the necessary ACC network information based on
    http://www.github.com/adcoin-project/AdCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'adcoin'
    symbols = ('ACC', )
    seeds = ('node1.getadcoin.com', 'node2.getadcoin.com')
    port = 19499
    message_start = b'\x3d\x05\x35\x77'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class AdCoinTestNet(AdCoin):
    """
    Class with all the necessary ACC testing network information based on
    http://www.github.com/adcoin-project/AdCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-adcoin'
    seeds = ('testnet-seed.adcointools.com',
             'seed-b.adcoin.loshan.co.uk', 'dnsseed-testnet.thrasher.io')
    port = 19335
    message_start = b'\xfd\xd2\xc8\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
