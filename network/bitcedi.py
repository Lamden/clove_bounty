from clove.network.bitcoin import Bitcoin


class Bitcedi(Bitcoin):
    """
    Class with all the necessary Bitcedi (BXC) network information based on
    https://github.com/lulworm/bitcedi/blob/master/src/CryptoNoteConfig.h
    (date of access: 02/17/2018)
    """
    name = 'bitcedi'
    symbols = ('BXC', )
    seeds = ('seed0.bitcedi.org', 'seed1.bitcedi.org', 'seed2.bitcedi.org', )
    port = 55008

# no testnet
