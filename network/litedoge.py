from clove.network.bitcoin import Bitcoin


class LiteDoge(Bitcoin):
    """
    Class with all the necessary LiteDoge network information based on
    https://github.com/vashshawn/LDOGE/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'litedoge'
    symbols = ('LDOGE', )
    nodes = ("46.4.37.190",
             "134.255.218.110",
             "213.133.99.84",
             "66.214.14.254",
             "73.120.71.189",
             "108.21.75.150",
             "71.197.143.70",
             "188.153.14.20")
    port = 17014
    message_start = b'\x65\x44\x15\x06'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 171
    }

# no testnet
