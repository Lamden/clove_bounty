from clove.network.bitcoin import Bitcoin


class UniversalRoyalCoin(Bitcoin):
    """
    Class with all the necessary Universal Royal Coin (UNRC) network information based on
    https://github.com/replicant17/UNRC-sources/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'universalroyalcoin'
    symbols = ('UNRC', )
    seeds = ('217.61.21.132', 'seed2.unrc.eu', 'seed3.unrc.eu', 'seed4.unrc.eu', 'seed5.unrc.eu')
    port = 24298

# no testnet
