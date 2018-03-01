from clove.network.bitcoin import Bitcoin


class StarCashNetwork(Bitcoin):
    """
    Class with all the necessary StarCash Network (STARS) network information based on
    https://github.com/cybernetik7/StarCash-Network-2.0/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'starcashnetwork'
    symbols = ('STARS', )
    seeds = ('45.32.226.114')
    port = 21698
    message_start = b'\xf1\xca\xba\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 125,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 253
    }

# no testnet
