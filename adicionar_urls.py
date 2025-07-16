#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para adicionar URLs das imagens dos emojis de animais
usando a API do GitHub emojis
"""

import csv
import requests
import json

def buscar_urls_emojis():
    """Busca as URLs dos emojis da API do GitHub"""
    try:
        response = requests.get('https://api.github.com/emojis')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
        return {}

def mapear_emoji_para_nome(emoji_data):
    """Cria um mapeamento reverso de emoji para nome baseado nos dados da API"""
    # Dicionário para mapear emojis específicos para seus nomes na API
    emoji_para_nome = {}
    
    # Alguns mapeamentos específicos que encontramos na API
    mapeamentos_conhecidos = {
        '🐜': 'ant',
        '🦡': 'badger', 
        '🦇': 'bat',
        '🦫': 'beaver',
        '🪲': 'beetle',
        '🐦': 'bird',
        '🦬': 'bison',
        '🐡': 'blowfish',
        '🐃': 'buffalo',
        '🐛': 'bug',
        '🦋': 'butterfly',
        '🐫': 'camel',
        '🐈': 'cat',
        '🐤': 'baby_chick',  # chick -> baby_chick na API
        '🐿️': 'chipmunk',
        '🪳': 'cockroach',
        '🪸': 'coral',
        '🐄': 'cow',
        '🦀': 'crab',
        '🦗': 'cricket',
        '🐊': 'crocodile',
        '🦌': 'deer',
        '🦤': 'dodo',
        '🐕': 'dog',
        '🐬': 'dolphin',
        '🕊️': 'dove',
        '🐪': 'dromedary_camel',  # dromedary -> dromedary_camel
        '🦆': 'duck',
        '🦅': 'eagle',
        '🐘': 'elephant',
        '🐟': 'fish',
        '🦩': 'flamingo',
        '🪰': 'fly',
        '🦒': 'giraffe',
        '🐐': 'goat',
        '🪿': 'goose',
        '🦍': 'gorilla',
        '🦔': 'hedgehog',
        '🦛': 'hippopotamus',
        '🐝': 'honeybee',  # abelha -> honeybee
        '🐎': 'horse',
        '🪼': 'jellyfish',
        '🦘': 'kangaroo',
        '🐞': 'lady_beetle',  # joaninha -> lady_beetle
        '🐆': 'leopard',
        '🦎': 'lizard',
        '🦙': 'llama',
        '🦞': 'lobster',
        '🦣': 'mammoth',
        '🐒': 'monkey',
        '🦟': 'mosquito',
        '🐁': 'mouse',
        '🐙': 'octopus',
        '🦧': 'orangutan',
        '🦦': 'otter',
        '🦉': 'owl',
        '🐂': 'ox',
        '🦜': 'parrot',
        '🦚': 'peacock',
        '🐧': 'penguin',
        '🐖': 'pig',
        '🐩': 'poodle',
        '🐇': 'rabbit',
        '🐏': 'ram',
        '🐀': 'rat',
        '🦏': 'rhinoceros',
        '🐓': 'rooster',
        '🦕': 'sauropod',
        '🦂': 'scorpion',
        '🦭': 'seal',
        '🐑': 'sheep',
        '🦐': 'shrimp',
        '🦨': 'skunk',
        '🦥': 'sloth',
        '🐌': 'snail',
        '🐍': 'snake',
        '🕷️': 'spider',
        '🦑': 'squid',
        '🦢': 'swan',
        '🦖': 't-rex',
        '🐅': 'tiger',
        '🦃': 'turkey',
        '🐢': 'turtle',
        '🪱': 'worm',
        '🐋': 'whale'
    }
    
    return mapeamentos_conhecidos

def processar_csv():
    """Processa o arquivo CSV e adiciona a coluna URL"""
    # Buscar dados da API
    print("Buscando dados da API do GitHub...")
    emoji_data = buscar_urls_emojis()
    
    if not emoji_data:
        print("Erro: Não foi possível obter dados da API")
        return
    
    # Criar mapeamento de emoji para nome
    emoji_para_nome = mapear_emoji_para_nome(emoji_data)
    
    # Ler arquivo original
    linhas_originais = []
    with open('emojis-animais.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        linhas_originais = list(reader)
    
    # Criar arquivo com URLs
    with open('emojis-animais-com-urls.csv', 'w', encoding='utf-8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escrever cabeçalho com nova coluna
        cabecalho = linhas_originais[0] + ['URL']
        writer.writerow(cabecalho)
        
        # Processar cada linha de dados
        for linha in linhas_originais[1:]:
            emoji = linha[0]
            nome_ingles = linha[1].lower()
            
            # Tentar encontrar URL do emoji
            url = ""
            
            # Primeiro, tentar pelo mapeamento direto do emoji
            if emoji in emoji_para_nome:
                nome_api = emoji_para_nome[emoji]
                if nome_api in emoji_data:
                    url = emoji_data[nome_api]
            
            # Se não encontrou, tentar pelo nome em inglês
            if not url and nome_ingles in emoji_data:
                url = emoji_data[nome_ingles]
            
            # Adicionar URL à linha
            nova_linha = linha + [url]
            writer.writerow(nova_linha)
            
            if url:
                print(f"✓ {emoji} ({nome_ingles}) -> {url}")
            else:
                print(f"✗ {emoji} ({nome_ingles}) -> URL não encontrada")
    
    print(f"\nArquivo 'emojis-animais-com-urls.csv' criado com sucesso!")

if __name__ == "__main__":
    processar_csv()
