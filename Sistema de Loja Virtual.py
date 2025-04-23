class ProdutoInexistenteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class EstoqueInsuficienteError(Exception):
    pass


class LojaVirtual:
    def __init__(self):
        self.produtos = {
            "Camisola": {"preco": 50.00, "estoque": 10},
            "Calças": {"preco": 100.00, "estoque": 5},
            "Sapatos": {"preco": 150.00, "estoque": 3},
            "Boné": {"preco": 30.00, "estoque": 15},
            "Meias": {"preco": 15.00, "estoque": 20}
        }
        self.carrinho = []
        self.saldo = 200.00
        self.historico_compras = []

    def listar_produtos(self):
        print("\n" + "="*50)
        print("PRODUTOS DISPONÍVEIS:")
        print("="*50)
        print(f"{'Produto':<15} {'Preço (€)':<15} {'Stock':<10}")
        print("-"*50)
        for produto, info in self.produtos.items():
            print(f"{produto:<15} €{info['preco']:<13.2f} {info['estoque']:<10}")
        print("="*50)

    def verificar_carrinho(self):
        if not self.carrinho:
            print("\nCarrinho vazio.")
            return
        
        print("\n" + "="*50)
        print("O SEU CARRINHO:")
        print("="*50)
        print(f"{'Produto':<15} {'Qtd':<5} {'Preço Unit.':<15} {'Subtotal':<10}")
        print("-"*50)
        
        for produto, quantidade in self.carrinho:
            preco = self.produtos[produto]["preco"]
            subtotal = preco * quantidade
            print(f"{produto:<15} {quantidade:<5} €{preco:<13.2f} €{subtotal:.2f}")
        
        print("-"*50)
        print(f"Total: €{self.calcular_total():.2f}")
        print("="*50)

    def adicionar_ao_carrinho(self, produto, quantidade):
        try:
            if produto not in self.produtos:
                raise ProdutoInexistenteError(f"Produto '{produto}' não encontrado no catálogo.")
            
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            
            estoque_disponivel = self.produtos[produto]["estoque"]
            if quantidade > estoque_disponivel:
                raise EstoqueInsuficienteError(f"Stock insuficiente. Disponível: {estoque_disponivel}")
            
            # Verifica se o produto já está no carrinho
            for i, (prod, qtd) in enumerate(self.carrinho):
                if prod == produto:
                    self.carrinho[i] = (produto, qtd + quantidade)
                    break
            else:
                self.carrinho.append((produto, quantidade))
            
            # Atualiza o estoque
            self.produtos[produto]["estoque"] -= quantidade
            
        except ProdutoInexistenteError as e:
            print(f"\nERRO: {e}")
        except ValueError as e:
            print(f"\nERRO: {e}")
        except EstoqueInsuficienteError as e:
            print(f"\nERRO: {e}")
        else:
            print(f"\nSUCESSO: {quantidade} unidade(s) de {produto} adicionado ao carrinho.")
        finally:
            print("Operação de adição ao carrinho finalizada.")

    def remover_do_carrinho(self, produto, quantidade=None):
        try:
            # Verifica se o produto está no carrinho
            for i, (prod, qtd) in enumerate(self.carrinho):
                if prod == produto:
                    # Se quantidade não especificada ou maior/igual à quantidade no carrinho, remove todo o item
                    if quantidade is None or quantidade >= qtd:
                        removido = qtd
                        self.produtos[produto]["estoque"] += qtd
                        self.carrinho.pop(i)
                    else:
                        removido = quantidade
                        self.produtos[produto]["estoque"] += quantidade
                        self.carrinho[i] = (produto, qtd - quantidade)
                    
                    print(f"\nSUCESSO: {removido} unidade(s) de {produto} removido do carrinho.")
                    return
            
            raise ValueError(f"Produto '{produto}' não encontrado no carrinho.")
        
        except ValueError as e:
            print(f"\nERRO: {e}")
        finally:
            print("Operação de remoção do carrinho finalizada.")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.carrinho:
            total += self.produtos[produto]["preco"] * quantidade
        return total

    def adicionar_saldo(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")
            
            self.saldo += valor
            
        except ValueError as e:
            print(f"\nERRO: {e}")
        else:
            print(f"\nSUCESSO: Saldo adicionado. Novo saldo: €{self.saldo:.2f}")
        finally:
            print("Operação de adição de saldo finalizada.")

    def simular_pagamento(self):
        try:
            total = self.calcular_total()
            
            if total == 0:
                raise ValueError("Carrinho vazio. Adicione produtos antes de pagar.")
            
            if total > self.saldo:
                raise SaldoInsuficienteError(f"Saldo insuficiente para realizar a compra. Faltam €{total - self.saldo:.2f}")
            
            # Copia os itens do carrinho para o histórico
            compra_atual = {"itens": self.carrinho.copy(), "total": total}
            self.historico_compras.append(compra_atual)
            
            # Deduz o valor da compra do saldo
            self.saldo -= total
            
        except SaldoInsuficienteError as e:
            print(f"\nERRO: {e}")
            return False
        except ValueError as e:
            print(f"\nERRO: {e}")
            return False
        else:
            print(f"\nSUCESSO: Pagamento de €{total:.2f} realizado com sucesso!")
            print(f"Saldo restante: €{self.saldo:.2f}")
            self.carrinho.clear()  # Limpa o carrinho após a compra
            return True
        finally:
            print("Operação de pagamento finalizada.")

    def mostrar_saldo(self):
        print(f"\nO seu saldo atual: €{self.saldo:.2f}")

    def mostrar_historico(self):
        if not self.historico_compras:
            print("\nVocê ainda não realizou nenhuma compra.")
            return
        
        print("\n" + "="*50)
        print("HISTÓRICO DE COMPRAS:")
        print("="*50)
        
        for i, compra in enumerate(self.historico_compras, 1):
            print(f"Compra #{i} - Total: €{compra['total']:.2f}")
            print("-"*50)
            for produto, quantidade in compra["itens"]:
                print(f"- {quantidade}x {produto}")
            print("-"*50)
        
        print("="*50)

    def executar(self):
        print("\n" + "*"*50)
        print("BEM-VINDO AO SISTEMA DE LOJA VIRTUAL")
        print("*"*50)
        
        while True:
            try:
                print("\nOpções:")
                print("1. Listar produtos")
                print("2. Adicionar produto ao carrinho")
                print("3. Verificar carrinho")
                print("4. Remover produto do carrinho")
                print("5. Mostrar saldo")
                print("6. Adicionar saldo")
                print("7. Finalizar compra")
                print("8. Ver histórico de compras")
                print("0. Sair")
                
                opcao = input("\nEscolha uma opção (0-8): ")
                
                if opcao == "0":
                    print("\nObrigado por utilizar nosso sistema. Volte sempre!")
                    break
                    
                elif opcao == "1":
                    self.listar_produtos()
                    
                elif opcao == "2":
                    self.listar_produtos()
                    produto = input("\nDigite o nome do produto para adicionar ao carrinho: ")
                    try:
                        quantidade = int(input("Digite a quantidade: "))
                        self.adicionar_ao_carrinho(produto, quantidade)
                    except ValueError:
                        print("\nERRO: Por favor, insira um número válido para a quantidade.")
                    
                elif opcao == "3":
                    self.verificar_carrinho()
                    
                elif opcao == "4":
                    self.verificar_carrinho()
                    if self.carrinho:
                        produto = input("\nDigite o nome do produto para remover do carrinho: ")
                        try:
                            resposta = input("Remover todas as unidades? (S/N): ")
                            if resposta.upper() == "S":
                                self.remover_do_carrinho(produto)
                            else:
                                quantidade = int(input("Digite a quantidade a remover: "))
                                self.remover_do_carrinho(produto, quantidade)
                        except ValueError:
                            print("\nERRO: Por favor, insira um número válido para a quantidade.")
                    
                elif opcao == "5":
                    self.mostrar_saldo()
                    
                elif opcao == "6":
                    try:
                        valor = float(input("Digite o valor a adicionar ao saldo: €"))
                        self.adicionar_saldo(valor)
                    except ValueError:
                        print("\nERRO: Por favor, insira um valor numérico válido.")
                    
                elif opcao == "7":
                    self.verificar_carrinho()
                    if self.carrinho:
                        confirmacao = input("\nConfirmar pagamento? (S/N): ")
                        if confirmacao.upper() == "S":
                            self.simular_pagamento()
                    
                elif opcao == "8":
                    self.mostrar_historico()
                    
                else:
                    print("\nERRO: Opção inválida. Por favor, escolha uma opção de 0 a 8.")
                    
            except Exception as e:
                print(f"\nERRO INESPERADO: {e}")
                print("Por favor, tente novamente.")


if __name__ == "__main__":
    loja = LojaVirtual()
    loja.executar()