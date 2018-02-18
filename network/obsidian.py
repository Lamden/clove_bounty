from clove.network.bitcoin import Bitcoin


class Obsidian(Bitcoin):
    """
    Class with all the necessary Obsidian (ODN) network information based on
    https://github.com/obsidianproject/Obsidian-Qt/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'obsidian'
    symbols = ('ODN', )
    seeds = ('obsidianblockchain1.westeurope.cloudapp.azure.com',
			 'obsidianblockchain2.westeurope.cloudapp.azure.com',
			 'obsidianseednode1.westeurope.cloudapp.azure.com',
			 'seed1.obsidianplatform.com',
			 'seed2.obsidianplatform.com')
    port = 56660

# no testnet
