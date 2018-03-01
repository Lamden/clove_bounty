
from clove.network.bitcoin import Bitcoin


class LetItRide(Bitcoin):
    """
    Class with all the necessary LIR network information based on
    http://www.github.com/shogdite/letitride/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'letitride'
    symbols = ('LIR', )
    seeds = ('198.27.90.242',)
    port = 2717
    message_start = b'\x2f\xc3\xe5\x27'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 153
    }


class LetItRideTestNet(LetItRide):
    """
    Class with all the necessary LIR testing network information based on
    http://www.github.com/shogdite/letitride/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-letitride'
    seeds = ()
    port = 3717
    message_start = b'\xef\xc3\x1e\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
