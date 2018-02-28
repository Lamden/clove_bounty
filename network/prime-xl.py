from clove.network.bitcoin import Bitcoin


class PrimeXI(Bitcoin):
    """
    Class with all the necessary Prime-XI network information based on
    https://github.com/Prime-Cryptos/Prime-xi/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'prime-xi'
    symbols = ('PXI', )
    nodes = ('138.197.144.217',
             '162.243.151.67',
             '192.241.184.85',
             '188.226.248.45',
             '128.199.165.180')
    port = 11110

# no testnet
