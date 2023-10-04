def convert(i,number):
    if i == 1:
        print('число',number,'у двійковій системі дорівнює:')
        print(bin(number))
    elif i == 2:
        print('число', number, 'у вісімковій системі дорівнює:')
        print(oct(number))
    else:
        print('число', number, 'у шіснадцятковій системі дорівнює:')
        print(hex(number))

def convert_choise():
    options = ['двійкова', 'вісімкова', 'шіснадцятквоа']
    d = 0
    print("Будь ласка виберіть систему числення, в яку необхідно перевести число:")
    for element in options:
        d += 1
        print("{}) {}".format(d, element))
    i = int(input("введіть номер: "))
    try:
        if 0 < i <= len(options):
            convert(i, number)
        else:
            print("виникла помилка при введенні данних.")
    except:
        print("виникла помилка при введенні данних.")

try:
    number=int(input("введіть число:"))
    convert_choise()
except:
    print("виникла помилка при введенні данних.")
