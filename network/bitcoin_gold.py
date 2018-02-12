from clove.network.bitcoin import Bitcoin


class BitcoinGold(Bitcoin):
    """
    Class with all the necessary BTG network information based on
    https://github.com/BTCGPU/BTCGPU/blob/master/src/chainparams.cpp    
    (date of access: 02/12/2018)
    """
    name = 'bitcoin-gold'
    symbols = ('BTG', )
    seeds = ('eu-dnsseed.bitcoingold-official.org','dnsseed.bitcoingold.org','dnsseed.btcgpu.org')
    port = 8338


class BitcoinGoldTestNet(BitcoinGold):
    """
    Class with all the necessary BTG testing network information based on
    https://github.com/BTCGPU/BTCGPU/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-bitcoin-gold'
    seeds = ('eu-test-dnsseed.bitcoingold-official.org','test-dnsseed.bitcoingold.org','test-dnsseed.btcgpu.org','btg.dnsseed.minertopia.org')
    port = 18338
