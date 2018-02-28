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

# Has no testnet
