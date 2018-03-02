from clove.network.bitcoin import Bitcoin


class Mergecoin(Bitcoin):
    """
    Class with all the necessary Mergecoin (MGC) network information based on
    https://github.com/mergecoin-project/Mergecoin-master/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'mergecoin'
    symbols = ('MGC', )
    seeds = ('mergechain.com', 'mergecoin.com')
    port = 17700
    message_start = b'\xc8\xe1\xd5\xec'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }

# no testnet
