from clove.network.bitcoin import Bitcoin


class Milllionaire_Coin(Bitcoin):
    """
    Class with all the necessary Milllionaire Coin network information based on
    https://github.com/MILcoindev/Milliionaire-Coin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'milllionaire_coin'
    symbols = ('MIL', )
    seeds = ("108.61.198.32")
    port = 35552
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 178
    }

# no testnet
