
from clove.network.bitcoin import Bitcoin


class AudioCoin(Bitcoin):
    """
    Class with all the necessary ADC network information based on
    http://www.github.com/aurovine/audiocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'audiocoin'
    symbols = ('ADC', )
    seeds = ('52.56.111.222', '52.56.175.189', '35.176.14.149')
    port = 25159


class AudioCoinTestNet(AudioCoin):
    """
    Class with all the necessary ADC testing network information based on
    http://www.github.com/aurovine/audiocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-audiocoin'
    seeds = ('178.62.233.116', 'adcseed.presstab.pw')
    port = 25159
