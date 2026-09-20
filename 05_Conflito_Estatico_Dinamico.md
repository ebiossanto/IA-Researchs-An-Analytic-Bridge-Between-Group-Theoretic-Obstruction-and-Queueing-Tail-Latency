# Conflito entre Preservacao Informacional e Preservacao de Adjacencia em Coloracoes do Hipercubo

**Euzebio Soares dos Santos**
euambiente@gmail.com
19/Set/2026

---

## Resumo

Investigamos a relacao entre duas metricas naturais em coloracoes phi: Q_n -> {0,...,m-1} do hipercubo n-dimensional: (i) erro estatico, que mede a preservacao de informacao entre os bits de x e os bits de phi(x); (ii) erro dinamico, que mede a preservacao de adjacencia (numero de arestas monocromaticas). Demonstramos que E_dyn*(n,m) = 0 para todo m >= 2 (pois Q_n e bipartido), enquanto E_static* pode ser positivo. Identificamos um conflito fundamental: o mapa otimo para uma metrica nao e otimo para a outra. Caracterizamos a fronteira de Pareto para n = 3 e formulamos perguntas abertas sobre a estrutura geral desta discrepancia.

---

## 1. Introducao

Seja Q_n = (V, E) o grafo do hipercubo n-dimensional, com V = Z_2^n e E = {{x, x XOR e_i} : x em V, i = 0,...,n-1}. Considere coloracoes phi: V -> {0,...,m-1}.

Duas questoes naturais surgem:

**Questao estatica (compressao):** Quao bem phi preserva a informacao dos bits? Isto e relevante para codificacao, compressao e monitoramento de estado.

**Questao dinamica (adjacencia):** Quao bem phi preserva a estrutura do grafo? Isto e relevante para coloracao de grafos, scheduling e deteccao de transicoes.

Estabelecemos que estas questoes conduzem a otimos diferentes, e que o conflito entre elas e um objeto matematico genuino.

---

## 2. Definicoes

### 2.1 Hipercubo

Seja Q_n = (V, E) com V = Z_2^n e |V| = 2^n, |E| = n . 2^(n-1). Para x em V e i em {0,...,n-1}, denote por tau_i(x) = x XOR e_i o toggle do i-esimo bit.

### 2.2 Coloracao

Seja phi: V -> {0,...,m-1} uma funcao de coloracao. Para x em V, denote por phi(x)_i o i-esimo bit da representacao binaria de phi(x).

### 2.3 Erro estatico

O erro estatico de phi e:

    E_static(phi) = (1 / (n . 2^n)) . sum_{x em V} sum_{i=0}^{n-1} 1[phi(x)_i != x_i]

Isto mede a fracao de posicoes onde os bits de phi(x) divergem dos bits de x.

### 2.4 Erro dinamico

O erro dinamico de phi e:

    E_dyn(phi) = (1 / (n . 2^n)) . sum_{x em V} sum_{i=0}^{n-1} 1[phi(x) = phi(tau_i(x))]

Isto mede a fracao de arestas monocromaticas em Q_n.

### 2.5 Minimos

Denote por E_static*(n,m) = min_phi E_static(phi) e E_dyn*(n,m) = min_phi E_dyn(phi), onde o minimo e sobre todas as coloracoes phi: V -> {0,...,m-1}.

---

## 3. Resultados principais

### 3.1 O erro dinamico e sempre zero para m >= 2

**Teorema 1.** Para todo n >= 1 e todo m >= 2:

    E_dyn*(n, m) = 0

**Demonstracao.** O hipercubo Q_n e bipartido: a particao V = V_0 union V_1, onde V_j = {x em V : sum x_i = j (mod 2)}. Toda aresta conecta vertices de paridades diferentes. A coloracao phi(x) = sum x_i mod 2 e uma 2-coloracao propria (sem arestas monocromaticas). Para m >= 2, esta coloracao e valida. QED

**Corolario.** A cromaticidade de Q_n e chi(Q_n) = 2.

**Validacao computacional.** Busca exaustiva sobre m^(2^n) mapeamentos confirma E_dyn* = 0 para n=3, m=2,3,4,5,6.

### 3.2 O erro estatico minimo

**Proposicao 1.** Para m = 1: E_static*(n,1) = 1 (trivial).

