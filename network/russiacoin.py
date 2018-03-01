from clove.network.bitcoin import Bitcoin


class RussiaCoin(Bitcoin):
    """
    Class with all the necessary RussiaCoin network information based on
    https://github.com/russiacoindotinfo/russiacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'russiacoin'
    symbols = ('RC', )
    nodes = ("194.135.89.60", )
    port = 19992
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 75,
        'SECRET_KEY': 188
    }


# Has no testnet
