#!/usr/bin/env python3

import random
import sys
import platform

if(platform.system() == "Linux"):
    cRED = "\033[31m"
    cBLUE = "\033[34m"
    cGREEN = "\033[32m"
    cRESET_ALL = "\033[0m"

else:
    cRED = ""
    cBLUE = ""
    cGREEN = ""
    cRESET_ALL = ""


osObjetos = [
    "O Crime",
    "A Felicidade",
    "O Escudo",
    "A Espada",
    "As Polainas",
    "O Escafandro",
    "O Tradutor",
    "A Esperança"
]

asPessoas = [
    "Do Ignorante",
    "Do Sádico",
    "Do Abestado",
    "Do Sábio",
    "Do Satanista",
    "Do Sagrado",
    "Do Programador",
    "Do Desajustado"
]

asCarinhas = [
    "( ͡° ͜ʖ ͡°)",
    "¯\_(ツ)_/¯",
    "ಠ_ಠ",
    "(╯°□°）╯︵ ┻━┻",
    "(⌐■_■)",
    "ʕ•ᴥ•ʔ",
    "(•̀ᴗ•́)و",
    "ಥ_ಥ",
    "(⊙_☉)",
    "(ง •̀_•́)ง"
]


if __name__ == "__main__":
    try:
        palavra = sys.argv[1].upper()+" "+(" ".join(sys.argv[2:]))
    except:
        palavra = "O Uso Errado"
    objeto = random.choice(osObjetos)
    pessoa = random.choice(asPessoas)
    carinha = random.choice(asCarinhas)

    pre = "{red}{palavra}{reset} é {blue}{obj}{reset} {green}{pes}{reset} {car}".format(palavra = palavra,obj = objeto, pes = pessoa,car = carinha, red = cRED, blue=cBLUE, green=cGREEN,reset=cRESET_ALL)
    print(pre)






