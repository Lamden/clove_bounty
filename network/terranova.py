from clove.network.bitcoin import Bitcoin


class TerraNova(Bitcoin):
    """
    Class with all the necessary TerraNova network information based on
    https://github.com/TERRAcoin-source/TerraNova-src/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'terranova'
    symbols = ('TER', )
    seeds = ("194.87.96.140")
    port = 14542
    message_start = b'\x32\x5e\x6f\x86'
    base58_prefixes = {
        'PUBKEY_ADDR': 66,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 194
    }

# no testnet
