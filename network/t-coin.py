from clove.network.bitcoin import Bitcoin


class TCoin(Bitcoin):
    """
    Class with all the necessary T-coin network information based on
    https://github.com/tcoindev/t-coin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 't-coin'
    symbols = ('TCOIN', )
    seeds = ("175.124.227.229",
             "175.124.227.230")
    port = 25286
    message_start = b'\xb4\xfc\xc8\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 38,
        'SECRET_KEY': 193
    }
