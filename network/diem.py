from clove.network.bitcoin import Bitcoin


class Diem(Bitcoin):
    """
    Class with all the necessary Diem network information based on
    https://github.com/diemcoin/carpediemcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'diem'
    symbols = ('DIEM', )
    seeds = ("dnsseed.carpediemexplorer.com")
    port = 9449

# Has no testnet
