from clove.network.bitcoin import Bitcoin


class SJWCoin(Bitcoin):
    """
    Class with all the necessary SJWCoin network information based on
    https://github.com/sjwcoin/sjwcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sjwcoin'
    symbols = ('SJW', )
    seeds = ("seed.sjwcoin.com")
    port = 19966
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 95,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 223
    }

# no testnet
