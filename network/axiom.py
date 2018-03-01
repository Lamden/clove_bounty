
from clove.network.bitcoin import Bitcoin


class Axiom(Bitcoin):
    """
    Class with all the necessary AXIOM network information based on
    http://www.github.com/axiomcryptocurrency/axiom/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'axiom'
    symbols = ('AXIOM', )
    seeds = ('seed.axiomcoin.xyz',)
    port = 15760
    message_start = b'\x03\x3f\x1a\x0c'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class AxiomTestNet(Axiom):
    """
    Class with all the necessary AXIOM testing network information based on
    http://www.github.com/axiomcryptocurrency/axiom/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-axiom'
    seeds = ()
    port = 25760
    message_start = b'\x3f\x1a\x1c\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
