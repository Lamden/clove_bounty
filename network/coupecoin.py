from clove.network.bitcoin import Bitcoin


class Coupecoin(Bitcoin):
    """
    Class with all the necessary Coupecoin network information based on
    https://github.com/CoupecoinOriginal/coupecoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'coupecoin'
    symbols = ('COUPE', )
    seeds = ("electrum5.cryptolife.net", )
    port = 17739
    message_start = b'\xb9\xf6\xa2\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 88,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 216
    }
