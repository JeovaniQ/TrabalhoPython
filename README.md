# Sistema de Loja Virtual

## Explicação do Código

### Classes de Exceção

O código começa com a definição de três exceções personalizadas:

- `ProdutoInexistenteError`: Utilizada quando se tenta aceder a um produto que não existe no catálogo
- `SaldoInsuficienteError`: Acionada quando o utilizador tenta fazer uma compra sem saldo suficiente
- `EstoqueInsuficienteError`: Lançada quando a quantidade solicitada excede o stock disponível

### Classe LojaVirtual

A classe `LojaVirtual` implementa a funcionalidade principal do sistema:

#### Inicialização

O método `__init__` configura:
- Um catálogo de produtos com preços e quantidades em stock
- Um carrinho de compras vazio
- Um saldo inicial de €200.00
- Um histórico de compras vazio

#### Métodos de Visualização

- `listar_produtos`: Exibe uma tabela formatada com todos os produtos, preços e quantidades em stock
- `verificar_carrinho`: Mostra os produtos no carrinho, quantidades, preços unitários, subtotais e o total geral
- `mostrar_saldo`: Apresenta o saldo atual do utilizador
- `mostrar_historico`: Exibe uma lista de todas as compras anteriores e os produtos adquiridos

#### Métodos de Gestão do Carrinho

- `adicionar_ao_carrinho`: Adiciona um produto ao carrinho, verificando:
  - Se o produto existe no catálogo
  - Se a quantidade solicitada é válida
  - Se há stock suficiente
  - Atualiza o stock disponível após adicionar ao carrinho

- `remover_do_carrinho`: Remove produtos do carrinho, permitindo remover uma quantidade específica ou todo o produto
  - Devolve os produtos removidos ao stock disponível

- `calcular_total`: Calcula o valor total dos produtos no carrinho

#### Métodos de Gestão Financeira

- `adicionar_saldo`: Aumenta o saldo do utilizador, verificando se o valor é positivo
- `simular_pagamento`: Processa a compra:
  - Verifica se o carrinho não está vazio
  - Confirma se há saldo suficiente
  - Regista a compra no histórico
  - Deduz o valor do saldo
  - Limpa o carrinho após a compra bem-sucedida

#### Método Principal

- `executar`: Inicia o loop principal da aplicação:
  - Apresenta um menu com 9 opções (0-8)
  - Processa a escolha do utilizador
  - Implementa uma interface de utilizador baseada em texto
  - Captura e trata erros para garantir que a aplicação não fecha inesperadamente

### Fluxo de Execução

O código utiliza um padrão consistente de try-except-else-finally para tratar erros em cada operação:
1. Tenta executar a operação desejada
2. Captura e exibe mensagens de erro específicas quando ocorrem problemas
3. Executa código adicional em caso de sucesso no bloco else
4. Finaliza com mensagens de conclusão no bloco finally

Por fim, a condição `if __name__ == "__main__"` garante que a aplicação é iniciada automaticamente apenas quando o script é executado diretamente, e não quando importado como módulo.
