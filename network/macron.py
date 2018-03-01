from clove.network.bitcoin import Bitcoin


class MACRON(Bitcoin):
    """
    Class with all the necessary MACRON network information based on
    https://github.com/macroncoin/macron/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'macron'
    symbols = ('MCRN', )
    seeds = ('192.52.167.209')
    port = 55553


# Has no testnet
