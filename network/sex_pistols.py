from clove.network.bitcoin import Bitcoin


class Sex_Pistols(Bitcoin):
    """
    Class with all the necessary Sex Pistols network information based on
    https://github.com/sexpist/sexpistols/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sex_pistols'
    symbols = ('SP', )
    seeds = ("node.walletbuilders.com")
    port = 7515
    message_start = b'\x36\x06\x0c\xc3'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

#  no testnet
