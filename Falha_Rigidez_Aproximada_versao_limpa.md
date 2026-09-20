# Falha da Rigidez Aproximada Uniforme para Compressoes do Hipercubo Baseada no Defeito Medio de Comutatividade

**Euzebio Soares dos Santos**
euambiente@gmail.com
19/Set/2026

---

## Resumo

Considere o hipercubo binario F_2^n, equipado com os operadores de toggle tau_i(x) = x + e_i, i = 1,...,n, e uma compressao phi: F_2^n -> Y. Uma compressao e dinamicamente exata quando cada toggle do espaco original induz uma transformacao deterministica no espaco comprimido. No caso exato, as fibras da compressao sao classes laterais de um subespaco de F_2^n.

Este trabalho investiga a questao aproximada: se a comutatividade falha em apenas uma pequena proporcao media das transicoes, a compressao precisa estar proxima de uma compressao exata?

Mostramos que a resposta e negativa quando o defeito e normalizado pela dimensao. Para cada n >= 2, construimos uma compressao phi_n: F_2^n -> {A,B,C} satisfazendo delta_bar(phi_n) = 1/(2n) -> 0, enquanto d_H(phi_n, E_n) = 1/4, onde E_n e o conjunto das compressoes dinamicamente exatas com o mesmo contradominio.

Portanto, nao existe uma funcao f(epsilon) -> 0, independente de n, que controle a distancia ate uma compressao exata apenas a partir do defeito medio. O fenomeno decorre da concentracao do defeito em apenas duas direcoes, seguida de sua diluicao pela normalizacao por n.

O resultado conduz naturalmente a uma formulacao anisotropica da rigidez aproximada, na qual se considera o vetor completo de defeitos direcionais, e nao apenas sua media.

---

## 1. Introducao

### 1.1 O problema exato

O espaco F_2^n = {0,1}^n pode ser interpretado como o conjunto dos vertices do hipercubo Q_n.

Para cada coordenada i, seja e_i o vetor da base canonica e defina tau_i(x) = x + e_i. Como a soma ocorre em F_2, a transformacao tau_i troca o i-esimo bit.

Considere uma compressao phi: F_2^n -> Y. Queremos saber se a dinamica original pode ser representada deterministicamente no espaco comprimido. Para isso, exigimos a existencia de operadores T_i: Y -> Y satisfazendo

    phi(x + e_i) = T_i(phi(x))

para todo x em F_2^n e todo i. Equivalentemente, o diagrama

    F_2^n --tau_i--> F_2^n
      |phi              |phi
      v                 v
      Y   --T_i---->    Y

comuta exatamente. Nesse caso, a compressao sera chamada de **dinamicamente exata**.

### 1.2 Rigidez no caso exato

A condicao de exatidao implica que a relacao x ~_phi y iff phi(x) = phi(y) e preservada por todas as translacoes de F_2^n. Consequentemente, existe um subespaco V <= F_2^n tal que phi(x) = phi(y) iff x - y em V. As fibras de phi sao, portanto, os cosets x + V.

Esse fato se enquadra na teoria classica das congruencias de grupos. No caso de F_2^n, todo subgrupo aditivo e tambem subespaco linear. Assim, as compressoes dinamicamente exatas sao, a menos de uma renomeacao dos estados comprimidos, projecoes pi_V: F_2^n -> F_2^n/V.

Em particular, o numero de estados efetivamente utilizados por uma compressao exata deve ser |F_2^n/V| = 2^(n - dim V), ou seja, deve ser uma potencia de 2.

---

## 2. Da rigidez exata a rigidez aproximada

### 2.1 A pergunta natural

Uma vez classificado o caso exato, surge uma pergunta:

> Se uma compressao viola a condicao de comutatividade em apenas uma pequena proporcao das transicoes, ela deve estar proxima de uma compressao por cosets?

Essa pergunta esta relacionada, em espirito, a estabilidade de acoes aproximadas e a estabilidade de Ulam. A literatura nessa area investiga quando relacoes algebricas aproximadamente satisfeitas podem ser corrigidas para relacoes exatas.

O problema considerado aqui nao e identico a esses problemas gerais. Nosso objeto principal nao e uma representacao aproximada em um grupo simetrico, mas uma compressao cujas fibras podem nao ser congruencias exatas da acao dos toggles. Ainda assim, a pergunta possui a mesma forma conceitual:

    defeito local pequeno => proximidade global de uma estrutura exata?

