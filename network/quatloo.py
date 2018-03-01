from clove.network.bitcoin import Bitcoin


class Quatloo(Bitcoin):
    """
    Class with all the necessary Quatloo network information based on
    https://github.com/quatloos/quatloo/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'quatloo'
    symbols = ('PHO', )
    seeds = ("seeder.quatloos.org", "dnsseed.quatloos.org",
             "dns-seed.quatloos.org")
    port = 17012
    message_start = b'\xfa\xce\xbe\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 186
    }


class QuatlooTestNet(Quatloo):
    """
    Class with all the necessary Quatloo testing network information based on
    https://github.com/quatloos/quatloo/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-quatloo'
    seeds = ("testnet-seed.quatloos.org")
    port = 17912
