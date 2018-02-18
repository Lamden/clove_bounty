from clove.network.bitcoin import Bitcoin


class DigitalCredits(Bitcoin):
    """
    Class with all the necessary Digital Credits (DGCS) network information based on
    https://github.com/intristin/digitalcredits/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'digitalcredits'
    symbols = ('DGCS', )
    seeds = ('seeder.digitalcredits.xyz', 'seeder2.digitalcredits.xyz')
    port = 7183

# no testnet
