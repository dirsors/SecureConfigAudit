# SecureConfigAudit

## Descrição

O **SecureConfigAudit** é uma ferramenta de linha de comando (CLI) desenvolvida em Python para realizar auditorias básicas de segurança em sistemas Linux. Seu objetivo é identificar configurações potencialmente inseguras e apresentar um relatório simples que auxilie administradores e usuários na identificação de riscos.

Este projeto foi desenvolvido como artefato para a disciplina de Cibersegurança, utilizando Inteligência Artificial como apoio ao processo de desenvolvimento.

## Problema

Configurações inadequadas em sistemas Linux podem aumentar a superfície de ataque e comprometer a segurança do ambiente. Muitos desses problemas podem ser identificados por meio de verificações automatizadas.

O SecureConfigAudit busca automatizar esse processo, fornecendo uma análise inicial das configurações mais relevantes do sistema.

## Objetivo

Desenvolver uma ferramenta CLI em Python capaz de realizar verificações de segurança em sistemas Linux e apresentar um relatório indicando possíveis vulnerabilidades ou configurações inadequadas.

## Escopo Inicial

Na primeira versão, a ferramenta deverá realizar as seguintes verificações:

* Verificar se o login do usuário **root** via SSH está habilitado.
* Verificar se a autenticação por senha no SSH está habilitada.
* Verificar as permissões dos arquivos `/etc/passwd` e `/etc/shadow`.
* Identificar arquivos com permissão `777` em diretórios definidos pelo usuário.
* Verificar se o firewall do sistema está ativo.

Novas verificações poderão ser adicionadas em versões futuras.

## Tecnologias

* Python 3
* Interface de linha de comando (CLI)
* Sistema Operacional Linux

## Estrutura Inicial do Projeto

```text
SecureConfigAudit/
├── README.md
├── requirements.txt
├── audit.py
├── checks/
├── reports/
├── tests/
└── docs/
```

## Situação do Projeto

Este repositório encontra-se em fase inicial de desenvolvimento. A implementação será realizada de forma incremental, com validação contínua das funcionalidades e documentação da evolução do projeto.
