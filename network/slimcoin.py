from clove.network.bitcoin import Bitcoin


class Slimcoin(Bitcoin):
    """
    Class with all the necessary Slimcoin network information based on
    https://github.com/slimcoin-project/Slimcoin/blob/slimcoin/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'slimcoin'
    symbols = ('SLM', )
    seeds = ("dnsseed.slimcoinpool.com",
             "dnsseed.furiousnomad.com",
             "dnsseed.shitcoinrapist.club")
    port = 41682
    message_start = b'\x6e\x8b\x92\xa5'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }
