from clove.network.bitcoin import Bitcoin


class Bones(Bitcoin):
    """
    Class with all the necessary Bones network information based on
    https://github.com/BonesCoin/Bones/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'Bones'
    symbols = ('BONES', )
    seeds = ("seed.Bones.com", )
    port = 55355
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 153
    }


# Has no testnet
