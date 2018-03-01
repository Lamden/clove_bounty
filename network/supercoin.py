from clove.network.bitcoin import Bitcoin


class SuperCoin(Bitcoin):
    """
    Class with all the necessary SuperCoin network information based on
    https://github.com/CryptoUnited-Clients/SuperCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'supercoin'
    symbols = ('SUPER', )
    seeds = ("app1.super-coin.net", "app2.super-coin.net")
    port = 19390
    message_start = b'\xdb\xfa\xfc\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 191
    }


# Has no Testnet
