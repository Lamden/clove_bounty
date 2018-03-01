from clove.network.bitcoin import Bitcoin


class Mergecoin(Bitcoin):
    """
    Class with all the necessary Mergecoin (MGC) network information based on
    https://github.com/mergecoin-project/Mergecoin-master/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'mergecoin'
    symbols = ('MGC', )
    seeds = ('47.89.43.73', '43.241.232.45', '47.89.178.249', '120.55.82.131', '121.41.19.30', '120.26.231.61',
             '47.94.89.212', 'mergechain.com', 'mergecoin.com')
    port = 17700

# no testnet
