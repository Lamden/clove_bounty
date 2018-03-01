from clove.network.bitcoin import Bitcoin


class BitFID(Bitcoin):
    """
    Class with all the necessary BitFID (FID) network information based on
    https://github.com/FidChain/FIDWALLET/blob/master/src/chainparams.cpp
    (date of access: 02/22/2018)
    """
    name = 'bitfid'
    symbols = ('FID', )
    seeds = ('120.55.61.133', '47.92.98.238',
             '39.108.173.85', '39.108.154.111')
    port = 19771

# no testnet
