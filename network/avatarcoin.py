from clove.network.bitcoin import Bitcoin


class AvatarCoin(Bitcoin):
    """
    Class with all the necessary AvatarCoin network information based on
    https://github.com/avatarcoin/avatarcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'AvatarCoin'
    symbols = ('AV', )
    seeds = ('avatar.altnodes.xyz', 'avatar2.altnodes.xyz', )
    port = 9712
    message_start = b'\xb2\x3b\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 41,
        'SECRET_KEY': 151
    }


# Has no Testnet
