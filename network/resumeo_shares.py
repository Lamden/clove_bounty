from clove.network.bitcoin import Bitcoin


class ResumeoShares(Bitcoin):
    """
    Class with all the necessary Resumeo Shares network information based on
    https://github.com/vanyabios/resumeo/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'resumeo_shares'
    symbols = ('RMS', )
    nodes = ("107.170.189.185",
             "79.135.200.66")
    port = 38891
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 122,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 250
    }
