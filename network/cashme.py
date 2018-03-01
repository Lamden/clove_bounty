from clove.network.bitcoin import Bitcoin


class Cashme(Bitcoin):
    """
    Class with all the necessary Cashme network information based on
    https://github.com/stewpak/CashMe/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'cashme'
    symbols = ('CME', )
    nodes = ("64.90.187.238",
             "89.204.139.80",
             "136.243.50.159",
             "60.241.118.21",
             "93.157.25.130",
             "151.226.171.116",
             "95.215.45.81",
             "89.204.137.131",
             "85.25.214.214",
             "75.130.163.51",
             "92.46.21.75",
             "80.229.27.64",)
    port = 13370
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }
