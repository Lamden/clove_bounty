from clove.network.bitcoin import Bitcoin


class Xgox(Bitcoin):
    """
    Class with all the necessary Xgox network information based on
    https://github.com/bumbacoin/xgox/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Xgox'
    symbols = ('XGOX', )
    seeds = ("go1.dynu.net", "go2.dynu.net", )
    port = 23185
    message_start = b'\x71\xae\x76\x64'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }


# Has no Testnet