O resultado deste trabalho mostra que a resposta depende criticamente da maneira como o defeito local e normalizado.

---

## 3. Definicoes

### 3.1 Compressoes

Fixe n >= 1 e um conjunto finito Y. Uma compressao e uma funcao phi: F_2^n -> Y. O conjunto de estados efetivamente utilizados e Im(phi) subset Y.

### 3.2 Defeito direcional

Para cada direcao i, queremos encontrar o melhor operador deterministico T_i: Y -> Y para prever a observacao comprimida depois do toggle. Definimos o defeito direcional otimo por

    delta_i(phi) = min_{T_i: Y->Y} Pr_x[ phi(x + e_i) != T_i(phi(x)) ]

Em forma de contagem,

    delta_i(phi) = (1/2^n) min_{T_i} |{x : phi(x + e_i) != T_i(phi(x))}|

Temos 0 <= delta_i(phi) <= 1. Alem disso, delta_i(phi) = 0 se e somente se existe T_i satisfazendo phi(x + e_i) = T_i(phi(x)) para todo x.

### 3.3 Defeito medio

Definimos o defeito medio de comutatividade por

    delta_bar(phi) = (1/n) sum_{i=1}^{n} delta_i(phi)

Equivalentemente,

    delta_bar(phi) = min_{T_1,...,T_n} (1/(n * 2^n)) |{(x,i) : phi(x+e_i) != T_i(phi(x))}|

### 3.4 Compressoes exatas

Denote por E_n(Y) o conjunto das compressoes dinamicamente exatas de F_2^n em Y:

    E_n(Y) = {psi: F_2^n -> Y : delta_i(psi) = 0 para todo i}

Temos psi em E_n(Y) iff delta_bar(psi) = 0.

### 3.5 Distancia entre compressoes

Para duas funcoes phi, psi: F_2^n -> Y, definimos a distancia de Hamming normalizada por

    d_H(phi, psi) = (1/2^n) |{x : phi(x) != psi(x)}|

A distancia de phi ate o conjunto das compressoes exatas e

    d_H(phi, E_n(Y)) = min_{psi em E_n(Y)} d_H(phi, psi)

---

## 4. A conjetura natural e sua negacao

### Conjetura de estabilidade media uniforme

Existiria uma funcao f: [0,1] -> [0,1], independente de n, satisfazendo lim_{epsilon->0} f(epsilon) = 0, tal que, para toda dimensao n, todo conjunto finito Y e toda compressao phi: F_2^n -> Y, tivessemos

    d_H(phi, E_n(Y)) <= f(delta_bar(phi))

Mostraremos que essa conjetura e falsa.

---

## 5. O exemplo basico em dimensao 2

Considere a funcao f: F_2^2 -> {A,B,C} definida por:

    f(0,0) = A,  f(0,1) = B
    f(1,0) = C,  f(1,1) = A

A cor A aparece em dois vertices opostos: (0,0) e (1,1). As cores B e C aparecem uma vez cada.

A funcao nao e dinamicamente exata. Na direcao 1:

- (0,0) -> (1,0), logo A -> C
- (1,1) -> (0,1), logo A -> B

A mesma observacao A precisaria ser enviada simultaneamente para B e C. Nenhuma funcao deterministica T_1: {A,B,C} -> {A,B,C} pode satisfazer as duas exigencias.

---

## 6. Elevacao para dimensao arbitraria

Para cada n >= 2, definimos phi_n: F_2^n -> {A,B,C} por phi_n(x_1,...,x_n) = f(x_1,x_2):

    phi_n(x) = A se (x_1,x_2) in {(0,0),(1,1)}
    phi_n(x) = B se (x_1,x_2) = (0,1)
    phi_n(x) = C se (x_1,x_2) = (1,0)

A funcao depende apenas das duas primeiras coordenadas. As coordenadas x_3,...,x_n sao ignoradas. Essa extensao e o mecanismo central do contraexemplo: a estrutura nao exata permanece concentrada nas duas primeiras direcoes, enquanto o defeito medio sera dividido pelo numero total n de direcoes.

---

## 7. Distribuicao das fibras

As fibras e suas medidas sao:

