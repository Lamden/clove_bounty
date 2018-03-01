from clove.network.bitcoin import Bitcoin


class GeertCoin(Bitcoin):
    """
    Class with all the necessary GeertCoin network information based on
    https://github.com/geertaltcoin/geertcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'geertcoin'
    symbols = ('GEERT', )
    seeds = ('dnsseed.geertcoin.com')
    port = 64333
    message_start = b'\xf8\xd2\xe3\xbc'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }


# Has no Testnet
