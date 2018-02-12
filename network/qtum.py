from clove.network.bitcoin import Bitcoin


class Qtum(Bitcoin):
    """
    Class with all the necessary QTUM network information based on
    https://github.com/qtumproject/qtum/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'qtum'
    symbols = ('QTUM', )
    seeds = (
        'qtum3.dynu.net',
    )
    port = 3888


class QtumTestNet(Qtum):
    """
    Class with all the necessary QTUM testing network information based on
    https://github.com/qtumproject/qtum/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-qtum'
    seeds = (
        'qtum4.dynu.net',
    )
    port = 13888
