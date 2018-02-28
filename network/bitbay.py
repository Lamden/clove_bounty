from clove.network.bitcoin import Bitcoin


class BitBay(Bitcoin):
    """
    Class with all the necessary BitBay network information based on
    https://github.com/bitbayteam/bitbay/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitbay'
    symbols = ('BAY', )
    seeds = ("178.62.201.53", "128.199.251.218")
    port = 19914

# Has no testnet
