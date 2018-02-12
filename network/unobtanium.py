
from clove.network.bitcoin import Bitcoin


class Unobtanium(Bitcoin):
    """
    Class with all the necessary UNO network information based on
    http://www.github.com/unobtanium-official/Unobtanium/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'unobtanium'
    symbols = ('UNO', )
    seeds = ('node1.unobtanium.uno', 'node2.unobtanium.uno', 'unobtanium.cryptap.us')
    port = 65534


class UnobtaniumTestNet(Unobtanium):
    """
    Class with all the necessary UNO testing network information based on
    http://www.github.com/unobtanium-official/Unobtanium/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-unobtanium'
    seeds = ('23skidoo.info', 'testnet.unobtanium.info')
    port = 65525
