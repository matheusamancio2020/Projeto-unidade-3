
def negrito(texto):
    return '\033[1m' + texto + '\033[0m'


def sublinhado(texto):
    return '\033[4m' + texto + '\033[0m'


def vermelho(texto):
    return '\033[91m' + texto + '\033[0m'


def verde(texto):
    return '\033[92m' + texto + '\033[0m'


def amarelo(texto):
    return '\033[93m' + texto + '\033[0m'


def azul(texto):
    return '\033[94m' + texto + '\033[0m'


def roxo(texto):
    return '\033[95m' + texto + '\033[0m'


def ciano(texto):
    return '\033[96m' + texto + '\033[0m'


def piscar(texto):
    return '\033[5m' + texto + '\033[0m'


def oculto(texto):
    return '\033[8m' + texto + '\033[0m'


def espacamento():
    print('-'* 85)


