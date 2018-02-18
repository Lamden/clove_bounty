from clove.network.bitcoin import Bitcoin


class HollywoodCoin(Bitcoin):
    """
    Class with all the necessary HollywoodCoin (HWC) network information based on
    https://github.com/Hollywoodcoiin/hollywood_team/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'hollywoodcoin'
    symbols = ('HWC', )
    seeds = ('seed.hollywoodcoin.biz')
    port = 10267

# no testnet
