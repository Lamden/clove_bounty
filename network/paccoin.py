from clove.network.bitcoin import Bitcoin


class PACcoin(Bitcoin):
    """
    Class with all the necessary PACcoin network information based on
    https://github.com/paccoincommunity/paccoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'paccoin'
    symbols = ('PAC', )
    seeds = ('pacifica-nation.com')
    port = 8112


# Has no testnet
