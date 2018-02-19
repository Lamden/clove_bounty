from clove.network.bitcoin import Bitcoin


class PascalCoin(Bitcoin):
    """
    Class with all the necessary Pascal Coin (PASC) network information based on
    https://github.com/PascalCoin/PascalCoin/blob/master/Units/PascalCoin/UConst.pas
    (date of access: 02/18/2018)
    """
    name = 'pascalcoin'
    symbols = ('PASC', )
    seeds = ('bpascal1.dynamic-dns.net',
			 'bpascal2.dynamic-dns.net',
			 'pascalcoin1.dynamic-dns.net',
			 'pascalcoin2.dynamic-dns.net',
			 'pascalcoin1.dns1.us',
			 'pascalcoin2.dns1.us',
			 'pascalcoin1.dns2.us',
			 'pascalcoin2.dns2.us')
    port = 4004

# no testnet
