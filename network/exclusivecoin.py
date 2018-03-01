from clove.network.bitcoin import Bitcoin


class ExclusiveCoin(Bitcoin):
    """
    Class with all the necessary ExclusiveCoin (EXCL) network information based on
    https://github.com/exclfork/ExclusiveCoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'exclusivecoin'
    symbols = ('EXCL', )
    seeds = ('nodes.exclusivecoin.pw')
    port = 23230
    message_start = b'\xa2\x3d\x2f\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 137,
        'SECRET_KEY': 161
    }

# no testnet
