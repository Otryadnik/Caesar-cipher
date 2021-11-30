eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
igits = '0123456789'

decryption_or_encrypt = input('Здравствуйте. Что неоходимо сделать. Если заштфровать введите (ш), если дешифровать '
                              'введите (д) или подобрать ключь к шифру (п): ')
while decryption_or_encrypt.lower() != 'д' and decryption_or_encrypt.lower() != 'ш' \
        and decryption_or_encrypt.lower() != 'п':
    decryption_or_encrypt = input(
        'Неверный ввод. Если заштфровать введите (ш), если дешифровать введите (д), если подобрать ключь к шифру (п): ')
text_to_encrypt = input('Введите текст: ')
step = int(input('Введите шаг шифрования: '))


def sing(symbol):
    if symbol in eng_lower_alphabet:
        return eng_lower_alphabet
    elif symbol in eng_upper_alphabet:
        return eng_upper_alphabet
    elif symbol in rus_lower_alphabet:
        return rus_lower_alphabet
    elif symbol in rus_upper_alphabet:
        return rus_upper_alphabet
    elif symbol in igits:
        return igits
    else:
        return symbol


def encrypt(txt, step_encrypt):
    encrypt_end = ''
    if decryption_or_encrypt.lower() == 'д':
        for c in txt:
            symbol = sing(c)
            if symbol == c:
                encrypt_end += c
            elif symbol.find(c) - step_encrypt < 0:
                c = symbol.find(c) - step_encrypt + len(symbol)
                encrypt_end += symbol[c]
            elif symbol.find(c) - step_encrypt >= 0:
                c = symbol.find(c) - step_encrypt
                encrypt_end += symbol[c]


    elif decryption_or_encrypt.lower() == 'ш':
        for c in txt:
            symbol = sing(c)
            if symbol == c:
                encrypt_end += c
            elif symbol.find(c) + step_encrypt >= len(symbol):
                c = symbol.find(c) + step_encrypt - len(symbol)
                encrypt_end += symbol[c]
            elif symbol.find(c) + step_encrypt < len(symbol):
                c = symbol.find(c) + step_encrypt
                encrypt_end += symbol[c]

    elif decryption_or_encrypt.lower() == 'п':
        step_encrypt = 0
        end = 'да'
        while end.lower() == 'да':
            encrypt_end = ''
            step_encrypt += 1
            for c in txt:
                symbol = sing(c)
                if symbol == c:
                    encrypt_end += c
                elif symbol.find(c) - step_encrypt < 0:
                    c = symbol.find(c) - step_encrypt + len(symbol)
                    encrypt_end += symbol[c]
                elif symbol.find(c) - step_encrypt >= 0:
                    c = symbol.find(c) - step_encrypt
                    encrypt_end += symbol[c]
            print(encrypt_end)
            end = input('Чтобы продолжить введите (да). Для завершения введите (стоп): ')

    return encrypt_end


print(encrypt(text_to_encrypt, step))
