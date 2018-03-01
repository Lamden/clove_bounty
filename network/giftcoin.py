from clove.network.bitcoin import Bitcoin


class Giftcoin(Bitcoin):
    """
    Class with all the necessary Giftcoin network information based on
    https://github.com/GiftCoin/giftcoin-release/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'giftcoin'
    symbols = ('GFT', )
    seeds = ("seed.giftcoin.info",
             "node.giftcoin.info",
             "nodegift.poolnetwork.org")
    port = 8855
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 39,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 167
    }


class GiftcoinTestNet(Giftcoin):
    """
    Class with all the necessary Giftcoin testing network information based on
    https://github.com/GiftCoin/giftcoin-release/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-giftcoin'
    seeds = ("node.giftcoin.info",
             "nodegift.poolnetwork.org")
    port = 18855
