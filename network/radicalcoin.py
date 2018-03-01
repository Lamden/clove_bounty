from clove.network.bitcoin import Bitcoin


class Radicalcoin(Bitcoin):
    """
    Class with all the necessary Radicalcoin network information based on
    https://github.com/radicalcoin/RADICAL/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'radicalcoin'
    symbols = ('RADI', )
    nodes = ("5.196.10.57", )
    port = 42522
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }

# no testnet
