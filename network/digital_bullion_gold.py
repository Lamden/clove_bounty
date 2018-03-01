from clove.network.bitcoin import Bitcoin


class DigitalBullionGold(Bitcoin):
    """
    Class with all the necessary Digital Bullion Gold network information based on
    https://github.com/dbgold/dbgold/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'digitalbulliongold'
    symbols = ('DBG', )
    nodes = ('178.62.122.246', )
    port = 32113
    message_start = b'\x04\xa1\xb1\xb5'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 159
    }

# No testnet
