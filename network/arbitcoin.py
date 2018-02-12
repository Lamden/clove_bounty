from clove.network.bitcoin import Bitcoin


class ARbit(Bitcoin):
    """
    Class with all the necessary ARbit network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ARbit'
    symbols ('ARB', )
    seeds = ('162.243.203.211', '178.62.56.172')
    port = 31930

# Has no Testnet