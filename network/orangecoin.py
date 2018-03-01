from clove.network.bitcoin import Bitcoin


class OrangeCoin(Bitcoin):
    """
    Class with all the necessary OrangeCoin network information based on
    https://github.com/Orangecoins/Orangecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'orangecoin'
    symbols = ('OC', )
    nodes = ("54.235.70.55",
             "54.235.244.167")
    port = 18872
    message_start = b'\xd1\xd4\xb2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 243
    }

# no testnet
