from clove.network.bitcoin import Bitcoin


class LitecoinPlus(Bitcoin):
    """
    Class with all the necessary LitecoinPlus network information based on
    https://github.com/crypto-currency/litecoinplus/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'litecoinplus'
    symbols = ('LCP', )
    seeds = ("lcp.altcoinwarz.com", )
    port = 44351
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 203
    }

# Has no Testnet
