# Relatório do Laboratório 10

## Exercício 1 - Teste de Login (Web)
Os cenários em `exercicio01/tests/test_login.py` reutilizam a fixture `open_login_page`, que abre o formulário de login com um `chrome_driver` headless configurado em `conftest.py`. O objetivo é validar respostas positivas e negativas do fluxo de autenticação.
- `test_login_sucesso`: confirma o login com `student/Password123`, verificando a mensagem “Logged In Successfully”.
- `test_login_user_invalido`: envia um usuário inexistente e aguarda o banner com “Your username is invalid!”.
- `test_login_senha_incorreta`: mantém o usuário correto, troca apenas a senha e espera pela mensagem “Your password is invalid!”.
- `test_login_campos_vazios`: tenta submeter sem preencher campos e checa o alerta exibido.
- `test_login_mensagem_erro_apropriada`: preenche credenciais totalmente inválidas e garante que o erro de usuário inválido aparece.

## Exercício 2 - API de Produtos (REST)
Os testes em `exercicio02/tests/test_products_api.py` compartilham uma sessão HTTP (`requests.Session`) para reduzir overhead de rede contra a Fake Store API.
- `test_listar_todos_produtos`: garante resposta `200`, retorno em lista e presença dos campos principais no primeiro item.
- `test_buscar_produto_por_id`: consulta o produto `1` e valida identificação, título e categoria permitida.
- `test_filtrar_produtos_por_categoria`: parametriza as quatro categorias oficiais e verifica que cada item retornado pertence à categoria solicitada.
- `test_validar_schema_produtos`: valida cada produto com um schema JSON declarativo, colecionando possíveis violações.
- `test_limite_produtos_retorno`: envia o parâmetro `limit` (1, 3, 5) e confirma que o número de itens na resposta respeita o limite.

## Exercício 3 - Teste CRUD Completo (REST)
O arquivo `exercicio03/tests/test_todos_crud.py` usa uma sessão compartilhada e a fixture `todo`, que cria um registro na JSONPlaceholder e executa `DELETE` no teardown para limpeza.
- `test_create_todo_success`: verifica que a criação básica retorna título, status e `userId` esperados, além de um `id`.
- `test_read_todo`: acessa `/todos/1` e confirma status `200` e presença dos campos padrão.
- `test_update_todo_patch`: cria um TODO auxiliar, aplica `PATCH` para marcar como concluído e valida o campo `completed`.
- `test_delete_todo_and_verify`: executa `DELETE` seguido de `GET`, aceitando tanto `404` quanto `{}` como evidência de remoção.
- `test_create_todo_without_title`: força a criação sem título e aceita respostas de erro ou ausência do campo no retorno, cobrindo cenário inválido.

## Exercício 4 - Page Object Model (Web)
O módulo `pages` introduz uma camada POM: `base_page.py` centraliza waits e interações; `login_page.py` encapsula o formulário com métodos `abrir`, `fazer_login`, getters de erro; `dashboard_page.py` identifica o título de sucesso e mensagem de boas-vindas. Os testes em `exercicio04/tests/test_login_pom.py` utilizam esses objetos.
- `test_login_sucesso_pom`: autentica com credenciais válidas, instancia `DashboardPage` e confirma usuário logado pela presença da mensagem de sucesso.
- `test_login_credenciais_invalidas_pom`: parametriza variações de usuário e senha incorretos, conferindo visibilidade do alerta e texto retornado.
- `test_login_campos_vazios_pom`: dispara o envio sem preencher campos e assegura a mensagem de usuário inválido.

## Exercício 5 - Testes Parametrizados (REST + Web)
Os testes REST em `exercicio05/tests/test_validacoes_parametrizadas.py` adicionam um cabeçalho `x-api-key` e exploram matrizes de dados com `pytest.mark.parametrize`. Já `exercicio05/tests/test_busca_parametrizada.py` reutiliza o `chrome_driver` headless para validar buscas na Wikipedia.
- `test_validacao_email_api`: percorre a lista de e-mails inválidos e confirma que a API de registro retorna `400`.
- `test_validacao_senha`: envia senhas enfraquecidas com rótulos descritivos e valida a rejeição com status `400`.
- `test_busca_google`: visita `https://www.wikipedia.org`, preenche o campo de busca para cada termo e confirma que o título da página retornada contém o termo pesquisado.

