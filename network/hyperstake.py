from clove.network.bitcoin import Bitcoin


class HyperStake(Bitcoin):
    """
    Class with all the necessary HyperStake network information based on
   https://github.com/hyperstake/hyperstake/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'hyperstake'
    symbols = ('HYP', )
    seeds = ('hyp.seed.fuzzbawls.pw', 'hypseed.presstab.pw')
    port = 18775
    message_start = b'\xdb\xad\xbd\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 117,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 245
    }


# Has no Testnet
