from clove.network.bitcoin import Bitcoin


class Paypeer(Bitcoin):
    """
    Class with all the necessary PAYP network information based on
    https://github.com/paypeer/paypeer/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'paypeer'
    symbols = ('PAYP', )
    seeds = (
        'seed1.paypeer.co',
        'seed2.paypeer.co',
        'seed3.paypeer.co',
        'seed4.paypeer.co',
        'ok1.altcoinsfoundation.com',
    )
    port = 33714


class PaypeerTestNet(Paypeer):
    """
    Class with all the necessary PAYP testing network information based on
    https://github.com/paypeer/paypeer/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-paypeer'
    seeds = ()
    port = 33715
