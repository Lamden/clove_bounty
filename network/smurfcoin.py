from clove.network.bitcoin import Bitcoin


class SmurfCoin(Bitcoin):
    """
    Class with all the necessary SmurfCoin network information based on
    https://github.com/smurfscoin/smf/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'smurfcoin'
    symbols = ('SMF', )
    nodes = ("45.55.83.96", )
    port = 43221
    message_start = b'\xb4\xf9\xe2\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 191
    }

# no testnet
