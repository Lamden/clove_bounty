from clove.network.bitcoin import Bitcoin


class Pesetacoin(Bitcoin):
    """
    Class with all the necessary Pesetacoin (PTC) network information based on
    https://github.com/FundacionPesetacoin/Pesetacoin-0.9.1-Oficial/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'pesetacoin'
    symbols = ('PTC', )
    seeds = ('dnsseed.pesetacoin.info', )
    port = 16639
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 47,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 175
    }


class PesetacoinTestNet(Pesetacoin):
    """
    Class with all the necessary Pesetacoin (PTC) testing network information based on
    https://github.com/FundacionPesetacoin/Pesetacoin-0.9.1-Oficial/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-pesetacoin'
    seeds = ('test-seed.pesetachain.info', )
    port = 26339
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 113,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 241
    }
