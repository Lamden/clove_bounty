from clove.network.bitcoin import Bitcoin


class TeamUp(Bitcoin):
    """
    Class with all the necessary TeamUp network information based on
    https://github.com/teamupdev/teamup/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'teamup'
    symbols = ('TEAM', )
    nodes = ("185.106.122.32", )
    port = 37091
    message_start = b'\x5a\x3c\xa4\xb2'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 193
    }


# Has no testnet
