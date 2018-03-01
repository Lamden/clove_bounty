from clove.network.bitcoin import Bitcoin


class Magnetcoin(Bitcoin):
    """
    Class with all the necessary Magnetcoin network information based on
    https://github.com/magnetcoindev/magnetcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'magnetcoin'
    symbols = ('MAGN', )
    nodes = ('96.44.173.109', )
    port = 22458
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 179
    }


# Has no testnet
