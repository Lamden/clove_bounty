from clove.network.bitcoin import Bitcoin


class BitBar(Bitcoin):
    """
    Class with all the necessary BitBar network information based on
    https://github.com/bitbarcoin/bitbar/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'BitBar'
    symbols = ('BTB', )
    seeds = ('btb.altcointech.net', )
    port = 8777
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 153
    }
