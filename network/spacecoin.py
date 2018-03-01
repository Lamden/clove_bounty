from clove.network.bitcoin import Bitcoin


class SpaceCoin(Bitcoin):
    """
    Class with all the necessary SpaceCoin network information based on
    https://github.com/midnight-miner/spacecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spacecoin'
    symbols = ('SPACE', )
    seeds = ('seed1.spacecoin.info', 'seed2.spacecoin.info')
    port = 9172


# Has no testnet
