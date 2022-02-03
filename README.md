# Formação em Teste de Software - Blazedemo
Projeto criado para acompanhar as aulas do curso [Formação em Teste de Software][Iterasys] em **Python** utilizando **Selenium**.

Neste projeto é possível rodar testes **web** localmente.

Ele foi criado para treinamento em **BDD** utilizando o **Behave**.

---

### Pré-Requisitos
- Instalar as seguintes Bibliotecas no pip:

```
selenium
behave
pytest
```

- URL utilizada para os testes: https://www.blazedemo.com/
- É necessário que o `chromedriver` esteja neste local `C:/webdrivers/chromedriver/{versão}/chromedriver.exe`
- Alterar a `{versão}` conforme o utilizado, e modificar o arquivo `environment.py` para a versão correta

---

### Glossário

`features` Diretório para alocação dos arquivos .feature com a descrição dos testes em BDD.

`environment.py` Tudo que será executado antes e depois do teste.

`features/steps` Código do passo a passo do BDD, utilizando Selenium.

`helpers` Diretório não utilizado, pode ser ignorado.

`lista10` Exercício para treinar o BDD com a função de Cadastro do mesmo site.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/
[Saucelabs]: https://saucelabs.com/
[MyDemoApp]: https://github.com/saucelabs/my-demo-app-rn/releases

<!-- imagens -->
[QANinja-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)