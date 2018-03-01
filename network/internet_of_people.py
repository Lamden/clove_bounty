from clove.network.bitcoin import Bitcoin


class InternetOfPeople(Bitcoin):
    """
    Class with all the necessary Internet Of People (IOP) network information based on
    https://github.com/Internet-of-People/iop-core/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'internetofpeople'
    symbols = ('IOP', )
    seeds = ('mainnet.iop.cash', 'main1.iop.cash', 'main2.iop.cash', 'main3.iop.cash',
             'main4.iop.cash', 'main5.iop.cash', 'main6.iop.cash')
    port = 4877
    message_start = b'\xfd\xb0\xbb\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 117,
        'SCRIPT_ADDR': 174,
        'SECRET_KEY': 49
    }


class InternetOfPeopleTestNet(InternetOfPeople):
    """
    Class with all the Internet Of People (IOP) testing network information based on
    https://github.com/Internet-of-People/iop-core/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-internetofpeople'
    seeds = ('testnet.iop.cash', 'test1.iop.cash', 'test2.iop.cash')
    port = 7475
