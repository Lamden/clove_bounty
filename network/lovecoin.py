from clove.network.bitcoin import Bitcoin


class LOVEcoin(Bitcoin):
    """
    Class with all the necessary LOVEcoin network information based on
    https://github.com/lovecoin-project/lovecoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'lovecoin'
    symbols = ('LOVE', )
    seeds = ("dnsseed.btc5.net", )
    port = 8863
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 143
    }

# no testnet
