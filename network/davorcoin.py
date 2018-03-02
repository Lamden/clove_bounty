from clove.network.bitcoin import Bitcoin


class DavorCoin(Bitcoin):
    """
    Class with all the necessary DavorCoin network information based on
    https://github.com/davorcc/DavorCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'davorcoin'
    symbols = ('DAV', )
    nodes = ("52.77.118.10", )
    port = 17511
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 158
    }

# No testnet
