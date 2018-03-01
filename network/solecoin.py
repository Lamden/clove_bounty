from clove.network.bitcoin import Bitcoin


class Solecoin(Bitcoin):
    """
    Class with all the necessary Solecoin network information based on
    https://github.com/thesolecoin/SoleCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'solecoin'
    symbols = ('SOLE', )
    seeds = ("50.116.32.118",
             "23.239.21.88",
             "106.185.33.98",
             "66.228.43.38",
             "114.215.182.130")
    port = 20631
    message_start = b'\x7e\x15\xd2\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
