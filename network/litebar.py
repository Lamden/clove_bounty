from clove.network.bitcoin import Bitcoin


class Litebar(Bitcoin):
    """
    Class with all the necessary LTB network information based on
    https://github.com/crypto-currency/litebar/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'litebar'
    symbols = ('LTB', )
    seeds = (
        'litebar.co',
    )
    port = 9065


class LitebarTestNet(Litebar):
    """
    Class with all the necessary LTB testing network information based on
    https://github.com/crypto-currency/litebar/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-litebar'
    seeds = ()
    port = 19065
