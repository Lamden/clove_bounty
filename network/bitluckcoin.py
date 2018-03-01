from clove.network.bitcoin import Bitcoin


class BitLuckCoin(Bitcoin):
    """
    Class with all the necessary BitLuckCoin network information based on
    https://github.com/bitluckdev/bitluckcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitluckcoin'
    symbols = ('BTLC', )
    seeds = ("45.32.35.123", "45.76.96.149")
    port = 24289
    message_start = b'\xb4\xfc\xc8\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 38,
        'SECRET_KEY': 153
    }

# Has no testnet
