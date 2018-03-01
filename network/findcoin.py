from clove.network.bitcoin import Bitcoin


class FindCoin(Bitcoin):
    """
    Class with all the necessary FindCoin network information based on
    https://github.com/SHNICI/Findcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'findcoin'
    symbols = ('FIND', )
    seeds = ("178.63.51.87")
    port = 55097
    message_start = b'\xc4\x4b\xb1\xb9'
    base58_prefixes = {
        'PUBKEY_ADDR': 36,
        'SCRIPT_ADDR': 95,
        'SECRET_KEY': 164
    }

# no testnet
