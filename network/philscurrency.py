from clove.network.bitcoin import Bitcoin


class PhilsCurrency(Bitcoin):
    """
    Class with all the necessary PhilsCurrency network information based on
    https://github.com/philscurrency/philscurrency/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'philscurrency'
    symbols = ('PHILS', )
    seeds = ("dnsseed1.philscurrency.org",
             "dnsseed2.philscurrency.org",
             "dnsseed3.philscurrency.org",
             "explorer.philscurrency.org")
    port = 36003
    message_start = b'\xc1\xf4\xa7\xd6'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 118,
        'SECRET_KEY': 117
    }

# no testnet
