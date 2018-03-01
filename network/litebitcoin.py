
from clove.network.bitcoin import Bitcoin


class LiteBitcoin(Bitcoin):
    """
    Class with all the necessary LBTC network information based on
    http://www.github.com/litebitcoins/litebitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'litebitcoin'
    symbols = ('LBTC', )
    seeds = ('litebitcoins.thecryptochat.net',)
    port = 19037
    message_start = b'\x5b\x6d\x2f\x54'
    base58_prefixes = {
        'PUBKEY_ADDR': 3,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 131
    }


class LiteBitcoinTestNet(LiteBitcoin):
    """
    Class with all the necessary LBTC testing network information based on
    http://www.github.com/litebitcoins/litebitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-litebitcoin'
    seeds = ()
    port = 19335
    message_start = b'\xae\xc2\xb1\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
