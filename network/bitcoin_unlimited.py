from clove.network.bitcoin import Bitcoin


class Bitcoin_Unlimited(Bitcoin):
    """
    Class with all the necessary Bitcoin Unlimited network information based on
    https://github.com/BitcoinUnlimited/BitcoinUnlimited/blob/release/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'bitcoin_unlimited'
    symbols = ('BCU', )
    seeds = ("btccash-seeder.bitcoinunlimited.info",
             "seed.bitcoinabc.org",
             "seed-abc.bitcoinforks.org",
             "seed.bitprim.org", 
             "seed.deadalnix.me")
    port = 8333 
	
   
class Bitcoin_UnlimitedTestNet(Bitcoin_Unlimited):
    """
    Class with all the necessary Bitcoin Unlimited testing network information based on
    https://github.com/BitcoinUnlimited/BitcoinUnlimited/blob/release/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-bitcoin_unlimited'
    seeds = ("nolnet-seed.bitcoinunlimited.info")
    port = 18333              
