from clove.network.bitcoin import Bitcoin


class Altcommunitycoin(Bitcoin):
    """
    Class with all the necessary Altcommunitycoin network information based on
    https://github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'Altcommunitycoin'
    symbols = ('ALTCOM', )
    seeds = ('109.230.231.216', '109.230.231.221',
             '212.109.218.47', 'zPools.de')
    port = 29855


# Has no Testnet
