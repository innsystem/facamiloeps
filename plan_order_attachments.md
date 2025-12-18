Recurso: Anexos de Pedido (Admin e Catálogo)
Versão: OpenCart 3.x
Objetivo: O recurso que quero implementar basicamente é permitir que o Admin anexe arquivos ao pedido em questão. Acredito que o sistema deverá criar uma nova tabela order_attachments order_id e path para armazenar o id do pedido e o caminho ao arquivo que ficaria armazenado na pasta image/catalog/order_attachments/{order_id}/file.* 
Na página de detalhes do pedido e na página de listagem de pedido deverá ter um botão de ação que permitiria anexar um ou mais arquivos, ao clicar abriria uma modal criativa para abrir a seleção de arquivos e exibir quais foram selecionados e assim que o usuário confirmar o envio é feito o upload e armazenamento no sistema e tendo o sucesso a página se atualiza exibindo acesso aos arquivos anexados ao pedido em questão.

O mesmo deverá ser feito do lado do catalogo que é onde os clientes da loja podem ver seus pedidos e incluindo acesso aos arquivos anexados (o cliente não pode fazer upload, apenas o admin).

* Ponto importante, todas as URLs precisam ser autenticadas usando o {{ user_token }} garanta o uso correto seguindo os padrões da opencart.

1. 📁 BANCO DE DADOS
1.1. Criar tabela order_attachment

CREATE TABLE `oc_order_attachment` (
  `order_attachment_id` INT(11) NOT NULL AUTO_INCREMENT,
  `order_id` INT(11) NOT NULL,
  `filename` VARCHAR(255) NOT NULL,
  `path` TEXT NOT NULL,
  `date_added` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_attachment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
2. 📂 ESTRUTURA DE ARQUIVOS

admin/
├── controller/sale/order_attachment.php
├── language/pt-br/sale/order_attachment.php
├── model/sale/order_attachment.php
└── view/template/sale/order_attachment_modal.twig

catalog/
├── controller/account/order_attachment.php
├── language/pt-br/account/order_attachment.php
├── model/account/order_attachment.php
└── view/template/account/order_attachment_list.twig

image/
└── catalog/order_attachments/{order_id}/file.*
3. 🔐 PERMISSÕES ADMIN
Acesse System > Users > User Groups e habilite:

Access: sale/order_attachment

Modify: sale/order_attachment

4. 🔧 BACK-END ADMIN
4.1. Controller: admin/controller/sale/order_attachment.php
upload() – Upload de múltiplos arquivos via AJAX

getAttachments() – Lista os anexos existentes de um pedido

deleteAttachment() – (Opcional) Excluir arquivos

4.2. Model: admin/model/sale/order_attachment.php
addAttachment($order_id, $filename, $path)

getAttachments($order_id)

deleteAttachment($order_attachment_id)

sendNotification ($order_id) - Notificação automática por e-mail quando um anexo for incluído

5. 📜 VIEW ADMIN
5.1. Arquivo: view/template/sale/order_info.twig
Inserir na visualização do pedido (ex: abaixo dos produtos ou histórico):



<button id="btn-attachments" data-order-id="{{ order_id }}">Anexar Arquivos</button>
<div id="order-attachment-container"></div>
5.2. Modal via Twig + JS (ex: order_attachment_modal.twig)
Input de múltiplos arquivos

Preview dos arquivos selecionados

Botão de envio via AJAX

Exibe arquivos anexados após envio

6. 🧠 JAVASCRIPT
AJAX para upload: admin/index.php?route=sale/order_attachment/upload&token=...

Atualizar listagem após upload com chamada para getAttachments

Recomendo usar Dropzone.js ou FilePond para UX moderna e visual criativo.

7. 📂 CATÁLOGO (FRONTEND)
7.1. Controller: catalog/controller/account/order_attachment.php
index() – Lista de arquivos por pedido

7.2. Model: catalog/model/account/order_attachment.php
getAttachments($order_id, $customer_id) – Validação por cliente

7.3. View: view/template/account/order_attachment_list.twig
Incluir em account/order_info.twig ou criar uma aba nova:



<h4>Anexos do Pedido</h4>
<ul>
  {% for file in attachments %}
    <li><a href="{{ file.url }}" target="_blank">{{ file.filename }}</a></li>
  {% endfor %}
</ul>
8. 📁 ARMAZENAMENTO
Ao fazer upload:

Criar pasta se não existir: image/catalog/order_attachments/{order_id}/

Salvar arquivos como: original_nome.ext

Registrar order_id, filename, e path no banco

9. 🔐 SEGURANÇA
Validar extensão e tamanho do arquivo (permitir: PDF, DOCX, JPG, PNG)

Verificar customer_id em catalog antes de listar anexos

Proteger diretório via .htaccess ou validar acesso via PHP