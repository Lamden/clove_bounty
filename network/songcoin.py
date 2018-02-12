
from clove.network.bitcoin import Bitcoin


class SongCoin(Bitcoin):
    """
    Class with all the necessary SONG network information based on
    http://www.github.com/Songcoin/Songcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'songcoin'
    symbols = ('SONG', )
    seeds = ('seed.songcoin.org',)
    port = 8335


class SongCoinTestNet(SongCoin):
    """
    Class with all the necessary SONG testing network information based on
    http://www.github.com/Songcoin/Songcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-songcoin'
    seeds = ('seed.songcoin.org',)
    port = 18335
