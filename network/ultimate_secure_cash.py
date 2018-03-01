
from clove.network.bitcoin import Bitcoin


class UltimateSecureCash(Bitcoin):
    """
    Class with all the necessary USC network information based on
    http://www.github.com/SilentTrader/UltimateSecureCash/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'ultimatesecurecash'
    symbols = ('USC', )
    seeds = ('45.55.52.85',)
    port = 51737
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }


class UltimateSecureCashTestNet(UltimateSecureCash):
    """
    Class with all the necessary USC testing network information based on
    http://www.github.com/SilentTrader/UltimateSecureCash/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-ultimatesecurecash'
    seeds = ()
    port = 51997
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 255
    }
