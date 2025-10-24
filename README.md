# CC8550-ATV10

## Passo a passo para configurar o ambiente Python

1. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    ```

2. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

3. Instale as dependências do `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Como rodar os testes

Para executar os testes, utilize os seguintes comandos:

```bash
python -m pytest -v
```

## Output

```bash
========================================================= test session starts =========================================================
platform linux -- Python 3.12.3, pytest-7.4.3, pluggy-1.6.0 -- /home/baggio/CC8550-ATV10/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.12.3', 'Platform': 'Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39', 'Packages': {'pytest': '7.4.3', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.1.1', 'cov': '4.1.0', 'metadata': '3.1.1'}}
rootdir: /home/baggio/CC8550-ATV10
plugins: html-4.1.1, cov-4.1.0, metadata-3.1.1
collected 42 items                                                                                                                    

exercicio01/tests/test_login.py::test_login_sucesso PASSED                                                                      [  2%]
exercicio01/tests/test_login.py::test_login_user_invalido PASSED                                                                [  4%]
exercicio01/tests/test_login.py::test_login_senha_incorreta PASSED                                                              [  7%]
exercicio01/tests/test_login.py::test_login_campos_vazios PASSED                                                                [  9%]
exercicio01/tests/test_login.py::test_login_mensagem_erro_apropriada PASSED                                                     [ 11%]
exercicio02/tests/test_products_api.py::test_listar_todos_produtos PASSED                                                       [ 14%]
exercicio02/tests/test_products_api.py::test_buscar_produto_por_id PASSED                                                       [ 16%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[electronics] PASSED                                 [ 19%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[jewelery] PASSED                                    [ 21%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[men's clothing] PASSED                              [ 23%]
exercicio02/tests/test_products_api.py::test_filtrar_produtos_por_categoria[women's clothing] PASSED                            [ 26%]
exercicio02/tests/test_products_api.py::test_validar_schema_produtos PASSED                                                     [ 28%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[1] PASSED                                                  [ 30%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[3] PASSED                                                  [ 33%]
exercicio02/tests/test_products_api.py::test_limite_produtos_retorno[5] PASSED                                                  [ 35%]
exercicio03/tests/test_todos_crud.py::test_create_todo_success PASSED                                                           [ 38%]
exercicio03/tests/test_todos_crud.py::test_read_todo PASSED                                                                     [ 40%]
exercicio03/tests/test_todos_crud.py::test_update_todo_patch PASSED                                                             [ 42%]
exercicio03/tests/test_todos_crud.py::test_delete_todo_and_verify PASSED                                                        [ 45%]
exercicio03/tests/test_todos_crud.py::test_create_todo_without_title PASSED                                                     [ 47%]
exercicio04/tests/test_login_pom.py::test_login_sucesso_pom PASSED                                                              [ 50%]
exercicio04/tests/test_login_pom.py::test_login_credenciais_invalidas_pom[usuario_invalido-Password123-Your username is invalid!] PASSED [ 52%]
exercicio04/tests/test_login_pom.py::test_login_credenciais_invalidas_pom[student-senha_errada-Your password is invalid!] PASSED [ 54%]
exercicio04/tests/test_login_pom.py::test_login_campos_vazios_pom PASSED                                                        [ 57%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Python] PASSED                                                 [ 59%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Selenium] PASSED                                               [ 61%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Pytest] PASSED                                                 [ 64%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[API Testing] PASSED                                            [ 66%]
exercicio05/tests/test_busca_parametrizada.py::test_busca_google[Automation] PASSED                                             [ 69%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-arroba.com] PASSED                            [ 71%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@sem-usuario.com] PASSED                          [ 73%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-dominio@] PASSED                              [ 76%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[espacos no meio@teste.com] PASSED                 [ 78%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[caracteres!especiais@teste.com] PASSED            [ 80%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[..pontos@teste.com] PASSED                        [ 83%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[teste@] PASSED                                    [ 85%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@teste.com] PASSED                                [ 88%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[123-muito curta] PASSED                               [ 90%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[semNumero-sem n\xfamero] PASSED                       [ 92%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[semmaiuscula123-sem mai\xfascula] PASSED              [ 95%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[12345678-s\xf3 n\xfameros] PASSED                     [ 97%]
exercicio05/tests/test_validacoes_parametrizadas.py::test_validacao_senha[ab-muito curta] PASSED                                [100%]

========================================================= 42 passed in 52.63s =================================================== ~53s
```
