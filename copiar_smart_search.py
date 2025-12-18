import os
import shutil

# Lista de arquivos e pastas a serem copiados
itens = [
    r'C:/laragon/www/loja_marchipapelaria/admin/controller/extension/module/smart_search.php',
    r'C:\laragon\www\loja_marchipapelaria\admin\language\pt-br\extension\module\smart_search.php',
    r'C:\laragon\www\loja_marchipapelaria\admin\view\template\extension\module\smart_search.twig',
    r'C:\laragon\www\loja_marchipapelaria\catalog\view\javascript\smart_search.js',
    r'C:\laragon\www\loja_marchipapelaria\catalog\controller\extension\module\smart_search.php',
    r'C:\laragon\www\loja_marchipapelaria\catalog\language\pt-br\extension\module\smart_search.php',
    r'C:\laragon\www\loja_marchipapelaria\catalog\model\extension\module\smart_search.php',
    r'C:\laragon\www\loja_marchipapelaria\catalog\view\theme\default\template\extension\module\smart_search.twig',
]

origem_base = r'C:/laragon/www/loja_marchipapelaria'
destino_base = r'D:/Backup dos Arquivos/Empresa/Projetos/Loja Virtual/OC3/Extensões Premiums/smart_search.ocmod/upload'

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