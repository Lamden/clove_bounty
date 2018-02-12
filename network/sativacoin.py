from clove.network.bitcoin import Bitcoin


class Sativacoin(Bitcoin):
    """
    Class with all the necessary Sativacoin network information based on
    https://github.com/newsativacoindev/sativacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Sativacoin'
    symbols = ('STV', )
    seeds = ("0.stv.bitnodes.net","1.stv.bitnodes.net","2.stv.bitnodes.net")
    port = 60990


# Has no testnet

