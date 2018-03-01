from clove.network.bitcoin import Bitcoin


class DarkTron(Bitcoin):
    """
    Class with all the necessary DarkTron network information based on
    https://github.com/DarkTronDev/DarkTron/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'darktron'
    symbols = ('DRKT', )
    seeds = ("178.62.222.55")
    port = 31454

# has no testnet
