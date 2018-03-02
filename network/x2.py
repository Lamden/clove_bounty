from clove.network.bitcoin import Bitcoin


class X2(Bitcoin):
    """
    Class with all the necessary X2 network information based on
    https://github.com/x2team2017/x2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'x2'
    symbols = ('X2', )
    seeds = ("x2team2017.ddns.net", "stratumtest.ddns.net")
    port = 16384
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }


# Has no test
