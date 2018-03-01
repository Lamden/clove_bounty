from clove.network.bitcoin import Bitcoin


class BitBar(Bitcoin):
    """
    Class with all the necessary BitBar network information based on
    https://github.com/bitbarcoin/bitbar/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'BitBar'
    symbols = ('BTB', )
    seeds = ('btb.altcointech.net')
    port = 8777
