from clove.network.bitcoin import Bitcoin


class  B3Coin(Bitcoin):
    """
    Class with all the necessary  B3Coin (KB3) network information based on
    https://github.com/B3-Coin/B3-CoinV2/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'b3coin'
    symbols = ('KB3', )
    seeds =  ('seed001.b3nodes.net', 'seed002.b3nodes.net', 'seed003.b3nodes.net', 'seed004.b3nodes.net', 'seed005.b3nodes.net',
              'seed006.b3nodes.net', 'seed007.b3nodes.net', 'seed008.b3nodes.net', 'seed008.b3nodes.net', 'seed010.b3nodes.net',
              'seed011.b3nodes.net', 'seed012.b3nodes.net', 'seed013.b3nodes.net', 'seed014.b3nodes.net', 'seed015.b3nodes.net',
              'seed016.b3nodes.net', 'seed017.b3nodes.net', 'seed018.b3nodes.net', 'seed019.b3nodes.net', 'seed020.b3nodes.net',
              'seed021.b3nodes.net', 'seed022.b3nodes.net', 'seed023.b3nodes.net', 'seed024.b3nodes.net', 'seed025.b3nodes.net')
    port = 5647


class  B3CoinTestNet(B3Coin):
    """
    Class with all the necessary  B3Coin (KB3) network information based on
    https://github.com/B3-Coin/B3-CoinV2/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-b3coin'
    symbols = ('KB3', )
    seeds =  ()
    port = 30420
