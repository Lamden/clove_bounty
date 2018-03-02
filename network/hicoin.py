from clove.network.bitcoin import Bitcoin


class HiCoin(Bitcoin):
    """
    Class with all the necessary HiCoin network information based on
    https://github.com/hicoindev/hicoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'hicoin'
    symbols = ('XHI', )
    nodes = ('45.32.35.123', )
    port = 35289
    message_start = b'\xb4\xfc\xc8\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 38,
        'SECRET_KEY': 168
    }


# Has no Testnet
