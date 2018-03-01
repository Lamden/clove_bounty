from clove.network.bitcoin import Bitcoin


class Neutron(Bitcoin):
    """
    Class with all the necessary Neutron network information based on
    https://github.com/neutroncoin/neutron/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'neutron'
    symbols = ('NTRN', )
    seeds = ('ntrnseed.presstab.pw', 'ntrn.seed.fuzzbawls.pw')
    port = 32001
    message_start = b'\xb2\xd1\xf4\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 21,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 149
    }

# Has no testnet
