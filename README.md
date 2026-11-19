# TorcidaNet - Painel do Mesário

Aplicação desktop feita em Python com Tkinter para registrar gols e cartões dos Times A e B durante uma partida.

## Funcionalidades

- Atualização do placar em tempo real
- Registro de cartões amarelos e vermelhos
- Painel de status do último evento
- Interface gráfica simples para uso pelo mesário

## Pré-requisitos

- Python 3
- Tkinter (geralmente incluído nas instalações padrão do Python)
- Pillow

## Como executar

Para apresentar no Chrome ou Edge, abra o arquivo [index.html](./index.html).
Você também pode iniciar um servidor local:

```bash
python -m http.server 8000
```

Depois, acesse `http://localhost:8000`.

O acesso de demonstração é:

- Usuário: `admin`
- Senha: `1234`

## Estrutura do projeto

```text
trabalho.py       Aplicação principal
imagem/image.png  Imagem utilizada no projeto
README.md         Documentação do projeto
.gitignore        Arquivos ignorados pelo Git
```
