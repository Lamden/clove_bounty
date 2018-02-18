from clove.network.bitcoin import Bitcoin


class PeopleCoin(Bitcoin):
    """
    Class with all the necessary PeopleCoin network information based on
    https://github.com/peopleproject/people/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'peoplecoin'
    symbols = ('MEN', )
    seeds = ("seed.peoplecoin.pw")
    port = 7721
	
# no testnet