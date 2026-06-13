# Calculadora-em-python
Este programa implementa uma calculadora multifuncional em Python puro (sem bibliotecas externas como numpy ou math). Ele cobre as quatro operações aritméticas básicas e duas operações avançadas: • Operações básicas: adição, subtração, multiplicação e divisão, • Multiplicação de matriz, • Troco em cédulas e moedas 
                                                                                                                                    
Calculadora Multifuncional em Python                                                         
Projeto desenvolvido como atividade prática da Liga Acadêmica de Sistemas Inteligentes (LASI) da UFPI. Implementa operações básicas e avançadas utilizando apenas Python puro, sem bibliotecas externas.                                                                               
Funcionalidades                                                                         
Código	Explicação                                                                                                
Adição / Subtração / Multiplicação / Divisão	Operações aritméticas com dois números reais.                             
Produto Matricial (A × B)	Matrizes de qualquer dimensão. Verifica compatibilidade automática.                                 
Troco em Cédulas e Moedas	Algoritmo guloso com todas as denominações do Real (R$ 200 → R$ 0,01).                           
Pré-requisitos                                                                                       
• Python 3.8 ou superior instalado.                                                  
• Nenhuma biblioteca externa necessária.                                                   
Como Executar                                                                    
# Clone ou baixe o arquivo calculadora.py                                                             
# No terminal, navegue até a pasta do arquivo e execute:                                                   
python calculadora.py                                                                                    
Exemplo de Uso – Produto Matricial                                                                 
Número de linhas de A: 2                                                                                          
Número de colunas de A: 3                                                                               
Linha 1 (3 valores separados por espaço): 1 2 3                                                            
Linha 2 (3 valores separados por espaço): 4 5 6                                                                    
                                                                                                    
Número de linhas de B: 3                                                                                                      
Número de colunas de B: 2                                                                                                  
Linha 1: 7 8                                                                                      
Linha 2: 9 10                                                                                    
Linha 3: 11 12                                                                                                       

C = A × B:                                                                                   
[    58.00    64.00  ]                                                                                      
[   139.00   154.00  ]                                                                          
Exemplo de Uso – Troco                                                                        
Valor total da compra (R$): 37,50                                                            
Valor pago pelo cliente (R$): 50,00                                                                               
                                                                              
Troco a devolver: R$ 12,50                     
  R$  10,00  ×  1                             
  R$   2,00  ×  1                              
  R$   0,50  ×  1                                  
Estrutura do Código                                                  
calculadora.py é dividido em 4 blocos:                              
   
  Bloco 1 – Operações Básicas: funções puras (adicao, subtracao, multiplicacao, divisao).                                             
  Bloco 2 – Produto Matricial: leitura, cálculo (triplo loop) e exibição de matrizes.                            
  Bloco 3 – Troco: constante DENOMINACOES + algoritmo guloso.                                      
  Bloco 4 – Interface: menu interativo com laço principal e validação de entradas.                                         
