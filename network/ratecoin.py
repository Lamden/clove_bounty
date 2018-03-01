from clove.network.bitcoin import Bitcoin


class Ratecoin(Bitcoin):
    """
    Class with all the necessary Ratecoin network information based on
    https://github.com/ratecoinxra/ratecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ratecoin'
    symbols = ('XRA', )
    seeds = ("xraseed1.presstab.pw",
             "xraseed2.presstab.pw",
             "xraseed3.presstab.pw",
             "104.238.137.2",
             "185.92.222.152")
    port = 35851
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 188
    }


# Has no testnet
