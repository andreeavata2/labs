#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""


from __future__ import print_function


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    if not mesaj:
        print("Nu am primit mesaj!")
        return
    for i in range(1, 27):
        result = []
        for letter in mesaj:
            if letter.isalpha():
                a_result = ord(letter)
                a_result += i
                if a_result < ord('A'):
                    a_result += 26
                elif a_result > ord('z'):
                    a_result -= 26
                result.append(chr(a_result))
            else:
                result.append(letter)
            s_result = ''.join(result)
        if s_result.startswith('ave'):
            print(s_result)


def main():
    """ Main function docstring """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()