- phi_n^{-1}(A) = {x : x_1 = x_2}, medida 1/2
- phi_n^{-1}(B) = {x : (x_1,x_2) = (0,1)}, medida 1/4
- phi_n^{-1}(C) = {x : (x_1,x_2) = (1,0)}, medida 1/4

---

## 8. Calculo dos defeitos direcionais

### 8.1 Direcoes i >= 3

Para i >= 3, o toggle nao altera as duas primeiras coordenadas. Portanto phi_n(x + e_i) = phi_n(x). Tomando T_i = id, obtemos delta_i(phi_n) = 0 para i = 3,...,n.

### 8.2 Primeira direcao

Sob o toggle da primeira coordenada:

- (0,0) -> (1,0): A -> C
- (0,1) -> (1,1): B -> A
- (1,0) -> (0,0): C -> A
- (1,1) -> (0,1): A -> B

O problema aparece em A: uma ocorrencia deve ser enviada para C, a outra para B. Como T_1 e funcao, qualquer escolha erra em exatamente uma das quatro configuracoes (cada uma com probabilidade 1/4). Portanto delta_1(phi_n) = 1/4.

### 8.3 Segunda direcao

Sob o toggle da segunda coordenada:

- (0,0) -> (0,1): A -> B
- (0,1) -> (0,0): B -> A
- (1,0) -> (1,1): C -> A
- (1,1) -> (1,0): A -> C

Novamente, as duas ocorrencias de A exigem resultados diferentes. Pelo mesmo argumento, delta_2(phi_n) = 1/4.

---

## 9. Calculo do defeito medio

Temos delta_1 = delta_2 = 1/4 e delta_i = 0 para i >= 3. Logo:

    delta_bar(phi_n) = (1/n)(1/4 + 1/4) = 1/(2n)

Consequentemente, lim_{n->inf} delta_bar(phi_n) = 0.

---

## 10. Classificacao das compressoes exatas com tres rotulos

**Lema 1 (Rigidez dinamica).** Se phi: F_2^n -> Y e dinamicamente exata, entao as fibras nao vazias de phi sao cosetes de um subespaco V <= F_2^n.

*Prova.* A relacao x ~_phi y iff phi(x) = phi(y) e compativel com toggles: x ~_phi y implica tau_i(x) ~_phi tau_i(y) para todo i. Como em F_2^n todo translate x + y e composicao de no maximo n toggles, a relacao e compativel com adicao. O nucleo V = {x : x ~_phi 0} e subespaco linear, e toda classe de equivalencia e um cosete de V.

Pelo Lema 1, as fibras nao vazias de psi: F_2^n -> {A,B,C} (dinamicamente exata) sao cosets de algum subespaco V. Assim |Im(psi)| = |F_2^n/V| = 2^(n - dim V). Como o contradominio tem apenas tres elementos, |Im(psi)| <= 3. A unica potencia de 2 positiva <= 3 e 1 ou 2.

**Toda compressao dinamicamente exata em tres rotulos utiliza no maximo dois dos tres rotulos.**

---

## 11. Limitante inferior para a distancia

A compressao phi_n utiliza os tres rotulos com frequencias (1/2, 1/4, 1/4). Uma compressao exata psi utiliza no maximo dois rotulos. Portanto pelo menos um dos tres rotulos nao pode continuar sendo utilizado. Para eliminar um rotulo, e necessario modificar todos os pontos da respectiva fibra. A menor fibra possui medida 1/4.

Portanto, para toda compressao exata psi:

    d_H(phi_n, psi) >= min_r mu(phi_n^{-1}(r)) = 1/4

---

## 12. Construcao de uma compressao exata a distancia 1/4

Defina psi_n: F_2^n -> {A,B,C} por:

    psi_n(x) = A se x_1 = x_2
    psi_n(x) = B se x_1 != x_2

O rotulo C nao e utilizado. Equivalente a aplicacao linear x -> x_1 + x_2. Seu nucleo e V = {x : x_1 + x_2 = 0}, de dimensao n-1.

### Verificacao dinamica

- i=1: L(x+e_1) = L(x) + 1. T_1(A)=B, T_1(B)=A.
- i=2: L(x+e_2) = L(x) + 1. T_2(A)=B, T_2(B)=A.
- i>=3: L(x+e_i) = L(x). T_i(A)=A, T_i(B)=B.

