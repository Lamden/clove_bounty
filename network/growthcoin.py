from clove.network.bitcoin import Bitcoin


class GrowthCoin(Bitcoin):
    """
    Class with all the necessary GrowthCoin network information based on
    https://github.com/iamunick/growthcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'growthcoin'
    symbols = ('GRW', )
    seeds = ("seed.grw.blockx.info",
             "seed1.grw.acidpool.com")
    port = 17177
    message_start = b'\xa5\xef\xdb\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 166
    }

# no testnet
