from clove.network.bitcoin import Bitcoin


class DutchCoin(Bitcoin):
    """
    Class with all the necessary Dutch Coin (DUTCH) network information based on
    https://github.com/devdutch/dutch/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'dutchcoin'
    symbols = ('DUTCH', )
    seeds = ('198.136.28.100')
    port = 20717
    message_start = b'\x57\xbe\xfd\xa9'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 158
    }

# no testnet
