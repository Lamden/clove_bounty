from clove.network.bitcoin import Bitcoin


class CacheCoin(Bitcoin):
    """
    Class with all the necessary CacheCoin network information based on
    https://github.com/kalgecin/cachecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cachecoin'
    symbols = ('CACH', )
    seeds = ('seed.novacoin.su')
    port = 2225
    message_start = b'\xd9\xe6\xe7\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 87,
        'SECRET_KEY': 156
    }


# Has no Testnet
