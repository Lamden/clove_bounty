from clove.network.bitcoin import Bitcoin


class BitSoar(Bitcoin):
    """
    Class with all the necessary BitSoar (BSR) network information based on
    https://github.com/BITSOAR/wallet/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'bitsoar'
    symbols = ('BSR', )
    seeds = ('139.59.7.111', '138.197.156.193')
    port = 40119

# no testnet
