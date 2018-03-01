from clove.network.bitcoin import Bitcoin


class BestChain(Bitcoin):
    """
    Class with all the necessary BestChain network information based on
    https://github.com/BestChain/Source/blob/BestChain/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bestchain '
    symbols = ('BEST', )
    nodes = ("54.68.215.235",
             "95.211.57.108",
             "94.23.216.214",
             "81.169.212.185",
             "185.16.41.61")
    port = 47949
    message_start = b'\x31\x0e\x83\x36'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
