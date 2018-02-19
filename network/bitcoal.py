from clove.network.bitcoin import Bitcoin


class BitCoal(Bitcoin):
    """
    Class with all the necessary BitCoal (COAL) network information based on
    https://github.com/bitcoal/bitcoalwallet/blob/master/cryptonote/src/CryptoNoteConfig.h
    (date of access: 02/18/2018)
    """
    name = 'bitcoal'
    symbols = ('COAL', )
    seeds = ('108.61.188.93', '136.243.69.10', '192.121.166.182')
    port = 7700

# no testnet
