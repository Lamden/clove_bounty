from clove.network.bitcoin import Bitcoin


class Halcyon(Bitcoin):
    """
    Class with all the necessary Halcyon network information based on
    https://github.com/ghostlander/halcyon/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'halcyon'
    symbols = ('HAL', )
    seeds = ('seed0.phoenixcoin.org', 'seed1.phoenixcoin.org')
    port = 21108
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 168
    }


# Has no testnet
