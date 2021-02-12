# Robios: Triagem de Covid-19 

## Objetivo

Este projeto foi feito para servir como aplicação de triagem de Covid-19 para o Robios, utilizando a linguagem Python e o protocolo MQTT.

## Instalação

Para executar o projeto, é necessário instalar o pacote paho-mqtt:
```
pip install paho-mqtt
```
Após a instalação do pacote, execute main.py utilizando Python 3

## Funcionalidades

O projeto foi feito para ser escalável e atendendo aos princípios SOLID quando possível. 
Portanto, ainda que a quantidade limitada de funcionalidades seja pequena e certos métodos pareçam redundantes, 
a exemplo dos métodos de introdução, tais métodos foram criados propositalmente para facilitar a manutenção e adição de funcionalidades e regras. 

Para melhor organização, a documentação necessária para compreender os métodos e parâmetros está presente no código. 
No entanto, podemos mencionar algumas funcionalidades previamente, são elas


- Modo de identificação  
(Main.__log_user = False)
```
On: A triagem coleta dados de identificação, como nome e CPF.
Off: A triagem é feita independente de dados de identificação.
Pensado para possível expansão em lojas de franquias, centros comerciais, entre outros.  
O formulário de dados pessoais é escalável e suas regras são definidas por meio de um arquivo .json  
```
- Triagem rápida  
(ScreeningController.fast = False)
```
On: O preenchimento do formulário é interrompido a qualquer momento ao identificar a possibilidade de infecção.
Off: O preenchimento do formulário é feito até o final em todos os casos, com verificação posterior.
```
- JSON Forms Settings
```
Todos os campos de formulário estão presentes em um arquivo JSON padronizável e escalável.  
O formulário está disponível em português até o momento. No entando, sua padronização prevê o suporte a multiplas linguas.
```
