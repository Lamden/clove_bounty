from clove.network.bitcoin import Bitcoin


class InflationCoin(Bitcoin):
    """
    Class with all the necessary InflationCoin network information based on
    https://github.com/inflationcoin/inflationcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'inflationcoin'
    symbols = ('IFLT', )
    seeds = ("45.42.189.71", "45.42.189.111")
    port = 11370
    message_start = b'\xdb\xc4\xf1\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 7,
        'SECRET_KEY': 230
    }


# Has no testnet
