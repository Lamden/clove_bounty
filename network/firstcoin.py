from clove.network.bitcoin import Bitcoin


class FirstCoin(Bitcoin):
    """
    Class with all the necessary FirstCoin network information based on
    https://github.com/firstcoinofficial/firstcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'firstcoin'
    symbols = ('FRST', )
    seeds = ("108.179.227.118")
    port = 10667
    message_start = b'\xc3\xd2\xd1\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }


class FirstCoinTestNet(FirstCoin):
    """
    Class with all the necessary FirstCoin testing network information based on
    https://github.com/firstcoinofficial/firstcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-firstcoin'
    seeds = ("192.168.200.100")
    port = 10667
    message_start = b'\xd1\xb2\xa4\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
