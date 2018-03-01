from clove.network.bitcoin import Bitcoin


class Phoenixcoin(Bitcoin):
    """
    Class with all the necessary Phoenixcoin network information based on
    https://github.com/ghostlander/phoenixcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'phoenixcoin'
    symbols = ('PXC', )
    seeds = ('seed0.phoenixcoin.org',
             'seed1.phoenixcoin.org', 'seed2.phoenixcoin.org')
    port = 9555
    message_start = b'\xfe\xd0\xd8\xc3'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 184
    }


# Has no testnet
