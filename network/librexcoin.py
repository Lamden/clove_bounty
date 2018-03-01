from clove.network.bitcoin import Bitcoin


class Librexcoin(Bitcoin):
    """
    Class with all the necessary Librexcoin network information based on
    https://github.com/librexcoin/librexcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'librexcoin'
    symbols = ('LXC', )
    nodes = ("192.99.223.96",
             "192.227.251.74",
             "198.23.178.87",
             "23.94.38.173")
    port = 61778
    message_start = b'\xa2\xa2\xa2\xa2'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 158
    }
