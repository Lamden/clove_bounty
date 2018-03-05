
from clove.network.bitcoin import Bitcoin


class InterstellarHoldings(Bitcoin):
    """
    Class with all the necessary HOLD network information based on
    http://www.github.com/InterstellarHoldings/InterstellarHoldings/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'interstellar-holdings'
    symbols = ('HOLD', )
    seeds = ('seed1.interstellarcoin.com', 'seed2.interstellarcoin.com', )
    port = 10130
    message_start = b'\x90\x2f\x32\x15'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 100,
        'SECRET_KEY': 153
    }
