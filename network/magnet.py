from clove.network.bitcoin import Bitcoin


class Magnet(Bitcoin):
    """
    Class with all the necessary Magnet network information based on
    https://github.com/magnetwork/magnet/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'magnet'
    symbols = ('MAG', )
    seeds = ("magdns1.magnetwork.io",
             "magdns2.magnetwork.io",
             "magdns3.magnetwork.io")
    port = 17177
    message_start = b'9162173204'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 83
    }

# no test net
