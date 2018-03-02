from clove.network.bitcoin import Bitcoin


class HappyCreatorCoin(Bitcoin):
    """
    Class with all the necessary Happy Creator Coin network information based on
    https://github.com/creath/hcc/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'happy_creator_coin'
    symbols = ('HCC', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net")
    port = 11176
    message_start = b'\xfc\xcc\xba\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 41,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 169
    }
