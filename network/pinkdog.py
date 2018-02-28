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


class PinkDogTestNet(PinkDog):
    """
    Class with all the necessary PinkDog testing network information based on
    https://github.com/PinkDogOfficial/pinkdog/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-pinkdog'
    seeds = ("mytestseed.org")
    port = 19777
