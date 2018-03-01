from clove.network.bitcoin import Bitcoin


class Gulden(Bitcoin):
    """
    Class with all the necessary Gulden network information based on
    https://github.com/Gulden/gulden-official/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'gulden'
    symbols = ('NLG', )
    seeds = ("seed.gulden.com",
             "rotterdam.gulden.network")
    port = 9231
    message_start = b'\xfc\xfe\xf7\xe0'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 98,
        'SECRET_KEY': 166
    }


class GuldenTestNet(Gulden):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/Gulden/gulden-official/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-gulden'
    seeds = ("testseed.gulden.blue",
             "testseed.gulden.network",
             "testseed.coinpool.nl")
    port = 9923
    message_start = b'targetIntervalseedTimestamp >> 8seedTimestamp >> 16\xFF'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 122,
        'SECRET_KEY': 188
    }
