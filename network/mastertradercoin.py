from clove.network.bitcoin import Bitcoin


class MasterTraderCoin(Bitcoin):
    """
    Class with all the necessary MasterTraderCoin network information based on
    https://github.com/chrysophylax69/mastertrader/blob/master/src/net.cpp#L13
    (date of access: 02/16/2018)
    """
    name = 'mastertradercoin'
    symbols = ('MTR', )
    seeds = ("mtr-seed01.chainworksindustries.com",
             "mtr-seed02.chainworksindustries.com",
             "mtr-seed03.chainworksindustries.com",
             "mtr-seed04.chainworksindustries.com",
             "mtr-seed05.chainworksindustries.com",
             "mtr-seed06.chainworksindustries.com",
             "mtr-seed07.chainworksindustries.com")
    port = 14475
