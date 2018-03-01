from clove.network.bitcoin import Bitcoin


class Tellurion(Bitcoin):
    """
    Class with all the necessary Tellurion network information based on
    https://github.com/telluriondev/tellurion/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tellurion'
    symbols = ('TELL', )
    seeds = ("seed1.tellurion.co", "seed2.tellurion.co",
             "seed3.tellurion.co", "seed4.tellurion.co",
             "ok1.altcoinsfoundation.com")
    port = 9999
    message_start = b'\x1a\x1c\x3a\x1b'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 193
    }


# Has no testnet
