from clove.network.bitcoin import Bitcoin


class GrowersIntl(Bitcoin):
    """
    Class with all the necessary Growers International (GRWI) network information based on
    https://github.com/growersintl/growers/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'growersintl'
    symbols = ('GRWI', )
    seeds = ('45.55.4.192', '104.236.78.83', '104.236.120.44')
    port = 11667
    message_start = b'\x28\x44\x15\x06'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 132,
        'SECRET_KEY': 171
    }

# no testnet
