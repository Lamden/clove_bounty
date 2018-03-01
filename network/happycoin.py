from clove.network.bitcoin import Bitcoin


class Happycoin(Bitcoin):
    """
    Class with all the necessary Happycoin network information based on
    https://www.github.com/happycoinmaster/happycoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'happycoin'
    symbols = ('HPC', )
    seeds = ("seed5.cryptolife.net", "seed3.cryptolife.net",
             "electrum5.cryptolife.net", "seed4.cryptolife.net", "explore.cryptolife.net")
    port = 12846
    message_start = b'\xb4\xf3\xef\xcc'
    base58_prefixes = {
        'PUBKEY_ADDR': 41,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 169
    }


# Has no testnet
