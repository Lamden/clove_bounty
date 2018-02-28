from clove.network.bitcoin import Bitcoin


class SpaceCash(Bitcoin):
    """
    Class with all the necessary SpaceCash network information based on
    https://github.com/SpaceCash/SpaceCash/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'spacecash'
    symbols = ('SCASH', )
    seeds = ("185.61.151.109",
             "94.177.229.242",
             "stratumtest.ddns.net")
    port = 55554

# no testnet