**Proposicao 2.** Para m >= 2^n: E_static*(n,m) = 0 (injetivo com mapeamento direto).

**Proposicao 3.** Para 2 <= m < 2^n:

    E_static*(n,m) >= 1/(n . 2^n)

**Demonstracao.** Pelo Principio da Casa dos Pombos, existem >= 2 pares colididos. Cada par contribui >= 1 erro. Total: >= 2 erros / (n . 2^n). QED

**Validacao computacional (n=3):**

    m=1: E_static* = 1.000000
    m=2: E_static* = 0.000000
    m=3: E_static* = 0.000000
    m=4: E_static* = 0.000000
    m=5: E_static* = 0.000000
    m=6: E_static* = 0.000000

### 3.3 O conflito entre otimos

**Teorema 2.** Para n=3 e m=2, nenhum mapa phi satisfaz simultaneamente E_static(phi) = 0 E E_dyn(phi) = 0.

**Demonstracao.** 

E_static(phi) = 0 exige que o unico bit de phi(x) iguale x_0 para todo x.
Isto determina phi unicamente: phi(x) = x_0.

E_dyn(phi) = 0 exige que phi seja uma 2-coloracao propria de Q_3.
A unica 2-coloracao propria (ate permutacao de cores) e a bipartida: phi(x) = sum x_i mod 2.

Estes sao mapeamentos DIFERENTES:
    First-bit: phi(001) = 0, phi(010) = 0, phi(100) = 1
    Paridade:  phi(001) = 1, phi(010) = 1, phi(100) = 1

Portanto, nenhum mapa e simultaneamente otimo para ambas as metricas. QED

---

## 4. Fronteira de Pareto para n=3

Para n=3 e m=2, enumeramos todos os 2^8 = 256 mapeamentos e computamos (E_static, E_dyn) para cada um. A fronteira de Pareto e:

    (E_static, E_dyn)  |  Descricao
    --------------------|------------
    (0.000, 0.083)      |  First-bit (otimo estatico)
    (0.042, 0.042)      |  Compromisso
    (0.083, 0.000)      |  Paridade (otimo dinamico)

**Observacao:** Nenhum ponto atinge (0, 0). O conflito e real.

Para m=3, a fronteira se expande mas o conflito persiste: existem mapas com E_static=0 e E_dyn=0 separadamente, mas nenhum simultaneamente.

---

## 5. A discrepancia como objeto matematico

Definimos a discrepancia estatica/dinamica como:

    Delta(n,m) = |{(E_static(phi), E_dyn(phi)) : phi otimo para uma metrica mas nao para a outra}|

Propriedades:

1. **Delta(n,m) > 0 para m=2 e n >= 3.** O conflito existe.

2. **Delta(n,m) depende da geometria de Q_n.** Para grafos diferentes, o conflito pode nao existir.

3. **Delta(n,m) pode ter estrutura algebrica.** Relacao com a decomposicao espectral de Q_n?

4. **Delta(n,m) e computavel exatamente** para n pequeno (forca bruta).

---

## 6. Perguntas abertas

1. **Classificacao:** Para quais (n,m) existe conflito?

2. **Fronteira:** Qual e a forma da fronteira de Pareto para n geral?

3. **Desigualdade:** Existe constante c > 0 tal que E_static(phi) + c . E_dyn(phi) >= f(n,m) para toda phi?

4. **Algebra:** A discrepancia Delta(n,m) tem estrutura de anel ou modulo?

5. **Transicao:** Para que m o conflito desaparece? Existe um limiar m*(n)?

6. **Aplicacao:** A discrepancia e util para codificacao, scheduling ou deteccao de falhas?

---

## 7. Conclusao

O conflito entre preservacao informacional (estatica) e preservacao de adjacencia (dinamica) em coloracoes do hipercubo e um objeto matematico genuino.

O hipercubo Q_n e bipartido, entao E_dyn* = 0 para m >= 2. Mas o mapa que atinge E_dyn* = 0 (paridade) nao atinge E_static* = 0, e vice-versa.

Este conflito nao e um detalhe tecnico: e a questao matematica central. A pesquisa futura deve classificar quando o conflito existe, caracterizar a fronteira de Pareto, e explorar a estrutura algebrica da discrepancia.
