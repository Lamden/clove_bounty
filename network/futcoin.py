from clove.network.bitcoin import Bitcoin


class FutCoin(Bitcoin):
    """
    Class with all the necessary FutCoin network information based on
    https://github.com/Futcoin/Futcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'futcoin'
    symbols = ('FUTC', )
    seeds = ("seed1.FutCoin.eu", )
    port = 2345
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 95,
        'SECRET_KEY': 163
    }

# No testnet
