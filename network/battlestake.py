from clove.network.bitcoin import Bitcoin


class BattleStake(Bitcoin):
    """
    Class with all the necessary BattleStake network information based on
    https://github.com/battlestake/source/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'BattleStake'
    symbols = ('BSTK', )
    seeds = ("seed.battlestake.xyz")
    port = 9542
    message_start = b'\xfb\xc2\xba\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
