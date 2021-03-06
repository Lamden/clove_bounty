from clove.network.bitcoin import Bitcoin


class CanadaeCoin(Bitcoin):
    """
    Class with all the necessary Canada eCoin network information based on
    https://github.com/Canada-eCoin/Canada-eCoin-qt/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'canada_ecoin'
    symbols = ('CDN', )
    seeds = ("alberta.canadaecoin.net", )
    port = 34331
    message_start = b'\xfd\xc4\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CanadaeCoinTestNet(CanadaeCoin):
    """
    Class with all the necessary Canada eCoin testing network information based on
    https://github.com/Canada-eCoin/Canada-eCoin-qt/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-canada_ecoin'
    seeds = ("ontario.canadaecoin.net", )
    port = 41331
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 87,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 215
    }
