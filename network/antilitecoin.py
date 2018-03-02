from clove.network.bitcoin import Bitcoin


class Antilitecoin(Bitcoin):
    """
    Class with all the necessary Antilitecoin (ALTC) network information based on
    https://github.com/cyberpay/coin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'antilitecoin'
    symbols = ('ALTC', )
    nodes = ('192.52.166.80', )
    port = 8795
    message_start = b'\xc1\xd1\xd2\xad'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 143
    }


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
    message_start = b'\xd2\xb1\xa1\xac'
    base58_prefixes = {
        'PUBKEY_ADDR': 119,
        'SCRIPT_ADDR': 199,
        'SECRET_KEY': 247
    }
