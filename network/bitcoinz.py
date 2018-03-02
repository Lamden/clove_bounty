from clove.network.bitcoin import Bitcoin


class BitcoinZ(Bitcoin):
    """
    Class with all the necessary BitcoinZ network information based on
    https://github.com/bitcoinz-pod/bitcoinz/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitcoinz'
    symbols = ('BTCZ', )
    seeds = ("btcz.kovach.biz",
             "seed.btcz.life",
             "bzseed.secnode.tk",
             "btzseed.blockhub.info",
             "btcz-us.crypt29.net",
             "btcz.vnminers.com",
             "dnsseed.ppcall.ru")
    port = 1989


class BitcoinZTestNet(BitcoinZ):
    """
    Class with all the necessary BitcoinZ testing network information based on
    https://github.com/bitcoinz-pod/bitcoinz/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-BitcoinZ'
    seeds = ("test-dnsseed.rotorproject.org")
    port = 11989
