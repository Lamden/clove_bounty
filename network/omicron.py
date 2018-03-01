from clove.network.bitcoin import Bitcoin


class Omicron(Bitcoin):
    """
    Class with all the necessary Omicron network information based on
    https://www.github.com/gladimor/omicron-investment-platform/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'omicron'
    symbols = ('OMC', )
    seeds = ('159.203.62.235')
    port = 8519
    message_start = b'\xf2\x40\xeb\xb3'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 143
    }


# Has no Testnet
