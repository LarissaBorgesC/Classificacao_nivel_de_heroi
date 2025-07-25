# 🦸‍♂️ Classificador de Nível de Herói

## Descrição do Projeto

Este projeto consiste em um programa simples que classifica o nível de um herói com base em sua quantidade de experiência (XP). Ele utiliza **variáveis**, **operadores**, **laços de repetição (loops)** e **estruturas de decisão** para determinar o nível e exibir uma mensagem personalizada.

## Funcionalidades

  * **Entrada de Dados**: O programa solicita o **nome** e a **quantidade de XP** do herói.
  * **Classificação de Nível**: Com base na XP fornecida, o herói é classificado em um dos seguintes níveis:
      * **Ferro**: XP menor que 1.000
      * **Bronze**: XP entre 1.001 e 2.000
      * **Prata**: XP entre 2.001 e 5.000
      * **Ouro**: XP entre 5.001 e 7.000
      * **Platina**: XP entre 7.001 e 8.000
      * **Ascendente**: XP entre 8.001 e 9.000
      * **Imortal**: XP entre 9.001 e 10.000
      * **Radiante**: XP maior ou igual a 10.001
  * **Loop de Execução**: O programa utiliza um **loop `while`** para permitir a entrada de múltiplos heróis.
  * **Interrupção de Loop**: Foi implementado um **`break`** para interromper o loop `while` quando uma condição específica é atendida (por exemplo, quando o usuário decide não classificar mais heróis), evitando que o código rode em loop infinito.
  * **Saída Formatada**: A mensagem final é exibida utilizando **f-strings**, garantindo uma saída clara e formatada com o nome do herói e seu nível.

## Como Executar

1.  Certifique-se de ter o Python instalado em sua máquina.
2.  Clone ou baixe o repositório do projeto.
3.  Execute o arquivo principal (por exemplo, `main.py` ou `classificador_heroi.py`) através do terminal:
    ```bash
    python seu_arquivo_aqui.py
    ```
4.  Siga as instruções no console para inserir o nome e a XP do herói.

## Exemplo de Saída

```
O Herói de nome **{nome_do_heroi}** está no nível de **{nivel_do_heroi}**
```
