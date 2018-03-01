from clove.network.bitcoin import Bitcoin


class CleverHash(Bitcoin):
    """
    Class with all the necessary CleverHash network information based on
    https://github.com/Cleverhash/CHASH/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cleverhash'
    symbols = ('CHASH', )
    seeds = ("104.131.197.190", "104.236.15.167")
    port = 28194
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 168
    }

# Has no testnet
