# Exercício 5

### Executar:

1. Configure seu ambiente virtual

2. Execute os testes

```
pytest tests/ -v --cov=. --cov-report=html
```

### Relatório HTML

O relatório HTML está disponível na pasta [./htmlcov](./htmlcov/)

### Logs

```
❯ pytest tests/ -v --cov=. --cov-report=html
================================================================= test session starts =================================================================
platform darwin -- Python 3.11.9, pytest-7.4.3, pluggy-1.6.0 -- /Users/enzobozzani/.pyenv/versions/3.11.9/envs/atv10-ex5/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.11.9', 'Platform': 'macOS-26.0.1-arm64-arm-64bit', 'Packages': {'pytest': '7.4.3', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'cov': '7.0.0'}}
rootdir: /Users/enzobozzani/College/atv10
plugins: html-4.1.1, metadata-3.1.1, cov-7.0.0
collected 18 items

tests/test_busca_parametrizada.py::test_busca_google[Python] PASSED                                                                             [  5%]
tests/test_busca_parametrizada.py::test_busca_google[Selenium] PASSED                                                                           [ 11%]
tests/test_busca_parametrizada.py::test_busca_google[Pytest] PASSED                                                                             [ 16%]
tests/test_busca_parametrizada.py::test_busca_google[API Testing] PASSED                                                                        [ 22%]
tests/test_busca_parametrizada.py::test_busca_google[Automation] PASSED                                                                         [ 27%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-arroba.com] PASSED                                                        [ 33%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@sem-usuario.com] PASSED                                                      [ 38%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[sem-dominio@] PASSED                                                          [ 44%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[espacos no meio@teste.com] PASSED                                             [ 50%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[caracteres!especiais@teste.com] PASSED                                        [ 55%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[..pontos@teste.com] PASSED                                                    [ 61%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[teste@] PASSED                                                                [ 66%]
tests/test_validacoes_parametrizadas.py::test_validacao_email_api[@teste.com] PASSED                                                            [ 72%]
tests/test_validacoes_parametrizadas.py::test_validacao_senha[123-muito curta] PASSED                                                           [ 77%]
tests/test_validacoes_parametrizadas.py::test_validacao_senha[semNumero-sem n\xfamero] PASSED                                                   [ 83%]
tests/test_validacoes_parametrizadas.py::test_validacao_senha[semmaiuscula123-sem mai\xfascula] PASSED                                          [ 88%]
tests/test_validacoes_parametrizadas.py::test_validacao_senha[12345678-s\xf3 n\xfameros] PASSED                                                 [ 94%]
tests/test_validacoes_parametrizadas.py::test_validacao_senha[ab-muito curta] PASSED                                                            [100%]

=================================================================== tests coverage ====================================================================
__________________________________________________ coverage: platform darwin, python 3.11.9-final-0 ___________________________________________________

Coverage HTML written to dir htmlcov
================================================================= 18 passed in 30.88s =================================================================
```
