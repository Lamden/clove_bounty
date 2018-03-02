from clove.network.bitcoin import Bitcoin


class UltraCoin(Bitcoin):
    """
    Class with all the necessary UltraCoin network information based on
    https://github.com/presstab/ultracoin-2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ultracoin'
    symbols = ('UTC', )
    seeds = ("utcseed.presstab.pw", )
    port = 44100
    message_start = b'\xd9\xe6\xe7\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 6,
        'SECRET_KEY': 196
    }


# Has no testnet
