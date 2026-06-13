# =============================================================================
# CALCULADORA MULTIFUNCIONAL
# Operações: básicas + produto matricial + troco em cédulas/moedas
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
# BLOCO 1 – OPERAÇÕES BÁSICAS
# ─────────────────────────────────────────────────────────────────────────────

def adicao(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtracao(a, b):
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicacao(a, b):
    """Retorna o produto de dois números."""
    return a * b


def divisao(a, b):
    """Retorna o quociente de dois números. Levanta erro se b == 0."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b


# ─────────────────────────────────────────────────────────────────────────────
# BLOCO 2 – PRODUTO MATRICIAL (Álgebra Linear)
# ─────────────────────────────────────────────────────────────────────────────

def ler_matriz(nome):
    """
    Lê uma matriz do teclado, linha por linha.
    Retorna a matriz como lista de listas de floats e suas dimensões (linhas, colunas).
    """
    print(f"\n  Leitura da Matriz {nome}")
    linhas = int(input(f"  Número de linhas de {nome}: "))
    colunas = int(input(f"  Número de colunas de {nome}: "))

    matriz = []
    for i in range(linhas):
        while True:
            entrada = input(f"  Linha {i + 1} ({colunas} valores separados por espaço): ")
            valores = entrada.strip().split()
            if len(valores) != colunas:
                print(f"  Digite exatamente {colunas} valor(es).")
                continue
            try:
                linha = [float(v) for v in valores]
                break
            except ValueError:
                print(" Use apenas números.")
        matriz.append(linha)

    return matriz, linhas, colunas


def produto_matricial(A, B, linhas_A, colunas_A, colunas_B):
    """
    Calcula o produto C = A × B manualmente (sem bibliotecas).
    Condição: colunas de A == linhas de B.
    Retorna a matriz resultado C.
    """
    # Cria matriz resultado com zeros: linhas_A × colunas_B
    C = [[0.0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):           # percorre linhas de A
        for j in range(colunas_B):      # percorre colunas de B
            soma = 0.0
            for k in range(colunas_A):  # produto escalar da linha i de A pela coluna j de B
                soma += A[i][k] * B[k][j]
            C[i][j] = soma

    return C


def imprimir_matriz(matriz, titulo="Resultado"):
    """Exibe uma matriz formatada no terminal."""
    print(f"\n  {titulo}:")
    for linha in matriz:
        # Formata cada elemento com 2 casas decimais e largura fixa
        print("  [" + "  ".join(f"{v:8.2f}" for v in linha) + "  ]")


def menu_produto_matricial():
    """Interface de usuário para o produto matricial."""
    print("\n" + "=" * 50)
    print("  PRODUTO MATRICIAL  A × B")
    print("=" * 50)

    A, linhas_A, colunas_A = ler_matriz("A")
    B, linhas_B, colunas_B = ler_matriz("B")

    # Verifica compatibilidade dimensional
    if colunas_A != linhas_B:
        print(f"\n  ✗ Dimensões incompatíveis: A é {linhas_A}×{colunas_A} "
              f"e B é {linhas_B}×{colunas_B}.")
        print("  O número de colunas de A deve ser igual ao número de linhas de B.")
        return

    C = produto_matricial(A, B, linhas_A, colunas_A, colunas_B)

    imprimir_matriz(A, "Matriz A")
    imprimir_matriz(B, "Matriz B")
    imprimir_matriz(C, "C = A × B")


# ─────────────────────────────────────────────────────────────────────────────
# BLOCO 3 – TROCO EM CÉDULAS E MOEDAS (Fluxo de Caixa)
# ─────────────────────────────────────────────────────────────────────────────

# Cédulas e moedas do Real em ordem decrescente de valor (em centavos)
DENOMINACOES = [
    (20000, "R$ 200,00"),
    (10000, "R$ 100,00"),
    ( 5000, "R$  50,00"),
    ( 2000, "R$  20,00"),
    ( 1000, "R$  10,00"),
    (  500, "R$   5,00"),
    (  200, "R$   2,00"),
    (  100, "R$   1,00"),
    (   50, "R$   0,50"),
    (   25, "R$   0,25"),
    (   10, "R$   0,10"),
    (    5, "R$   0,05"),
    (    1, "R$   0,01"),
]


def calcular_troco(valor_pago_centavos, valor_total_centavos):
    """
    Calcula o troco mínimo em cédulas e moedas (algoritmo guloso).
    Recebe e retorna valores em centavos (inteiros) para evitar erros de ponto flutuante.
    Retorna dicionário: { "R$ X,XX": quantidade, ... }
    """
    troco = valor_pago_centavos - valor_total_centavos
    resultado = {}

    for valor_centavos, rotulo in DENOMINACOES:
        quantidade = troco // valor_centavos   # quantas notas/moedas dessa denominação cabem
        if quantidade > 0:
            resultado[rotulo] = quantidade
            troco -= quantidade * valor_centavos  # atualiza o troco restante

    return resultado


def menu_troco():
    """Interface de usuário para o cálculo de troco."""
    print("\n" + "=" * 50)
    print("  TROCO EM CÉDULAS E MOEDAS")
    print("=" * 50)

    try:
        total = float(input("  Valor total da compra (R$): ").replace(",", "."))
        pago  = float(input("  Valor pago pelo cliente (R$): ").replace(",", "."))
    except ValueError:
        print("  ⚠ Entrada inválida. Digite valores numéricos.")
        return

    if pago < total:
        print(f"\n  ✗ Valor pago (R$ {pago:.2f}) é menor que o total (R$ {total:.2f}).")
        return

    if pago == total:
        print("\n  Sem troco. Valor exato!")
        return

    # Converte para centavos para evitar imprecisão de float
    total_centavos = round(total * 100)
    pago_centavos  = round(pago  * 100)
    troco_centavos = pago_centavos - total_centavos

    print(f"\n  Troco a devolver: R$ {troco_centavos / 100:.2f}")
    print("  ─" * 25)

    detalhes = calcular_troco(pago_centavos, total_centavos)

    if detalhes:
        print("  Cédulas / Moedas:")
        for denominacao, qtd in detalhes.items():
            print(f"    {denominacao}  ×  {qtd}")
    else:
        print("  (Nenhuma cédula/moeda necessária)")


# ─────────────────────────────────────────────────────────────────────────────
# BLOCO 4 – INTERFACE PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────

def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 50)
    print("       CALCULADORA MULTIFUNCIONAL")
    print("=" * 50)
    print("  Operações Básicas:")
    print("  [1] Adição")
    print("  [2] Subtração")
    print("  [3] Multiplicação")
    print("  [4] Divisão")
    print()
    print("  Operações Avançadas:")
    print("  [5] Produto Matricial (A × B)")
    print("  [6] Troco em Cédulas e Moedas")
    print()
    print("  [0] Sair")
    print("=" * 50)


def ler_dois_numeros():
    """Lê dois números reais do teclado com validação."""
    while True:
        try:
            a = float(input("  Primeiro número: ").replace(",", "."))
            b = float(input("  Segundo número:  ").replace(",", "."))
            return a, b
        except ValueError:
            print(" Entrada inválida. Digite apenas números.")


def main():
    """Função principal: loop do menu."""
    print("\n  Bem-vindo(a) à Calculadora Multifuncional!")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        # ── Operações básicas ──────────────────────────────────────────────
        if opcao in ("1", "2", "3", "4"):
            a, b = ler_dois_numeros()

            if opcao == "1":
                resultado = adicao(a, b)
                operador  = "+"
            elif opcao == "2":
                resultado = subtracao(a, b)
                operador  = "−"
            elif opcao == "3":
                resultado = multiplicacao(a, b)
                operador  = "×"
            else:                          # opcao == "4"
                try:
                    resultado = divisao(a, b)
                    operador  = "÷"
                except ValueError as e:
                    print(f"\n  {e}")
                    continue

            print(f"\n  {a} {operador} {b} = {resultado}")

        # ── Produto matricial ──────────────────────────────────────────────
        elif opcao == "5":
            menu_produto_matricial()

        # ── Troco ─────────────────────────────────────────────────────────
        elif opcao == "6":
            menu_troco()

        # ── Sair ───────────────────────────────────────────────────────────
        elif opcao == "0":
            print("\n  Encerrando a calculadora. Até mais!\n")
            break

        else:
            print("\n  ⚠ Opção inválida. Digite um número de 0 a 6.")

        input("\n  Pressione Enter para continuar...")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
