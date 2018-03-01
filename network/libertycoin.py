from clove.network.bitcoin import Bitcoin


class Libertycoin(Bitcoin):
    """
    Class with all the necessary Libertycoin network information based on
    https://github.com/libertydev/libertycoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'libertycoin'
    symbols = ('XLB', )
    nodes = ("23.94.38.173",
             "192.241.247.229",
             "162.243.90.199",
             "106.216.171.76",
             "82.231.48.47",
             "107.170.218.104",
             "203.195.205.72",
             "198.50.242.34",
             "37.187.74.123",
             "192.99.3.15",
             "174.51.17.18",
             "93.103.43.62",
             "192.241.247.229")
    port = 55901
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 176
    }

# no testnet
