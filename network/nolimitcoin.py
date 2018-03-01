from clove.network.bitcoin import Bitcoin


class NoLimitCoin(Bitcoin):
    """
    Class with all the necessary NoLimitCoin network information based on
    https://github.com/NoLimitCoin/Nolimitcoin-Core/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'nolimitcoin'
    symbols = ('NLC2', )
    seeds = ("seed1.nlc2.info",
             "seed2.nlc2.info",
             "seed3.nlc2.info")
    port = 6521
    message_start = b'\xb1\xb6\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 181
    }

# no testnet
