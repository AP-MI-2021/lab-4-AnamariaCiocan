def show_menu():
    print('1. Citire lista')
    print('2. Afisarea partii intregi a numerelor din lista')
    print('3. Afisarea numerelor care apartin unui interval deschis citit de la tastatura')
    print('4. Afisarea numerelor a caror parte intreaga este divizor al partii fractionare')
    print('5. Afisarea listei obtinuta din lista initiala in care numerele sunt inlocuite cu un string de cuvinte care le descriu')
    print('x. Exit')

def citire_lista():
    floats_as_str=input('Dati o lista de numere float separate printr-un spatiu: ')
    floats_as_str=floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_str:
        floats.append(float(float_str))
    return floats

def show_parte_intreaga(lst):
    print(f'Partea intreaga a numerelor din lista: {lst} sunt: {get_parte_intreaga(lst)}')

def get_parte_intreaga(lst):
    '''
    Determina partea intreaga a numerelor din lista citita.
    :param lst: lista de numere data
    :return: o lista cu partea intreaga a numerelor din lista.
    '''
    result=[]
    for num in lst:
        result.append(int(num))
    return result

def test_get_parte_intreaga():
    assert get_parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert get_parte_intreaga([3.3, 5, 6.7, 9.1]) == [3, 5, 6, 9]
    assert get_parte_intreaga([4.4, 3.2, 9, 6.8]) == [4, 3, 9, 6]
    assert get_parte_intreaga([5.5, 8.3, 7.4, 2.2]) == [5, 8, 7, 2]

def show_numere_din_interval(lst):
    a=int(input('Dati un numar pentru primul capat al intervalului deschis: '))
    b=int(input('Dati un numar pentru al doilea capat al intervalului deschis: '))
    print(f'Numerele din lista {lst} care se afla in interval sunt: {get_numere_din_interval(lst, a, b)}')


def get_numere_din_interval(lst, a, b):
    '''
    Determina numerele care se afla in intervalul deschis citit de la tastatura.
    :param lst: lista de numere
    :param a: primul capat al intervalului
    :param b: al doilea capat al intervalului
    :return: lista de numere din interval
    '''
    result=[]
    for i in lst:
        if i>a:
            if i<b:
                result.append(i)
    return result

def test_get_numere_din_interval():
    assert get_numere_din_interval([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert get_numere_din_interval([3.3, 4.4, 6.6], 8, 12) == []
    assert get_numere_din_interval([1.2, 3.6, 9.3, 2.4], 2, 4) == [3.6, 2.4]
    assert get_numere_din_interval([10, 20, 19.1, 21], 18, 20) == [19.1]

def show_intreg_divide_fractionar(lst):
    print(f'Numerele a caror parte intreaga divide partea fractionara sunt: {get_intreg_divide_fractionar(lst)}')


def get_intreg_divide_fractionar(lst):
    '''
    Determina numerele a caror parte intreaga divide partea lor fractionara.
    :param lst: lista de numere
    :return: lista cu numerele avand proprietatea ceruta
    '''
    result=[]
    for elem in lst:
        str_elem=str(elem)
        if '.' in str_elem:
            decimals = str_elem.split('.')[1]
            n=int(elem)
            if decimals % n == 0:
                result.append(elem)
    return result

def test_get_intreg_divide_fractionar():
    assert get_intreg_divide_fractionar([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert get_intreg_divide_fractionar([9.8, 7.6, 4.5, 3.8]) == []
    assert get_intreg_divide_fractionar([8.8, 7.7]) == [8.8, 7.7]
    assert get_intreg_divide_fractionar([8.9, 9.8, 5.5, 4.3]) == [5.5]

def get_inlocuire_string(lst):
    '''
    Inlocuieste caracter cu caracter numerele cu stringurile corespunzatoare
    :param lst:lista initiala
    :return: lista de stringuri
    '''
    result=[]
    for elem in lst:
        str_elem=str(elem)
        for i in range (len(str_elem)):
            if i == '-':
                result.append('minus')
            elif i =='1':
                result.append('unu')
            elif i =='2':
                result.append('doi')
            elif i =='3':
                result.append('trei')
            elif i =='4':
                result.append('patru')
            elif i =='5':
                result.append('cinci')
            elif i =='6':
                result.append('sase')
            elif i =='7':
                result.append('sapte')
            elif i =='8':
                result.append('opt')
            elif i =='9':
                result.append('noua')
            elif i =='.':
                result.append('punct')
        result.append(' ')
    return result

def test_get_inlocuire_string():
    assert get_inlocuire_string([2, 3, 5.6]) == ['doi', 'trei', 'cincipunctsase']
    assert get_inlocuire_string([]) == []
    assert get_inlocuire_string([1.5, -3.3, 8, 9.8, 3.2, 14.52]) == ['unuvirgulacinci', 'minustreivirgulatrei', 'opt', 'nouavirgulaopt', 'treivirguladoi', 'unupatruvirgulacincidoi']

def show_inlocuire_string(lst):
    print(f'Inlocuirea caracter cu caracter a sirului de numere cu un stringuri este: {get_inlocuire_string(lst)}')

def main():
    lst=[]
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lst=citire_lista()
        elif option == '2':
            show_parte_intreaga(lst)
        elif option == '3':
            show_numere_din_interval(lst)
        elif option == '4':
            show_intreg_divide_fractionar(lst)
        elif option == '5':
            show_inlocuire_string(lst)
        elif option == 'x':
            break
        else: 
            print('Optiune invalida, reancearca!')

if __name__ == '__main__':
    test_get_numere_din_interval()
    test_get_parte_intreaga()
    test_get_intreg_divide_fractionar()
    test_get_inlocuire_string()
    main() 
        
            