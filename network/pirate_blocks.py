from clove.network.bitcoin import Bitcoin


class PirateBlocks(Bitcoin):
    """
    Class with all the necessary Pirate Blocks (SKULL) network information based on
    https://github.com/pirateblocks/PBlocks/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'pirateblocks'
    symbols = ('SKULL', )
    seeds = ('pblocks.servep2p.com')
    port = 27991

# no testnet
