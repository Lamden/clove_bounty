from clove.network.bitcoin import Bitcoin


class CybCSec(Bitcoin):
    """
    Class with all the necessary CybCSec network information based on
    https://github.com/cybcsec/cybcsec/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cybcsec'
    symbols = ('XCS', )
    seeds = ("45.32.174.216",
             "45.76.87.39")
    port = 6601

# Has no testnet
