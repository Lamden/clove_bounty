from clove.network.bitcoin import Bitcoin


class Auroracoin(Bitcoin):
    """
    Class with all the necessary Auroracoin network information based on
    https://www.github.com/aurarad/auroracoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'Auroracoin'
    symbols = ('AUR', )
    seeds = ('s1.auroraseed.net', 'aurseed1.criptoe.com', 's1.auroraseed.com', 's1.auroraseed.org',
             's1.auroraseed.eu', 'electrum2.aurorcoin.is', 'electrum3.auroracoin.is', 'electrum4.auroracoin.is')
    port = 12340
    message_start = b'\xfd\xa4\xdc\x6c'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


# Has no Testnet
