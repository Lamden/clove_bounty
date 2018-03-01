from clove.network.bitcoin import Bitcoin


class DFSCoin(Bitcoin):
    """
    Class with all the necessary DFSCoin network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'dfscoin'
    symbols = ('DFS', )
    seeds = ('192.155.85.156')
    port = 20373
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 153
    }


# Has no testnet
