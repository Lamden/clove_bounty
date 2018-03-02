from clove.network.bitcoin import Bitcoin


class Xenixcoin(Bitcoin):
    """
    Class with all the necessary Xenixcoin network information based on
    https://github.com/xenixcoin/xenixcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xenixcoin'
    symbols = ('XEN', )
    nodes = ("92.63.57.235", "92.63.57.104", )
    port = 5556
    message_start = b'\xff\xef\xeb\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 203
    }

# no testnet
