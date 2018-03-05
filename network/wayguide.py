
from clove.network.bitcoin import Bitcoin


class WayGuide(Bitcoin):
    """
    Class with all the necessary WAY network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'wayguide'
    symbols = ('WAY', )
    nodes = (
        '104.167.119.153',
        '106.185.46.190',
        '119.96.207.40',
        '151.80.166.168',
        '162.243.234.233',
        '176.9.0.19',
        '176.9.65.41',
        '191.238.242.192',
        '198.27.80.162',
        '24.22.169.199',
        '37.187.62.197',
        '37.59.103.62',
        '45.48.14.241',
        '5.135.147.146',
        '5.196.82.175',
        '66.205.195.234',
        '71.252.212.230',
        '74.208.184.161',
        '76.88.138.192',
        '87.127.113.47',
        '89.215.246.62',
        '94.23.38.198',
        '98.192.139.14',
        '99.238.193.38',
    )
    port = 21000
    message_start = b'\x57\x41\x59\x47'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 97,
        'SECRET_KEY': 173
    }


class WayGuideTestNet(WayGuide):
    """
    Class with all the necessary WAY testing network information based on
    https://github.com/wayguide/waycoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wayguide'
    seeds = ()
    port = 22000
    message_start = b'\x77\x61\x79\x67'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 208,
        'SECRET_KEY': 249
    }
