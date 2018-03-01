from clove.network.bitcoin import Bitcoin


class Titcoin(Bitcoin):
    """
    Class with all the necessary Titcoin network information based on
    https://github.com/OfficialTitcoin/titcoin-wallet/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'titcoin'
    symbols = ('TIT', )
    seeds = ("titcoin.isasecret.com",
             "titcoin.sytes.net",
             "titcoin.slyip.com",
             "seed.titcoins.info",
             "seed.titcoinpool.com")
    port = 8698
    message_start = b'\x25\x17\x4c\x22'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }
