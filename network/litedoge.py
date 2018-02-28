from clove.network.bitcoin import Bitcoin


class LiteDoge(Bitcoin):
    """
    Class with all the necessary LiteDoge network information based on
    https://github.com/vashshawn/LDOGE/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'litedoge'
    symbols = ('LDOGE', )
    seeds = ("46.4.37.190",
             "134.255.218.110",
             "213.133.99.84",
             "66.214.14.254",
             "73.120.71.189",
             "108.21.75.150",
             "71.197.143.70",
             "188.153.14.20")
    port = 17014

# no testnet
