from clove.network.bitcoin import Bitcoin


class PetroDollar(Bitcoin):
    """
    Class with all the necessary PetroDollar network information based on
    https://github.com/bryceweiner/petrodollar/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'petrodollar'
    symbols = ('p$', )
    seeds = ("162.243.147.115")
    port = 23932

# no testnet
