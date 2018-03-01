from clove.network.bitcoin import Bitcoin


class Gram_Coin(Bitcoin):
    """
    Class with all the necessary Gram Coin network information based on
    https://github.com/kilogram1/kilogram1/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'gram_coin'
    symbols = ('GRAM', )
    seeds = ("node.GramCoin.org",
             "node.GramCoin.cf",
             "GramCoin.no-ip.org")
    port = 7567
    message_start = b'\xc6\xb2\x63\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 224
    }

# no testnet
