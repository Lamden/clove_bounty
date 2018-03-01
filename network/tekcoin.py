from clove.network.bitcoin import Bitcoin


class TEKcoin(Bitcoin):
    """
    Class with all the necessary TEKcoin network information based on
    https://github.com/maxxine/tek/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tekcoin'
    symbols = ('TEK', )
    seeds = ("node1.tekcoin.uk",
             "node2.tekcoin.uk",
             "node3.tekcoin.uk",
             "node4.tekcoin.uk",
             "node5.tekcoin.uk")
    port = 8514
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 154
    }


# Has no testnet
