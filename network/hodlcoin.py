from clove.network.bitcoin import Bitcoin


class HOdlcoin(Bitcoin):
    """
    Class with all the necessary HOdlcoin network information based on
    https://github.com/HOdlcoin/HOdlcoin/blob/HODLCoin0.11.3/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'hodlcoin'
    symbols = ('HODL', )
    seeds = ("westcoast.hodlcoin.com",
             "eastcoast.hodlcoin.com",
             "europe.hodlcoin.com",
             "asia.hodlcoin.com",
             "seed.hodlcoin.oo.fi",
             "seed.hodlcoin.dk",
             "seed.hodlcoin.com")
    port = 1989
    message_start = b'\xf9\xbc\xb5\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 168
    }

# no testnet
