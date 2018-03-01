from clove.network.bitcoin import Bitcoin


class UniversalCurrency(Bitcoin):
    """
    Class with all the necessary Universal Currency (UNIT) network information based on
    https://github.com/unitcurrency/unitcurrency/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'universalcurrency'
    symbols = ('UNIT', )
    seeds = ('104.207.154.199', '103.22.181.2')
    port = 14158
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 183
    }


class UniversalCurrencyTestNet(UniversalCurrency):
    """
    Class with all the necessary Universal Currency (UNIT) testing network information based on
    https://github.com/unitcurrency/unitcurrency/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-universalcurrency'
    seeds = ()
    port = 24158
