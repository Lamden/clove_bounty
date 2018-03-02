from clove.network.bitcoin import Bitcoin


class Centurion(Bitcoin):
    """
    Class with all the necessary Centurion network information based on
    https://github.com/centurioncoin/centurion/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'centurion'
    symbols = ('CNT', )
    seeds = ("node1.centurion.org",
             "node1.centurionlab.org",
             "node2.centurionlab.org",
             "node3.centurionlab.org")
    port = 5556
    message_start = b'\xff\xef\xeb\xf1'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }

# Has no testnet
