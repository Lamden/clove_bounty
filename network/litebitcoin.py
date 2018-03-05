
from clove.network.bitcoin import Bitcoin


class LiteBitcoin(Bitcoin):
    """
    Class with all the necessary LBTC network information based on
    http://www.github.com/litebitcoins/litebitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'litebitcoin'
    symbols = ('LBTC', )
    seeds = ('litebitcoins.thecryptochat.net', )
    port = 19037
    message_start = b'\x5b\x6d\x2f\x54'
    base58_prefixes = {
        'PUBKEY_ADDR': 3,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 131
    }
