from clove.network.bitcoin import Bitcoin


class BigUp(Bitcoin):
    """
    Class with all the necessary BigUp (BIGUP) network information based on
    https://github.com/BigUps/wallet/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'bigup'
    symbols = ('BIGUP', )
    seeds = ('seed1.bigup.club', )
    port = 61609
    message_start = b'\x2a\x7c\xcb\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 72,
        'SECRET_KEY': 142
    }

# no testnet
