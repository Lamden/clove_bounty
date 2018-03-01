from clove.network.bitcoin import Bitcoin


class Canada_eCoin(Bitcoin):
    """
    Class with all the necessary Canada eCoin network information based on
    https://github.com/Canada-eCoin/Canada-eCoin-qt/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'canada_ecoin'
    symbols = ('CDN', )
    seeds = ("alberta.canadaecoin.net")
    port = 34331
    message_start = b'\xfd\xc4\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class Canada_eCoinTestNet(Canada_eCoin):
    """
    Class with all the necessary Canada eCoin testing network information based on
    https://github.com/Canada-eCoin/Canada-eCoin-qt/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-canada_ecoin'
    seeds = ("ontario.canadaecoin.net")
    port = 41331
