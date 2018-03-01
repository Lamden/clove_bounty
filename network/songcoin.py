
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
    message_start = b'\x53\x4f\x4e\x47'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }


class SongCoinTestNet(SongCoin):
    """
    Class with all the necessary SONG testing network information based on
    http://www.github.com/Songcoin/Songcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-songcoin'
    seeds = ('seed.songcoin.org',)
    port = 18335
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
