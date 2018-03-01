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
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class LitebarTestNet(Litebar):
    """
    Class with all the necessary LTB testing network information based on
    https://github.com/crypto-currency/litebar/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-litebar'
    seeds = ()
    port = 19065
