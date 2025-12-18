import os
import shutil

# Lista de arquivos e pastas a serem copiados
itens = [
    r'C:/laragon/www/loja_marchipapelaria/admin/controller/extension/module/whatsapp_api.php',
    r'C:/laragon/www/loja_marchipapelaria/admin/language/pt-br/extension/module/whatsapp_api.php',
    r'C:/laragon/www/loja_marchipapelaria/admin/model/extension/module/whatsapp_api.php',
    r'C:/laragon/www/loja_marchipapelaria/admin/view/template/extension/module/whatsapp_api.twig',
    r'C:/laragon/www/loja_marchipapelaria/admin/view/template/extension/module/whatsapp_api_template_form.twig',
    r'C:/laragon/www/loja_marchipapelaria/admin/view/template/extension/module/whatsapp_api_templates.twig',
    r'C:/laragon/www/loja_marchipapelaria/catalog/controller/extension/module/whatsapp_api.php',
    r'C:/laragon/www/loja_marchipapelaria/catalog/model/extension/module/whatsapp_api.php',
    r'C:/laragon/www/loja_marchipapelaria/catalog/view/javascript/intl-tel-input',
    r'C:/laragon/www/loja_marchipapelaria/catalog/view/javascript/sweetalert',
]

origem_base = r'C:/laragon/www/loja_marchipapelaria'
destino_base = r'D:/Backup dos Arquivos/Empresa/Projetos/Loja Virtual/OC3/Extensões Premiums/whatsapp_api.ocmod/upload'

for item in itens:
    caminho_relativo = os.path.relpath(item, origem_base)
    destino = os.path.join(destino_base, caminho_relativo)
    if os.path.isdir(item):
        print(f'Copiando pasta: {item} -> {destino}')
        shutil.copytree(item, destino, dirs_exist_ok=True)
    else:
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        print(f'Copiando arquivo: {item} -> {destino}')
        shutil.copy2(item, destino)

print('Cópia concluída!') 