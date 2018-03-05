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
    )
    port = 24241
    message_start = b'\xf1\xe0\xa2\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 97,
        'SCRIPT_ADDR': 38,
        'SECRET_KEY': 225
    }
