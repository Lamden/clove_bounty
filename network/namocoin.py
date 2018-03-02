from clove.network.bitcoin import Bitcoin


class NamoCoin(Bitcoin):
    """
    Class with all the necessary NamoCoin network information based on
    https://github.com/namocoin/namocoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'namocoin'
    symbols = ('NAMO', )
    seeds = ('namo.ddns.me', )
    port = 16305
    message_start = b'\xa1\xb3\xc7\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 52,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 180
    }


# Has no testnet
