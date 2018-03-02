from clove.network.bitcoin import Bitcoin


class DigitalMoneyBits(Bitcoin):
    """
    Class with all the necessary  Digital Money Bits (DMB) network information based on
    https://github.com/DMBcryptocurrency/DMB-project/blob/master/DigitalMoneyBits-master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'digital_money_bits'
    symbols = ('DMB', )
    nodes = ('195.74.52.227', )
    port = 64008
    message_start = b'\x3f\xf3\x4f\xf4'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 89,
        'SECRET_KEY': 218
    }


class DigitalMoneyBitsTestNet(DigitalMoneyBits):
    """
    Class with all the necessary  Digital Money Bits (DMB) network information based on
    https://github.com/DMBcryptocurrency/DMB-project/blob/master/DigitalMoneyBits-master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-digital_money_bits'
    symbols = ('DMB', )
    seeds = ()
    port = 16408
    message_start = b'\xea\x19\xaa\xc5'
    base58_prefixes = {
        'PUBKEY_ADDR': 91,
        'SCRIPT_ADDR': 92,
        'SECRET_KEY': 219
    }
