from clove.network.bitcoin import Bitcoin


class Bankcoin(Bitcoin):
    """
    Class with all the necessary Bankcoin network information based on
    https://github.com/bankcoin18/bankcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'bankcoin'
    symbols = ('B@', )
    nodes = ("172.104.187.169", "172.104.173.190", )
    port = 32886
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 154
    }

# Has no testnet
