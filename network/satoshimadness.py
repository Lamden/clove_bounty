from clove.network.bitcoin import Bitcoin


class SatoshiMadness(Bitcoin):
    """
    Class with all the necessary SatoshiMadness network information based on
    https://github.com/playpossat/blocksattime/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'SatoshiMadness'
    symbols = ('MAD', )
    seeds = ("52.27.159.176")
    port = 5444


# Has no testnet
