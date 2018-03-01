from clove.network.bitcoin import Bitcoin


class Bitgem(Bitcoin):
    """
    Class with all the necessary Bitgem network information based on
    https://github.com/bitgem/bitgem/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Bitgem'
    symbols = ('BTG', )
    seeds = ("bitgem.us", "seed.bitgem.us", )
    port = 7692
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 98,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 226
    }


# Has no Testnet
