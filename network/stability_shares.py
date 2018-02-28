from clove.network.bitcoin import Bitcoin


class Stability_Shares(Bitcoin):
    """
    Class with all the necessary Stability Shares network information based on
    https://bitcointalk.org/index.php?topic=490529.0
    (date of access: 02/16/2018)
    """
    name = 'stability_shares'
    symbols = ('XSS', )
    seeds = ("80.112.144.84",
             "82.139.127.205",
             "23.253.82.83",
             "27.33.1.58",
             "87.147.43.53",
             "174.108.122.202",
             "204.195.130.236",
             "92.55.41.212",
             "88.127.170.75",
             "94.23.196.92")
    port = 7711

# no testnet
