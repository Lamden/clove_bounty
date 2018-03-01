from clove.network.bitcoin import Bitcoin


class Scorecoin(Bitcoin):
    """
    Class with all the necessary Scorecoin network information based on
    https://github.com/marksteven2017/Scorecoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'scorecoin'
    symbols = ('SCORE', )
    seeds = ("scorecoin.net", )
    port = 17075
    message_start = b'\xac\xcd\xdf\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
