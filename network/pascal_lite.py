from clove.network.bitcoin import Bitcoin


class PascalLite(Bitcoin):
    """
    Class with all the necessary Pascal Lite (PASL) network information based on
    https://github.com/PascalLite/wallet/blob/master/Units/PascalCoin/UConst.pas
    (date of access: 02/18/2018)
    """
    name = 'pascallite'
    symbols = ('PASL', )
    seeds = ('pascallite.ddns.net',
             'pascallite2.ddns.net',
             'pascallite3.ddns.net',
             'pascallite4.dynamic-dns.net',
             'pascallite5.dynamic-dns.net',
             'pascallite.dynamic-dns.net',
             'pascallite2.dynamic-dns.net',
             'pascallite3.dynamic-dns.net')
    port = 4004

# no testnet
