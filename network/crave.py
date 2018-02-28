from clove.network.bitcoin import Bitcoin


class Crave(Bitcoin):
    """
    Class with all the necessary Crave (CRAVE) network information based on
    https://github.com/CooleRRSA/crave/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'crave'
    symbols = ('CRAVE', )
    seeds = ('dns0.mycrave.xyz', 'dns1.mycrave.xyz', 'dns2.mycrave.xyz', 'dns3.mycrave.xyz', 'dns4.mycrave.xyz',
             'dns5.mycrave.xyz', 'dns6.mycrave.xyz', 'dns7.mycrave.xyz', 'dns8.mycrave.xyz', 'dns9.mycrave.xyz')
    port = 30104

# no testnet
