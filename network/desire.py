from clove.network.bitcoin import Bitcoin


class Desire(Bitcoin):
    """
    Class with all the necessary Desire network information based on
    https://github.com/lazyboozer/Desire/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'desire'
    symbols = ('DSR', )
    seeds = ("154.16.7.228",
             "149.56.154.65",
             "154.16.7.190",
             "109.205.244.150",
             "202.5.19.121",
             "35.185.122.226",
             "35.205.214.124",
             "185.236.130.103",
             "185.236.130.112",
             "194.87.92.16",
             "194.87.92.23",
             "5.9.51.209",
             "164.132.18.89",
             "194.67.213.243")
    port = 9919
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 204
    }

# No testnet
