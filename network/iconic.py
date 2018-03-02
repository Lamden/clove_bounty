from clove.network.bitcoin import Bitcoin


class Iconic(Bitcoin):
    """
    Class with all the necessary Iconic network information based on
    https://www.github.com/iconictoken/iconic/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'iconic'
    symbols = ('ICON', )
    seeds = ('node.iconicproject.com', 'iconicproject.com', )
    port = 47426
    message_start = b'\xa3\xa5\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 230
    }


# Has no Testnet
