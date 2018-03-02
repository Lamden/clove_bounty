from clove.network.bitcoin import Bitcoin


class Virtacoin(Bitcoin):
    """
    Class with all the necessary Virtacoin (VTA) network information based on
    https://github.com/virtacoin/VirtaCoinProject/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'virtacoin'
    symbols = ('VTA', )
    seeds = ('seed1.virtacoin.com', 'seed2.virtacoin.com', )
    port = 22816
    message_start = b'\xbe\xd0\xc8\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }

# no testnet
