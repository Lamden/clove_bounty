from clove.network.bitcoin import Bitcoin


class Gaycoin(Bitcoin):
    """
    Class with all the necessary GAY network information based on
    https://github.com/gaycoins/gaycoin-online/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'gaycoin'
    symbols = ('GAY', )
    seeds = (
        'seed01.gay.money',
        'seed02.gay.money',
        'seed03.gay.money',
        'seed04.gay.money',
        'seed05.gay.money',
        'seed06.gay.money',
        'seed07.gay.money',
        'seed08.gay.money',
        'seed09.gay.money',
        '91.121.67.93',
        '138.68.237.158',
        '91.109.38.231',
    )
    port = 24241


class GaycoinTestNet(Gaycoin):
    """
    Class with all the necessary GAY testing network information based on
    https://github.com/gaycoins/gaycoin-online/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-gaycoin'
    seeds = ()
    port = 33542
