from clove.network.bitcoin import Bitcoin


class NobleCoin(Bitcoin):
    """
    Class with all the necessary NobleCoin network information based on
    https://github.com/noblecoinnobl/noblecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'noblecoin'
    symbols = ('NOBL', )
    seeds = ('nobl.poolerino.com')
    port = 55884


# Has no testnet
