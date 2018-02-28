from clove.network.bitcoin import Bitcoin


class BitcoinPlus(Bitcoin):
    """
    Class with all the necessary Bitcoin Plus (XBC) network information based on
    https://github.com/bitcoinplusorg/xbcwalletsource/blob/origin/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'bitcoinplus'
    symbols = ('XBC', )
    seeds = ('seednode1.bitcoinplus.net', 'seednode2.bitcoinplus.net',
             'seednode3.bitcoinplus.net', 'seednode4.bitcoinplus.net', 'seednode5.bitcoinplus.net')
    port = 8884

# no testnet
