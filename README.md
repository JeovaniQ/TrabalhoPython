# TrabalhoPython

# Sistema de Loja Virtual

## Descrição
Este sistema simula uma loja virtual no terminal com foco no tratamento de erros,
aplicando estruturas try, except, else, finally e exceções personalizadas.

## Funcionalidades
- Visualização de produtos disponíveis com nome, preço e stock
- Adição de produtos ao carrinho
- Verificação do carrinho
- Remoção de produtos do carrinho
- Visualização e adição de saldo
- Simulação de pagamento
- Histórico de compras

## Exceções Tratadas

### Exceções Personalizadas
1. **ProdutoInexistenteError**
   - Lançada quando o utilizador tenta adicionar um produto que não existe no catálogo
   - Tratada no método `adicionar_ao_carrinho`

2. **SaldoInsuficienteError**
   - Lançada quando o utilizador tenta realizar uma compra com saldo insuficiente
   - Tratada no método `simular_pagamento`

3. **EstoqueInsuficienteError**
   - Lançada quando o utilizador tenta adicionar ao carrinho mais unidades do que há em stock
   - Tratada no método `adicionar_ao_carrinho`

### Exceções Padrão do Python
1. **ValueError**
   - Tratada em vários métodos para validar entradas numéricas (quantidade, saldo)
   - Verifica valores negativos ou zero em campos que exigem valores positivos
   - Também usada quando um produto não é encontrado no carrinho

2. **Exception (genérica)**
   - Captura erros inesperados no ciclo principal para evitar que o programa termine abruptamente

## Estruturas de Tratamento de Erros
- **try/except**: Usado em todos os métodos que podem gerar exceções
- **else**: Implementado para executar código apenas quando nenhuma exceção é lançada
- **finally**: Usado para garantir que uma mensagem de finalização seja exibida, independente de exceções
