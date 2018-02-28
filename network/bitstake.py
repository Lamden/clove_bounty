from clove.network.bitcoin import Bitcoin


class BitStake(Bitcoin):
    """
    Class with all the necessary BitStake network information based on
    https://github.com/Bitstake/bitstakesource/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitstake'
    symbols = ('XBS', )
    nodes = (
        "71.236.71.3",
        "198.50.198.105",
        "198.50.198.106",
        "198.50.198.107",
        "173.88.17.232",
        "213.213.193.147",
        "92.222.38.197",
        "83.157.62.179",
        "144.76.239.66",
        "104.236.5.17",
        "104.236.29.189"
    )
    port = 38462

# Has no testnet
