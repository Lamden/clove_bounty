from clove.network.bitcoin import Bitcoin


class TeslaCoin(Bitcoin):
    """
    Class with all the necessary TeslaCoin network information based on
    https://github.com/teslacoinfoundation/teslacoin-v.3.3/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'teslacoin'
    symbols = ('TES', )
    seeds = ("electrum4.cryptolife.net",
             "tesla-coin.com",
             "node1.tesla-coin.com",
             "node2.tesla-coin.com",
             "tes1.altcoinsfoundation.com",
             "seed1.teslacoinfoundation.org",
             "seed1.teslachain.info",
             "seed2.teslachain.info",
             "108.49.185.3",
             "115.28.38.190",
             "5.189.187.91",
             "74.65.200.29",
             "81.245.187.75",
             "94.177.203.132")
    port = 1856
    message_start = b'\xe5\xd7\xe6\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 139
    }


# has no testnet
