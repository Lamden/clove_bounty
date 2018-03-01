from clove.network.bitcoin import Bitcoin


class Dimecoin(Bitcoin):
    """
    Class with all the necessary Dimecoin (DIME) network information based on
    https://github.com/dime-coin/dimecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'dimecoin'
    symbols = ('DIME', )
    seeds = ('217.175.119.125', '184.164.129.202', '200.123.47.184',
             '13.81.2.56', '189.27.221.173', '45.116.233.61', '200.123.47.184')
    port = 11931

# no testnet
