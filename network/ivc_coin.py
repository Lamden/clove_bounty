from clove.network.bitcoin import Bitcoin


class IVC_Coin(Bitcoin):
    """
    Class with all the necessary IVC_Coin network information based on
    https://github.com/invictus2082/invictus/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'ivc_Coin'
    symbols = ('IVC', )
    seeds = ("wallet.cryptolife.net",
             "explore.cryptolife.net",
             "seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "45.77.7.67")
    port = 41184

# no testnet
