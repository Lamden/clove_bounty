from clove.network.bitcoin import Bitcoin


class  GlassCoin(Bitcoin):
    """
    Class with all the necessary  GlassCoin (GLS) network information based on
    https://github.com/bretskiejr/glasscoin/blob/master/glasscoin/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'glasscoin'
    symbols = ('GLS', )
    seeds =  ('45.63.34.145', '104.238.159.50')
    port = 23835


# no testnet