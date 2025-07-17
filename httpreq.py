import csv
import pathlib

import requests

# TODO
# def carrega_animais(arq_csv: pathlib.Path) -> dict[str, dict[str, str]]:

def num_validos(n_animais: set[int], limi_inf: int, lim_sup: int) -> bool:
    return all([limi_inf<=n<=lim_sup for n in n_animais])

def main():
    pass

try:
    leitor = csv.DictReader(open('emojis-animais.csv', encoding='utf-8', mode='r'))
    animais = {dados_animal['portugues']:dados_animal for dados_animal in leitor}
    total_animais = len(animais)
    animal_chave = {i:nome for i,nome in enumerate(sorted(animais.keys()), start=1)}

    num_animais = set()
    while len(num_animais)!=7 or not num_validos(num_animais, 1, total_animais):
        print('Escolha de animais')
        for i,nome in animal_chave.items():
            print(f'{i}. {nome}')

        print('Escolha 7 animais, separados por espaço.')
        print()
        num_animais = set(map(int, input('Número dos 7 animais: ').split()))

    # Reforça o nome dos animais selecionados
    print('Ótimo. Você selecionou os seguintes animais:')
    for n in num_animais:
        print(f'{n}. {animal_chave[n]}')

except Exception as e:
    print('Deu erro.', e)

if __name__ == '__main__':
    # requests.delete()
    main()