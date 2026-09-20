# Teorema de Rigidez Dinamica - Prova Completa

**Euzebio Soares dos Santos**
euambiente@gmail.com
19/Set/2026

---

## 1. Setup

**Sistema dinamico.** Seja (X, T) com X = F_2^n e T = {tau_0,...,tau_{n-1}}, tau_i(x) = x + e_i.

**Compressao.** Seja phi: X -> Q sobrejetiva, |Q| = m.

**Definicao.** phi e **dinamicamente exata** se existem tau_tilde_i: Q -> Q tais que:

    phi(tau_i(x)) = tau_tilde_i(phi(x))  para todo x, todo i

Ou equivalentemente: phi o tau_i = tau_tilde_i o phi.

---

## 2. O Teorema

**Teorema de Rigidez Dinamica.** Seja phi: F_2^n -> Q dinamicamente exata. Entao:

  (a) ~_phi e congruencia: x ~ y implica x + z ~ y + z para todo z
  (b) V = {x : x ~ 0} e subespaco linear de F_2^n
  (c) Q e isomorfo a F_2^n / V
  (d) |Q| = 2^k para algum k em {0,...,n}

---

## 3. Prova

### Passo 1: Compatibilidade com toggles

Seja ~ a relacao: x ~ y iff phi(x) = phi(y).

Se x ~ y, entao phi(x) = phi(y). Logo:

    phi(tau_i(x)) = tau_tilde_i(phi(x)) = tau_tilde_i(phi(y)) = phi(tau_i(y))

Portanto tau_i(x) ~ tau_i(y). Temos:

    x ~ y  implica  tau_i(x) ~ tau_i(y)  para todo i    (★)

### Passo 2: Compatibilidade com adicao

**Lema 1.** A relacao ~ e compativel com adicao:

    x ~ y  implica  x + z ~ y + z  para todo z em F_2^n

**Prova do Lema 1.** Seja z = e_{i_1} + ... + e_{i_d}. Defina:

    x_0 = x,  x_k = x_{k-1} + e_{i_k}  para k = 1,...,d
    y_0 = y,  y_k = y_{k-1} + e_{i_k}  para k = 1,...,d

Pela propriedade (★): x_{k-1} ~ y_{k-1} implica x_k ~ y_k.

Pela hipotese: x_0 ~ y_0.

Por inducao: x_d ~ y_d, ou seja, x + z ~ y + z. QED

### Passo 3: O kernel e subespaco

Defina V = {x em F_2^n : x ~ 0}.

**Lema 2.** V e subgrupo de (F_2^n, +).

**Prova do Lema 2.**

  (i) 0 em V: trivialmente 0 ~ 0.

  (ii) Fechamento: Se x, y em V, entao x ~ 0 e y ~ 0.
       Pelo Lema 1: x ~ 0 implica x + y ~ 0 + y = y.
       Mas y ~ 0. Por transitividade: x + y ~ 0. Logo x + y em V.

  (iii) Inverso: Em F_2, -x = x. Logo x em V implica -x = x em V.

Portanto V e subgrupo. Como F_2^n e F_2-espaco vetorial e V e subgrupo,
V e subespaco linear (a unica operacao escalar e multiplicar por 0 ou 1). QED

### Passo 4: As classes sao cosetes

**Lema 3.** Toda classe de equivalencia e um cosete de V.

**Prova do Lema 3.** Seja C a classe de x: C = {y : y ~ x}.

Se y em C, entao y ~ x. Pelo Lema 1: y ~ x implica y + x ~ x + x = 0.
Logo y + x em V, ou seja, y = (y + x) + x = v + x para algum v em V.
Portanto C contido em x + V.

Se v em V, entao v ~ 0. Pelo Lema 1: v ~ 0 implica v + x ~ 0 + x = x.
Logo v + x em C. Portanto x + V contido em C.

Logo C = x + V. QED

### Passo 5: Isomorfismo e contagem

Pelo Lema 3, a particao induzida por phi e a particao por cosetes de V.

Defina pi: F_2^n -> F_2^n / V a projecao canonica: pi(x) = x + V.

Entao phi fatora por pi: existe bijecao psi: F_2^n / V -> Q tal que phi = psi o pi.

Portanto Q e isomorfo a F_2^n / V.

Pelo Teorema de Lagrange:

    |Q| = |F_2^n / V| = |F_2^n| / |V| = 2^n / 2^{dim(V)} = 2^{n - dim(V)}

Logo |Q| = 2^k com k = n - dim(V) em {0, 1, ..., n}. QED

---

## 4. Corolarios Imediatos

**Corolario 1.** Para m = 6 e n = 3: 6 nao e potencia de 2.
Nenhuma compressao dinamicamente exata com 6 estados existe.

**Corolario 2.** Os numeros de estados permitidos sao: 1, 2, 4, 8, ..., 2^n.

**Corolario 3.** A obstrucao de Lagrange (nao existe quociente de ordem 6 em F_2^3)
e consequencia imediata do Teorema de Rigidez.

**Corolario 4.** O Teorema de Rigidez e mais forte que Lagrange:
Lagrange diz que m deve dividir 2^n. Rigidez diz que m deve ser potencia de 2.
Para F_2^n, estas condicoes sao equivalentes (divisores de 2^n sao potencias de 2).

---

## 5. O que o Teorema prova

Se (X, tau_i) e o hipercubo e phi: X -> Q comprime o espaco de estados,
entao phi preserva a dinamica perfeitamente (phi o tau_i = tau_tilde_i o phi)
se e somente se Q e quociente vetorial F_2^n / V.

Em particular:

- Nao ha compressao dinamicamente exata com 3, 5, 6 ou 7 estados
- Os unicos numeros de estados possiveis sao 2^0, 2^1, ..., 2^n
- A algebra de F_2^n determina rigidamente a compressao

---

## 6. Originalidade

O resultado algébrico subjacente (compatibilidade com toggles => congruencia)
e consequencia direta de: toggles geram o grupo (F_2^n, +).
Isto e standard em teoria de grupos.

A contribuicao esta na APLICACAO:

- Formular compressao dinamica como problema de congruencia
- Provar que |Q| = 2^k e necessario
- Conectar com a impossibilidade de 6 estados

A prova e simples. A formulacao e aconexao e que podem ser novas.
