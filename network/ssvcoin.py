from clove.network.bitcoin import Bitcoin


class SSVCoin(Bitcoin):
    """
    Class with all the necessary SSVCoin network information based on
    https://github.com/SSVDevTeam/SSVCoin/blob/master/SSVCoin/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ssvcoin'
    symbols = ('SSV', )
    seeds = ("91.246.70.114")
    port = 9235

# no testnet
