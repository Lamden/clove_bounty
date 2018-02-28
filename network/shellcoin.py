from clove.network.bitcoin import Bitcoin


class ShellCoin(Bitcoin):
    """
    Class with all the necessary ShellCoin network information based on
    https://bitcointalk.org/index.php?topic=1054714.0
    (date of access: 02/19/2018)
    """
    name = 'shellcoin'
    symbols = ('SHELL', )
    seeds = ("153.92.98.55")
    port = 12454
