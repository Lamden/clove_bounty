from clove.network.bitcoin import Bitcoin


class EACoin(Bitcoin):
    """
    Class with all the necessary EA Coin (EAG) network information based on
    https://github.com/eacoin-project/eacore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'eacoin'
    symbols = ('EAG', )
    seeds = ('eaglive.co')
    port = 28635

# no testnet
