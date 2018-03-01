from clove.network.bitcoin import Bitcoin


class PX(Bitcoin):
    """
    Class with all the necessary PX network information based on
    https://www.github.com/igotspots/px/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'px'
    symbols = ('PX', )
    seeds = ('PX.freestaking.com')
    port = 9232


# Has no testnet
