from clove.network.bitcoin import Bitcoin


class PosEx(Bitcoin):
    """
    Class with all the necessary PosEx network information based on
    https://github.com/posex/posex/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'posex'
    symbols = ('PEX', )
    seeds = ("52.88.141.55",
             "178.20.139.146",
             "91.234.78.95",
             "82.20.209.59",
             "93.84.161.216",
             "94.241.197.182",
             "79.69.39.40",
             "216.189.153.5",
             "80.245.114.235",
             "82.169.211.185",
             "82.66.55.40",
             "83.149.47.98",
             "84.202.234.186",
             "89.161.82.50",
             "92.148.37.69",
             "92.223.185.250",
             "93.38.64.252",
             "94.213.50.182",
             "94.241.221.220",
             "94.241.232.129",
             "95.78.36.119")
    port = 9911

# Has no testnet
