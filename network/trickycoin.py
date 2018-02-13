from clove.network.bitcoin import Bitcoin


class TrickyCoin(Bitcoin):
    """
    Class with all the necessary TrickyCoin network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'trickycoin'
    symbols = ('TRICK', )
    seeds = ("52.11.105.205")
    port = 13414


# Has no testnet