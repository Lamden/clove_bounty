from clove.network.bitcoin import Bitcoin


class HempCoin(Bitcoin):
    """
    Class with all the necessary HempCoin network information based on
    https://github.com/hempcoin-project/THC/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'hempcoin'
    symbols = ('THC', )
    seeds = ("162.243.1.45")
    port = 21054
    message_start = b'\xa5\xa5\xfd\x01'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 168
    }

# no testnet
