from clove.network.bitcoin import Bitcoin


class TurboCoin(Bitcoin):
    """
    Class with all the necessary TurboCoin (TURBO) network information based on
    https://github.com/TurboCoinProject/TurboCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'turbocoin'
    symbols = ('TURBO', )
    seeds = ('195.181.245.38')
    port = 35282

# no testnet
