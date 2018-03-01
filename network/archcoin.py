from clove.network.bitcoin import Bitcoin


class ARCHcoin(Bitcoin):
    """
    Class with all the necessary ARCHcoin network information based on
    https://github.com/EdgarSoares/ARCH/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'archcoin'
    symbols = ('ARCH', )
    seeds = ("supernode.archcoin.co")
    port = 8998

# Has no testnet
