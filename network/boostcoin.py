from clove.network.bitcoin import Bitcoin


class BoostCoin(Bitcoin):
    """
    Class with all the necessary BoostCoin network information based on
    https://github.com/mammix2/boostcoin-core/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'boostcoin'
    symbols = ('BOST', )
    seeds = ("node1.bost.link",
             "node2.bost.link",
             "node3.bost.link",
             "node4.bost.link",
             "node5.bost.link",
             "node6.bost.link",
             "node7.bost.link",
             "node8.bost.link",
             "node9.bost.link",
             "node10.bost.link")
    port = 9697


class BoostCoinTestNet(BoostCoin):
    """
    Class with all the necessary BoostCoin testing network information based on
    https://github.com/mammix2/boostcoin-core/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-boostcoin'
    seeds = ("5kbw5bcuudj2s75s.onion",
             "gjgbuc3l52fxea5o.onion",
             "dg5moxtmks3auqc5.onion",
             "5hrzeemkppcdalp3.onion",
             "uwbrmhzppueemse5.onion",
             "3kt3ypmt63v7fhwg.onion",
             "bivpn37zx5g25u2g.onion",
             "o2jjy6kkavi7wbx3.onion",
             "rzqujgnsnejxkk3e.onion",
             "ylou7bnzivq2xgfc.onion",)
    port = 19697
