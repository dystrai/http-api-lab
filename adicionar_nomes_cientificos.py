#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para adicionar a coluna "Nome científico" ao arquivo emojis-animais.csv
"""

import csv

def obter_nomes_cientificos():
    """Retorna um dicionário com os nomes científicos dos animais"""
    nomes_cientificos = {
        'ant': 'Formicidae',
        'badger': 'Meles meles',
        'bat': 'Chiroptera',
        'beaver': 'Castor canadensis',
        'beetle': 'Coleoptera',
        'bird': 'Aves',
        'bison': 'Bison bison',
        'blowfish': 'Tetraodontidae',
        'buffalo': 'Bubalus bubalis',
        'bug': 'Hemiptera',
        'butterfly': 'Lepidoptera',
        'camel': 'Camelus dromedarius',
        'cat': 'Felis catus',
        'chick': 'Gallus gallus domesticus',
        'chipmunk': 'Tamias striatus',
        'cockroach': 'Blattodea',
        'coral': 'Anthozoa',
        'cow': 'Bos taurus',
        'crab': 'Brachyura',
        'cricket': 'Gryllidae',
        'crocodile': 'Crocodylus niloticus',
        'deer': 'Cervidae',
        'dodo': 'Raphus cucullatus',
        'dog': 'Canis lupus familiaris',
        'dolphin': 'Delphinus delphis',
        'dove': 'Columbidae',
        'dromedary': 'Camelus dromedarius',
        'duck': 'Anas platyrhynchos',
        'eagle': 'Aquila chrysaetos',
        'elephant': 'Elephas maximus',
        'fish': 'Pisces',
        'flamingo': 'Phoenicopterus roseus',
        'fly': 'Diptera',
        'giraffe': 'Giraffa camelopardalis',
        'goat': 'Capra aegagrus hircus',
        'goose': 'Anser anser',
        'gorilla': 'Gorilla gorilla',
        'hedgehog': 'Erinaceus europaeus',
        'hippopotamus': 'Hippopotamus amphibius',
        'honeybee': 'Apis mellifera',
        'horse': 'Equus caballus',
        'jellyfish': 'Scyphozoa',
        'kangaroo': 'Macropus rufus',
        'ladybeetle': 'Coccinellidae',
        'leopard': 'Panthera pardus',
        'lizard': 'Lacertilia',
        'llama': 'Lama glama',
        'lobster': 'Homarus americanus',
        'mammoth': 'Mammuthus primigenius',
        'monkey': 'Primates',
        'mosquito': 'Culicidae',
        'mouse': 'Mus musculus',
        'octopus': 'Octopus vulgaris',
        'orangutan': 'Pongo pygmaeus',
        'otter': 'Lutra lutra',
        'owl': 'Strigiformes',
        'ox': 'Bos taurus',
        'parrot': 'Psittaciformes',
        'peacock': 'Pavo cristatus',
        'penguin': 'Spheniscidae',
        'pig': 'Sus scrofa domesticus',
        'poodle': 'Canis lupus familiaris',
        'rabbit': 'Oryctolagus cuniculus',
        'ram': 'Ovis aries',
        'rat': 'Rattus rattus',
        'rhinoceros': 'Rhinocerotidae',
        'rooster': 'Gallus gallus domesticus',
        'sauropod': 'Sauropoda',
        'scorpion': 'Scorpiones',
        'seal': 'Pinnipedia',
        'sheep': 'Ovis aries',
        'shrimp': 'Caridea',
        'skunk': 'Mephitis mephitis',
        'sloth': 'Bradypus tridactylus',
        'snail': 'Gastropoda',
        'snake': 'Serpentes',
        'spider': 'Araneae',
        'squid': 'Teuthida',
        'swan': 'Cygnus olor',
        't-rex': 'Tyrannosaurus rex',
        'tiger': 'Panthera tigris',
        'turkey': 'Meleagris gallopavo',
        'turtle': 'Testudines',
        'worm': 'Annelida',
        'whale': 'Cetacea'
    }
    return nomes_cientificos

def adicionar_nomes_cientificos():
    """Adiciona a coluna 'Nome científico' ao arquivo CSV"""
    nomes_cientificos = obter_nomes_cientificos()
    
    # Ler arquivo original
    linhas_originais = []
    with open('emojis-animais.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        linhas_originais = list(reader)
    
    # Criar novo arquivo com a coluna adicional
    with open('emojis-animais-com-nomes-cientificos.csv', 'w', encoding='utf-8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escrever cabeçalho com nova coluna
        cabecalho = linhas_originais[0] + ['Nome científico']
        writer.writerow(cabecalho)
        
        # Processar cada linha de dados
        for linha in linhas_originais[1:]:
            emoji = linha[0]
            nome_ingles = linha[1].lower()
            nome_portugues = linha[2]
            
            # Buscar nome científico
            nome_cientifico = nomes_cientificos.get(nome_ingles, 'N/A')
            
            # Adicionar nome científico à linha
            nova_linha = linha + [nome_cientifico]
            writer.writerow(nova_linha)
            
            print(f"{emoji} {nome_ingles} -> {nome_cientifico}")
    
    print(f"\nArquivo 'emojis-animais-com-nomes-cientificos.csv' criado com sucesso!")

def atualizar_arquivo_original():
    """Atualiza o arquivo original adicionando a coluna Nome científico"""
    nomes_cientificos = obter_nomes_cientificos()
    
    # Ler arquivo original
    linhas_originais = []
    with open('emojis-animais.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        linhas_originais = list(reader)
    
    # Reescrever o arquivo original com a nova coluna
    with open('emojis-animais.csv', 'w', encoding='utf-8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escrever cabeçalho com nova coluna
        cabecalho = linhas_originais[0] + ['Nome científico']
        writer.writerow(cabecalho)
        
        # Processar cada linha de dados
        for linha in linhas_originais[1:]:
            emoji = linha[0]
            nome_ingles = linha[1].lower()
            nome_portugues = linha[2]
            
            # Buscar nome científico
            nome_cientifico = nomes_cientificos.get(nome_ingles, 'N/A')
            
            # Adicionar nome científico à linha
            nova_linha = linha + [nome_cientifico]
            writer.writerow(nova_linha)
            
            print(f"{emoji} {nome_ingles} -> {nome_cientifico}")
    
    print(f"\nArquivo 'emojis-animais.csv' atualizado com sucesso!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--update-original":
        atualizar_arquivo_original()
    else:
        adicionar_nomes_cientificos()
