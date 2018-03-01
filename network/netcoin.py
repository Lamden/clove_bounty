from clove.network.bitcoin import Bitcoin


class NetCoin(Bitcoin):
    """
    Class with all the necessary NetCoin network information based on
    https://github.com/netcoinfoundation/netcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'netcoin'
    symbols = ('NET', )
    seeds = ("netseed.presstab.pw")
    port = 11310
    message_start = b'\xfd\xb6\xa5\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 240
    }

# no testnet
