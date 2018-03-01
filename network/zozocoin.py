from clove.network.bitcoin import Bitcoin


class ZoZoCoin(Bitcoin):
    """
    Class with all the necessary ZoZoCoin (ZZC) network information based on
    https://github.com/ZoZoCoin/ZoZo-blockchain/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'zozocoin'
    symbols = ('ZZC', )
    seeds = (
        'seed_chainbytes1.chickenkiller.com', 'seed_chainbytes2.chickenkiller.com',
        'seed_chainbytes3.chickenkiller.com', 'seed_chainbytes4.chickenkiller.com',
        'seed_chainbytes5.chickenkiller.com'
    )
    port = 19995
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 76,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 204
    }

# no testnet
