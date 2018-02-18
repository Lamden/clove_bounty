from clove.network.bitcoin import Bitcoin


class FedoraCoin(Bitcoin):
    """
    Class with all the necessary FedoraCoin (TIPS) network information based on
    https://github.com/fedoracoin-dev/fedoracoin/blob/master-0.9/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'fedoracoin'
    symbols = ('TIPS', )
    seeds = ('seed.fedoracoin.net', '45.55.250.196', 'tips1.netcraft.ch' , 'tips2.netcraft.ch')
    port = 44890


class FedoraCoinTestNet(FedoraCoin):
    """
    Class with all the necessary FedoraCoin (TIPS) testing network information based on
    https://github.com/fedoracoin-dev/fedoracoin/blob/master-0.9/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-fedoracoin'
    seeds = ('115.29.37.248', 'testnet-dnsseed.fedoracoin.com')
    port = 19336
