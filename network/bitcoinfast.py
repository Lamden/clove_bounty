from clove.network.bitcoin import Bitcoin


class BitcoinFast(Bitcoin):
    """
    Class with all the necessary Evilcoin network information based on
    https://github.com/crypto-currency/bitcoinfast/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'bitcoinfast'
    symbols = ('BCF', )
    seeds = ("bitcoinfast.co", )
    port = 25671
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 153
    }

# Has no Testnet
