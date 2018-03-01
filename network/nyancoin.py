from clove.network.bitcoin import Bitcoin


class Nyancoin(Bitcoin):
    """
    Class with all the necessary Nyancoin network information based on
    https://github.com/nyancoin-release/nyancoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'Nyancoin'
    symbols = ('NYAN', )
    seeds = ("nyanseed.com")
    port = 33701
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 173
    }

# no testnet
