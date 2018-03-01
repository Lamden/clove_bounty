from clove.network.bitcoin import Bitcoin


class Printerium(Bitcoin):
    """
    Class with all the necessary Printerium network information based on
    https://github.com/printerium/printerium-project/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'printerium'
    symbols = ('PRX', )
    seeds = ("199.127.227.51")
    port = 10321
    message_start = b'\x0d\x37\x3b\x52'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }


# Has no testnet
