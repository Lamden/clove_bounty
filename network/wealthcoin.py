from clove.network.bitcoin import Bitcoin


class WealthCoin(Bitcoin):
    """
    Class with all the necessary WealthCoin network information based on
    https://github.com/WealthCoinDev/WealthCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wealthcoin'
    symbols = ('WEALTH', )
    nodes = ("104.236.220.47", )
    port = 15152
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 201
    }

# no testnet
