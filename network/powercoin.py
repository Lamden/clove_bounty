from clove.network.bitcoin import Bitcoin


class Powercoin(Bitcoin):
    """
    Class with all the necessary Powercoin network information based on
    https://github.com/Powercoin/PowerCoinFinal/blob/patch-1/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'powercoin'
    symbols = ('PWR', )
    nodes = ("52.39.155.228", )
    port = 4504
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 12,
        'SCRIPT_ADDR': 43,
        'SECRET_KEY': 140
    }

# no testnet
