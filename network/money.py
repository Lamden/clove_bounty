from clove.network.bitcoin import Bitcoin


class Money(Bitcoin):
    """
    Class with all the necessary Money ($$$) network information based on
    https://github.com/moneyfoundation/money/blob/master-0.8/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'money'
    symbols = ('$$$', )
    seeds = ('dns.yourmoneyknowledge.com', 'moneydns.info.tm')
    port = 11082


class MoneyTestNet(Money):
    """
    Class with all the necessary Money ($$$) testing network information based on
    https://github.com/moneyfoundation/money/blob/master-0.8/src/net.cpp    
    (date of access: 02/18/2018)
    """
    name = 'test-money'
    seeds = ('dns.yourmoneyknowledge.com')
    port = 21082
