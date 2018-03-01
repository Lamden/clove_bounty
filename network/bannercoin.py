from clove.network.bitcoin import Bitcoin


class BannerCoin(Bitcoin):
    """
    Class with all the necessary BannerCoin network information based on
    https://github.com/bannercoin/bannercoin-source/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'diamond'
    symbols = ('BCOIN', )
    seeds = ("node.walletbuilders.com")
    port = 21265
    message_start = b'\xa9\x17\xdb\x97'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
