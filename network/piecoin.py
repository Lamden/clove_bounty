from clove.network.bitcoin import Bitcoin


class PIECoin(Bitcoin):
    """
    Class with all the necessary PIECoin (PIE) network information based on
    https://github.com/flintsoft/PIE/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'piecoin'
    symbols = ('PIE', )
    seeds = ('195.74.52.227', '107.170.196.135', '149.56.154.75', '82.165.162.27',
             '81.89.100.38', '149.56.154.75', '62.138.3.214')
    port = 31415
    message_start = b'\x2a\x7c\xcb\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 72,
        'SECRET_KEY': 142
    }

# no testnet
