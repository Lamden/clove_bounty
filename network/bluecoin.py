from clove.network.bitcoin import Bitcoin


class BlueCoin(Bitcoin):
    """
    Class with all the necessary AUR network information based on
    https://github.com/bluecoiner/bluecoin-new/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'bluecoin'
    symbols = ('BLU', )
    seeds = ()
    port = 27104


class BlueCoinTestNet(BlueCoin):
    """
    Class with all the necessary AUR testing network information based on
    https://github.com/bluecoiner/bluecoin-new/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-bluecoin'
    seeds = ()
    port = 17104