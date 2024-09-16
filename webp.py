import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def fetch_webp_images(url):
    # Realiza a requisição para a página
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Falha ao acessar a página. Status code: {response.status_code}")
        return []

    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Recupera todas as URLs .webp
    webp_images = []

    # Procura em todas as tags com atributo 'src'
    for tag in soup.find_all(src=True):
        img_url = tag.get('src')
        if img_url and img_url.endswith('.webp'):
            # Constrói a URL completa e adiciona à lista
            full_img_url = urljoin(url, img_url)
            webp_images.append(full_img_url)

    # Procura em todas as tags com atributo 'style' contendo URLs .webp
    for tag in soup.find_all(style=True):
        style_content = tag.get('style')
        # Expressão regular para encontrar todas as URLs .webp nos estilos
        webp_urls_in_style = re.findall(r'url\((.*?)\)', style_content)
        for img_url in webp_urls_in_style:
            if img_url.endswith('.webp'):
                full_img_url = urljoin(url, img_url.strip('\'"'))  # Remove aspas se houver
                webp_images.append(full_img_url)

    return webp_images

def download_file(url, folder):
    try:
        # Faz o download do conteúdo da URL
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True)
        
        # Se a resposta for bem-sucedida
        if response.status_code == 200:
            # Extrai o nome do arquivo da URL
            filename = os.path.join(folder, url.split('/')[-1])
            
            # Salva o arquivo na pasta especificada
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Arquivo salvo: {filename}")
        else:
            print(f"Falha ao baixar o arquivo: {url}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

# URL da página a ser analisada
url = "https://diablo4.blizzard.com/pt-br/"

# Extrai URLs de imagens .webp da página
webp_images = fetch_webp_images(url)

# Pasta onde os arquivos serão salvos
download_folder = 'webp_images'

# Cria a pasta se ela não existir
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Baixa todas as imagens .webp
print("Baixando imagens .webp...")
for img_url in webp_images:
    download_file(img_url, download_folder)
