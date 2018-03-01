from clove.network.bitcoin import Bitcoin


class PeopleCoin(Bitcoin):
    """
    Class with all the necessary PeopleCoin network information based on
    https://github.com/peopleproject/people/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'peoplecoin'
    symbols = ('MEN', )
    seeds = ("seed.peoplecoin.pw")
    port = 7721
    message_start = b'\x4D\x45\x4E\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }

# no testnet
