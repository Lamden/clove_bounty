from clove.network.bitcoin import Bitcoin


class IgnitionCoin(Bitcoin):
    """
    Class with all the necessary Ignition Coin (IC) network information based on
    https://github.com/ignitioncoin/ignitioncoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'ignitioncoin'
    symbols = ('IC', )
    seeds = ('america.ignitioncoin.org', 'europ.ignitioncoin.org',
             'asia.ignitioncoin.org', 'explorer.ignitioncoin.org')
    port = 44144
    message_start = b'\x5f\x79\x64\xc9'
    base58_prefixes = {
        'PUBKEY_ADDR': 103,
        'SCRIPT_ADDR': 39,
        'SECRET_KEY': 138
    }

# no testnet
