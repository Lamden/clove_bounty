
from clove.network.bitcoin import Bitcoin


class FlorinCoin(Bitcoin):
    """
    Class with all the necessary FLO network information based on
    http://www.github.com/florincoin/florincoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'florincoin'
    symbols = ('FLO', )
    seeds = (
        'seed1.florincoin.org', 'seed2.florincoin.org', 'seed3.florincoin.org', 'seed4.florincoin.org',
        'seed5.florincoin.org', 'seed6.florincoin.org', 'seed7.florincoin.org', 'seed8.florincoin.org',
        'seed1.florincoin.com', 'seed2.florincoin.com', 'seed3.florincoin.com', 'seed4.florincoin.com',
        'nyc2.entertheblockchain.com', 'sf1.entertheblockchain.com', 'am2.entertheblockchain.com',
        'sgp.entertheblockchain.com', 'ind.entertheblockchain.com', 'de.entertheblockchain.com'
    )
    port = 7312
    message_start = b'\xfd\xc0\xa5\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 176
    }


class FlorinCoinTestNet(FlorinCoin):
    """
    Class with all the necessary FLO testing network information based on
    http://www.github.com/florincoin/florincoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-florincoin'
    seeds = ('testseed.florincoin.org', )
    port = 17312
    message_start = b'\xfd\xc0\x5a\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 198,
        'SECRET_KEY': 239
    }
