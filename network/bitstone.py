from clove.network.bitcoin import Bitcoin


class BitStone(Bitcoin):
    """
    Class with all the necessary BitStone network information based on
    https://github.com/chrysophylax69/bitstone/blob/master/src/net.cpp#L18
    (date of access: 02/14/2018)
    """
    name = 'bitstone'
    symbols = ('BST', )
    seeds = ("bst-seed1.granitecoin.com",
             "bst-seed2.granitecoin.com",
             "bst-seed3.granitecoin.com")
    port = 28392
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
