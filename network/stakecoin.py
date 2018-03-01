from clove.network.bitcoin import Bitcoin


class Stakecoin(Bitcoin):
    """
    Class with all the necessary Stakecoin network information based on
    https://github.com/Cinnicoin/stakecoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'stakecoin'
    symbols = ('STCN', )
    seeds = ("nodea.stakecoin.co",
             "nodeb.stakecoin.co",
             "nodec.stakecoin.co")
    port = 16814
    message_start = b'\x60\x34\x12\x08'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 171
    }

# no testnet
