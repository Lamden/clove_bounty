from clove.network.bitcoin import Bitcoin


class  DigitalMoneyBits(Bitcoin):
    """
    Class with all the necessary  Digital Money Bits (DMB) network information based on
    https://github.com/DMBcryptocurrency/DMB-project/blob/master/DigitalMoneyBits-master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'digital_money_bits'
    symbols = ('DMB', )
    seeds =  ('195.74.52.227')
    port = 64008


class  DigitalMoneyBitsTestNet(DigitalMoneyBits):
    """
    Class with all the necessary  Digital Money Bits (DMB) network information based on
    https://github.com/DMBcryptocurrency/DMB-project/blob/master/DigitalMoneyBits-master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-digital_money_bits'
    symbols = ('DMB', )
    seeds =  ()
    port = 16408