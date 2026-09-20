# Teorema Estrito: Congruencia e Divisibilidade

**Euzebio Soares dos Santos**
euambiente@gmail.com
19/Set/2026

---

## A lacuna identificada

O Teorema 5 anterior afirma:

    ~_phi e congruencia iff m divide 2^n

A lacuna esta na implicacao (=>):

    ~_phi congruencia => m divide 2^n

O argumento anterior diz: o quociente herda estrutura de grupo. Mas isto precisa ser provado. Um homomorfismo dinamico (phi o tau_i = tau_tilde_i o phi) NAO e automaticamente um homomorfismo de grupo.

---

## Lema auxiliar: Toggles geram translations

**Lema 1.** Em F_2^n, todo translate x + y e composicao de no maximo n toggles.

**Prova.** Seja d = d_H(x,y) o numero de bits onde x e y diferem.
Seja i_1,...,i_d os indices desses bits.
Entao y = tau_{i_d}(tau_{i_{d-1}}(...tau_{i_1}(x)...)).
Portanto x + y = e_{i_1} + ... + e_{i_d} (soma em F_2^n).
E x + (x+y) = y. Logo y e alcancavel por d <= n toggles a partir de x. QED

---

## Lema auxiliar: Congruencia preserva composicao

**Lema 2.** Se ~_phi e congruencia (x ~ y => tau_i(x) ~ tau_i(y)), entao:

    x ~ y => tau_{i_1}(...tau_{i_d}(x)...) ~ tau_{i_1}(...tau_{i_d}(y)...)

para qualquer sequencia de toggles i_1,...,i_d.

**Prova.** Inducao sobre d.
Caso base d=1: tau_i(x) ~ tau_i(y) pela definicao de congruencia.
Inducao: tau_{i_1}(tau_{i_2}(...x...)) ~ tau_{i_1}(tau_{i_2}(...y...)) pela hipotese de inducao (com tau_{i_1} aplicado). QED

---

## Teorema principal (versao estrita)

**Teorema 1.** Seja phi: F_2^n -> {0,...,m-1} sobrejetiva. As seguintes afirmativas sao equivalentes:

1. ~_phi e congruencia (x ~ y => tau_i(x) ~ tau_i(y) para todo i)
2. ~_phi e compativel com adicao (x ~ y => x+z ~ y+z para todo z em F_2^n)
3. O quociente F_2^n / ~_phi herda estrutura de grupo de F_2^n

**Prova.**

(1 => 2) Se ~_phi e congruencia e x ~ y, entao pelo Lema 2:
    tau_{i_1}(...tau_{i_d}(x)...) ~ tau_{i_1}(...tau_{i_d}(y)...)
Pelo Lema 1, tau_{i_1}(...tau_{i_d}(x)...) = x + z para algum z.
Logo x + z ~ y + z. Portanto ~_phi e compativel com adicao.

(2 => 3) Se ~_phi e compativel com adicao, entao a operacao [x] + [y] = [x+y] e bem-definida (nao depende das representantes). O quociente herda:
  - Associatividade: ([x]+[y])+[z] = [(x+y)+z] = [x+(y+z)] = [x]+([y]+[z])
  - Elemento neutro: [0] + [x] = [0+x] = [x]
  - Elemento inverso: [x] + [-x] = [x + (-x)] = [0]
Portanto F_2^n / ~_phi e um grupo. QED

(3 => 1) Se o quociente e um grupo, entao tau_i([x]) = [tau_i(x)] = [x + e_i] = [x] + [e_i] e uma operacao de grupo, logo bem-definida. Se x ~ y, entao [x] = [y], logo [tau_i(x)] = [x] + [e_i] = [y] + [e_i] = [tau_i(y)]. Portanto tau_i(x) ~ tau_i(y). QED

---

## Corolario: m deve dividir 2^n

**Corolario 1.** Se ~_phi e congruencia, entao m divide 2^n.

**Prova.** Pelo Teorema 1, o quociente F_2^n / ~_phi e um grupo de ordem m. Pelo Teorema de Lagrange, m deve dividir |F_2^n| = 2^n. QED

---

## Teorema 2: Existencia de congruencia

**Teorema 2.** Se m divide 2^n, entao existe phi: F_2^n -> {0,...,m-1} tal que ~_phi e congruencia.

**Prova.** Se m | 2^n, entao 2^n = m . k para algum k. Seja N = {(x_1,...,x_n) em F_2^n : x_1 = ... = x_k = 0} (subgrupo de ordem k).
O quociente F_2^n / N tem ordem m. A projecao pi: F_2^n -> F_2^n/N e homomorfismo, logo congruencia. QED

---

## Teorema 3: Nao-existencia

**Teorema 3.** Se m nao divide 2^n, entao NENHUMA phi: F_2^n -> {0,...,m-1} induz congruencia.

**Prova.** Se ~_phi e congruencia, pelo Corolario 1, m divide 2^n. Contradicao. QED

---

## Conexao com I(n,m)

**Teorema 4.** I(n,m) > 0 se e somente se m nao divide 2^n.

**Prova.**

Se m divide 2^n: pelo Teorema 2, existe phi com ~_phi congruencia. Para este phi, E_dyn = 0 (comutatividade perfeita). Logo I(n,m) = 0.

Se m nao divide 2^n: pelo Teorema 3, NENHUMA phi induz congruencia. Logo para toda phi, ~_phi nao e congruencia, ou seja, existe (x,i) tal que x ~_phi y mas tau_i(x) !~_phi tau_i(y). Portanto E_dyn > 0 para toda phi. Logo I(n,m) > 0. QED

---

## Resumo final

| Condicao | Congruencia? | I(n,m) |
|----------|-------------|--------|
| m divide 2^n | Sim (homomorfismo) | = 0 |
| m nao divide 2^n | Nao (nenhuma phi) | > 0 |

Esta e a ponte correta entre algebra e compressao dinamica.
