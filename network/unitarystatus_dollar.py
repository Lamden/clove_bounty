from clove.network.bitcoin import Bitcoin


class UnitaryStatus_Dollar(Bitcoin):
    """
    Class with all the necessary UnitaryStatus Dollar network information based on
    https://github.com/usde-project/USDE/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'unitarystatus_dollar'
    symbols = ('USDE', )
    seeds = ("liteminers.com")
    port = 54449
    message_start = b'\xd9\xd9\xf9\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }

# no testnet
