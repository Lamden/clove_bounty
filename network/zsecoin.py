from clove.network.bitcoin import Bitcoin


class ZSEcoin(Bitcoin):
    """
    Class with all the necessary ZSEcoin network information based on
    https://github.com/Prestige-coin/ZSECOIN/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'zsecoin'
    symbols = ('ZSE', )
    seeds = ("electrum2.cryptolife.net",
             "104.131.17.33",
             "138.68.17.203")
    port = 40919
    message_start = b'\xb9\x98\xe2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 80,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 208
    }
