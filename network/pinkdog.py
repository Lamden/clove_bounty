from clove.network.bitcoin import Bitcoin


class PinkDog(Bitcoin):
    """
    Class with all the necessary PinkDog network information based on
    https://github.com/PinkDogOfficial/pinkdog/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'pinkdog'
    symbols = ('PDG', )
    seeds = ("pinkdog.party")
    port = 17771
    message_start = b'\xc3\xf1\x8d\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 28
    }


class PinkDogTestNet(PinkDog):
    """
    Class with all the necessary PinkDog testing network information based on
    https://github.com/PinkDogOfficial/pinkdog/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-pinkdog'
    seeds = ("mytestseed.org")
    port = 19777
    message_start = b'\xba\xf8\xfb\x99'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 48,
        'SECRET_KEY': 50
    }