## Execução dos Testes
Comando executado: `source venv/bin/activate && pytest -v`
```text
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.3, pluggy-1.6.0 -- /home/baggio/CC8550-ATV10/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.12.3', 'Platform': 'Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39', 'Packages': {'pytest': '7.4.3', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.1.1', 'cov': '4.1.0', 'metadata': '3.1.1'}}
rootdir: /home/baggio/CC8550-ATV10
plugins: html-4.1.1, cov-4.1.0, metadata-3.1.1
collecting ... collected 42 items

exercicio01/tests/test_login.py::test_login_sucesso PASSED               [  2%]
exercicio01/tests/test_login.py::test_login_user_invalido PASSED         [  4%]
exercicio01/tests/test_login.py::test_login_senha_incorreta PASSED       [  7%]
exercicio01/tests/test_login.py::test_login_campos_vazios PASSED         [  9%]
exercicio01/tests/test_login.py::test_login_mensagem_erro_apropriada PASSED [ 11%]
exercicio02/tests/test_products_api.py::test_listar_todos_produtos PASSED [ 14%]
exercicio02/tests/test_products_api.py::test_buscar_produto_por_id PASSED [ 16%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[electronics] PASSED [ 19%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[jewelery] PASSED [ 21%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[men's clothing] PASSED [ 23%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[women's clothing] PASSED [ 26%]
exercicio02/tests/test_products_api.py::test_validar_schema_produtos PASSED [ 28%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[1] PASSED [ 30%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[3] PASSED [ 33%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[5] PASSED [ 35%]
exercicio03/tests/test_todos_crud.py::test_create_todo_success PASSED    [ 38%]
exercicio03/tests/test_todos_crud.py::test_read_todo PASSED              [ 40%]
exercicio03/tests/test_todos_crud.py::test_update_todo_patch PASSED      [ 42%]
exercicio03/tests/test_todos_crud.py::test_delete_todo_and_verify PASSED [ 45%]
exercicio03/tests/test_todos_crud.py::test_create_todo_without_title PASSED [ 47%]
exercicio04/tests/test_login_pom.py::test_login_sucesso_pom PASSED       [ 50%]
exercicio04/tests/test_login_pom.py::test_login_credenciais_invalidas_pom[usuario_invalido-Password123-Your username is invalid!] PASSED [ 52%]
exercicio04/tests/test_login_pom.py::test_login_credenciais_invalidas_pom[student-senha_errada-Your password is invalid!] PASSED [ 54%]
exercicio04/tests/test_login_pom.py::test_login_campos_vazios_pom PASSED [ 57%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Python] PASSED [ 59%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Selenium] PASSED [ 61%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Pytest] PASSED [ 64%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[API Testing] PASSED [ 66%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Automation] PASSED [ 69%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-arroba.com] PASSED [ 71%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@sem-usuario.com] PASSED [ 73%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-dominio@] PASSED [ 76%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[espacos no meio@teste.com] PASSED [ 78%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[caracteres!especiais@teste.com] PASSED [ 80%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[..pontos@teste.com] PASSED [ 83%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[teste@] PASSED [ 85%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@teste.com] PASSED [ 88%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[123-muito curta] PASSED [ 90%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[semNumero-sem n\xfamero] PASSED [ 92%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[semmaiuscula123-sem mai\xfascula] PASSED [ 95%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[12345678-s\xf3 n\xfameros] PASSED [ 97%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[ab-muito curta] PASSED [100%]

============================= 42 passed in 49.20s ==============================
```
Todos os 42 testes passaram, confirmando que os cenários web e REST deste laboratório executam com sucesso no ambiente virtual configurado.
