from clove.network.bitcoin import Bitcoin


class DROXNE(Bitcoin):
    """
    Class with all the necessary DROXNE network information based on
    https://github.com/droxdev/drox/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'droxne'
    symbols = ('DRXNE', )
    nodes = ("198.199.90.93", "45.55.89.248", )
    port = 41241
    message_start = b'\xb4\xfe\xe4\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 159
    }


# No Testnet
