import os
import json
import requests

def extract_media_urls_from_har(har_file_path):
    # Lista para armazenar URLs de imagens e vídeos
    images = []
    videos = []

    # Abre e lê o conteúdo do arquivo HAR
    with open(har_file_path, 'r', encoding='utf-8') as file:
        har_data = json.load(file)
    
    # Percorre todas as entradas no arquivo HAR
    for entry in har_data['log']['entries']:
        # Obtém o URL da solicitação
        url = entry['request']['url']
        # Obtém o tipo de mídia da resposta, se disponível
        mime_type = entry['response']['content'].get('mimeType', '')

        # Verifica se é uma imagem ou vídeo com base no MIME type
        if 'image' in mime_type:
            images.append(url)
        elif 'video' in mime_type:
            videos.append(url)
    
    return images, videos

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

# Caminho para o arquivo HAR
har_file_path = 'diablo4.blizzard.com.har'

# Extrai URLs de imagens e vídeos do arquivo HAR
images, videos = extract_media_urls_from_har(har_file_path)

# Pasta onde os arquivos serão salvos
download_folder = 'midia_har'

# Cria a pasta se ela não existir
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Baixa todas as imagens
print("Baixando imagens...")
for img_url in images:
    download_file(img_url, download_folder)

# Baixa todos os vídeos
print("\nBaixando vídeos...")
for video_url in videos:
    download_file(video_url, download_folder)
