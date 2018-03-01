from clove.network.bitcoin import Bitcoin


class PACcoin(Bitcoin):
    """
    Class with all the necessary PACcoin network information based on
    https://github.com/paccoincommunity/paccoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'paccoin'
    symbols = ('PAC', )
    seeds = ('pacifica-nation.com')
    port = 8112
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 24,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 152
    }


# Has no testnet
