from clove.network.bitcoin import Bitcoin


class SweetStake(Bitcoin):
    """
    Class with all the necessary SweetStake network information based on
    https://github.com/SweetStake/SweetStake/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sweetstake'
    symbols = ('SWEET', )
    seeds = ("sweetstake.endofinternet.net", )
    port = 34613
    message_start = b'\xaa\xa2\xb2\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 191
    }

# no testnet
