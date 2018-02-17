from clove.network.bitcoin import Bitcoin


class SpeedCash(Bitcoin):
    """
    Class with all the necessary SpeedCash (SCS) network information based on
    https://github.com/scashml/scashcpp/blob/main/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'speedcash'
    symbols = ('SCS', )
    seeds = ('node001.scash.ml', 'node002.scash.ml', 'node003.scash.ml')
    port = 35334

# no testnet
