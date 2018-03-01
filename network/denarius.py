from clove.network.bitcoin import Bitcoin


class Denarius(Bitcoin):
    """
    Class with all the necessary Denarius network information based on
    https://github.com/carsenk/denarius/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Denarius'
    symbols = ('DNR', )
    seeds = ("172.93.53.210", "104.233.106.135", "104.238.169.5",
             "147.135.191.162", "dnsseed.denarius.name")
    port = 33339
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 90,
        'SECRET_KEY': 158
    }


# Has no Testnet