C nao pertence a Im(psi_n), logo qualquer extensao de T_i ao rotulo C e irrelevante. Assim psi_n em E_n({A,B,C}).

### Distancia

phi_n e psi_n diferem apenas quando (x_1,x_2) = (1,0), que e a fibra de C em phi_n, de medida 1/4. Logo d_H(phi_n, psi_n) = 1/4.

Combinando com o limitante inferior:

    d_H(phi_n, E_n({A,B,C})) = 1/4

---

## 13. Teorema principal

**Teorema 1 (Diluicao dimensional do defeito).** Para todo n >= 2, existe uma compressao sobrejetiva phi_n: F_2^n -> {A,B,C} tal que

    delta_bar(phi_n) = 1/(2n) -> 0

e

    d_H(phi_n, E_n({A,B,C})) = 1/4

*Demonstracao.* Segue das Secoes 5-12.

---

## 14. Teorema de impossibilidade da rigidez media uniforme

**Teorema 2.** Nao existe funcao f: [0,1] -> [0,1] satisfazendo lim_{epsilon->0} f(epsilon) = 0 e

    d_H(phi, E_n(Y)) <= f(delta_bar(phi))

para toda dimensao n, todo conjunto finito Y e toda compressao phi: F_2^n -> Y.

*Demonstracao.* Por contradição. Se f existisse, entao 1/4 = d_H(phi_n, E_n) <= f(1/(2n)). Como 1/(2n) -> 0, f(1/(2n)) -> 0. Mas a desigualdade exige f(1/(2n)) >= 1/4 para todo n. Contradicao.

---

## 15. Consequencia para desigualdades lineares

**Corolario.** Se existisse d_H(phi, E_n) <= C_n * delta_bar(phi), entao C_n >= n/2.

Qualquer teorema de estabilidade baseado apenas no defeito medio precisara ter uma constante que cresca pelo menos linearmente com a dimensao.

---

## 16. Origem do fenomeno: diluicao dimensional

Toda a incompatibilidade esta localizada nas duas primeiras direcoes: delta_1 = delta_2 = 1/4. As demais sao perfeitamente compativeis: delta_3 = ... = delta_n = 0.

O defeito total permanece constante: sum delta_i = 1/2. O defeito medio divide por n: delta_bar = 1/(2n). Aumentar a dimensao nao corrige a nao exatidao. Apenas adiciona direcoes sem defeito, diluindo a media.

---

## 17. Formula anisotropica

Em vez de um unico numero, consideramos o vetor de defeitos:

    delta(phi) = (delta_1(phi), ..., delta_n(phi))

Tres normas:
- Defeito medio: (1/n) ||delta||_1
- Defeito total: ||delta||_1 = sum delta_i
- Defeito maximo: ||delta||_inf = max delta_i

No contraexemplo: delta_med = 1/(2n) -> 0, delta_tot = 1/2, delta_max = 1/4.

Somente o defeito medio converge a zero.

---

## 18. Formulações alternativas nao refutadas

O resultado nao refuta:
- Estabilidade por delta_max
- Estabilidade por delta_tot (com C >= 1/2)
- Estabilidade com hipotese de defeito difuso (delta_i <= K * delta_bar)

---

## 19. Limites do resultado

1. Foi refutada apenas a estabilidade uniforme baseada em delta_bar.
2. A construcao fornece apenas imagem de cardinalidade 3.
3. O resultado depende de toggles rotulados.
4. A originalidade nao esta estabelecida definitivamente.

---

## 20. Programa de pesquisa

**Problema 1:** Estabilidade por delta_max?
**Problema 2:** Estabilidade por delta_tot com C universal?
**Problema 3:** C_n* = Theta(n)?
**Problema 4:** Estabilidade anisotropica (vetor completo)?
**Problema 5:** Dimensao efetiva do defeito?

---

## 21. Conclusao

O caso exato apresenta rigidez completa: compressoes que preservam perfeitamente todos os toggles sao quocientes lineares por subespaços de F_2^n. O contraexemplo mostra que essa rigidez nao se prolonga uniformemente ao regime aproximado quando o erro e medido por uma media normalizada.

A causa e a diluicao dimensional: incompatibilidade concentrada em direcoes fixas, media que converge a zero. A transicao do caso exato para o aproximado exige uma mudanca de perspectiva:

    de um defeito escalar medio -> uma estrutura vetorial anisotropica do defeito.
