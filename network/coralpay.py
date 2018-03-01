from clove.network.bitcoin import Bitcoin


class CoralPay(Bitcoin):
    """
    Class with all the necessary CoralPay network information based on
    https://github.com/coralpay/coral/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'coralpay'
    symbols = ('CORAL', )
    seeds = ("35.163.164.145")
    port = 60093
    message_start = b'\xc4\x4b\xb1\xb9'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 95,
        'SECRET_KEY': 168
    }

# Has no testnet
