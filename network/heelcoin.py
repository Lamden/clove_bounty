from clove.network.bitcoin import Bitcoin


class HeelCoin(Bitcoin):
    """
    Class with all the necessary HeelCoin network information based on
    https://github.com/HeelCoin/heelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'heelcoin'
    symbols = ('HEEL', )
    seeds = ("52.10.89.163")
    port = 22077

# no testnet
