from clove.network.bitcoin import Bitcoin


class Twistercoin(Bitcoin):
    """
    Class with all the necessary Twistercoin network information based on
    https://github.com/miningfool/twistercoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'twistercoin'
    symbols = ('TWIST', )
    seeds = ("52.10.32.200")
    port = 44258

# no testnet
