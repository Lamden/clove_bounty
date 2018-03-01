from clove.network.bitcoin import Bitcoin


class CryptoJacks(Bitcoin):
    """
    Class with all the necessary CryptoJacks network information based on
    https://github.com/cryptojacks/cryptojacks/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cryptojacks'
    symbols = ('CJ', )
    seeds = ("node1.cryptojacks.com", "node2.cryptojacks.com", "node3.cryptojacks.com",
             "node4.cryptojacks.com", "node5.cryptojacks.com", "node6.cryptojacks.com", "node7.cryptojacks.com")
    port = 33433
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }

# Has no Testnet
