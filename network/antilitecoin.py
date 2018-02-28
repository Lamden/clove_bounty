from clove.network.bitcoin import Bitcoin


class Antilitecoin(Bitcoin):
    """
    Class with all the necessary Antilitecoin (ALTC) network information based on
    https://github.com/cyberpay/coin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'antilitecoin'
    symbols = ('ALTC', )
    seeds = ('192.52.166.80')
    port = 8795


class AntilitecoinTestNet(Antilitecoin):
    """
    Class with all the necessary Antilitecoin (ALTC) testing network information based on
    https://github.com/cyberpay/coin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-antilitecoin'
    seeds = ('testnet-seed.antilitecointools.com',
             'testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com')
    port = 18795
