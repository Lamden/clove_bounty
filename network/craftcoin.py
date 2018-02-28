from clove.network.bitcoin import Bitcoin


class CraftCoin(Bitcoin):
    """
    Class with all the necessary Diamond network information based on
    https://github.com/craftcoin/craftcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'craftcoin'
    symbols = ('CRC', )
    seeds = ("smp1.spendlitecoins.com")
    port = 12124

# Has no testnet
