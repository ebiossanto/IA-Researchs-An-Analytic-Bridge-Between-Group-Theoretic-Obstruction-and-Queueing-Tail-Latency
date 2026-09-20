"""
Verificacao Computacional do Passo 2: Compatibilidade com Adicao
================================================================

Prova detalhada do Lema 1:
  Se ~ e compativel com toggles, entao ~ e compativel com adicao.

Autor: Euzebio Soares dos Santos
Email: euambiente@gmail.com
Data: 19/Set/2026
"""
from itertools import product


def verify_lemma1_brute_force(n):
    """
    Verifica por Enumeracao Exaustiva:
    
    Para toda relacao ~ compativel com toggles em F_2^n,
    verifica se ~ e compativel com adicao.
    
    Uma relacao ~ e representada como:
      - Uma lista de classes (particao de F_2^n)
      - Verifica: se x ~ y, entao x+z ~ y+z para todo z
    
    Como existem Bell(2^n) particoes, enumeramos apenas as ADMISSIVEIS
    (compativas com toggles) e verificamos se sao compativeis com adicao.
    """
    vertices = list(product(range(2), repeat=n))
    n_vertices = len(vertices)
    
    print(f"Verificando Lema 1 para n={n} ({n_vertices} vertices)")
    print(f"Numero de particoes admissiveis: ", end="", flush=True)
    
    admissible_partitions = []
    
    for m in range(1, n_vertices + 1):
        for phi_tuple in product(range(m), repeat=n_vertices):
            phi = {v: c for v, c in zip(vertices, phi_tuple)}
            
            is_admissible = True
            for x in vertices:
                for i in range(n):
                    x_toggled = list(x)
                    x_toggled[i] = 1 - x_toggled[i]
                    x_toggled = tuple(x_toggled)
                    
                    for y in vertices:
                        if phi[x] == phi[y]:
                            y_toggled = list(y)
                            y_toggled[i] = 1 - y_toggled[i]
                            y_toggled = tuple(y_toggled)
                            
                            if phi[x_toggled] != phi[y_toggled]:
                                is_admissible = False
                                break
                    if not is_admissible:
                        break
                if not is_admissible:
                    break
            
            if is_admissible:
                admissible_partitions.append(phi)
    
    print(f"{len(admissible_partitions)}")
    
    print(f"Verificando compatibilidade com adicao: ", end="", flush=True)
    
    count_ok = 0
    count_fail = 0
    
    for phi in admissible_partitions:
        is_compatible = True
        
        for x in vertices:
            for y in vertices:
                if phi[x] == phi[y]:
                    for z in vertices:
                        xz = tuple((a + b) % 2 for a, b in zip(x, z))
                        yz = tuple((a + b) % 2 for a, b in zip(y, z))
                        
                        if phi[xz] != phi[yz]:
                            is_compatible = False
                            break
                    if not is_compatible:
                        break
            if not is_compatible:
                break
        
        if is_compatible:
            count_ok += 1
        else:
            count_fail += 1
    
    print(f"OK={count_ok}, FAIL={count_fail}")
    
    return count_ok, count_fail


def verify_lemma1_structural(n):
    """
    Verificacao estrutural (sem enumerar particoes).
    
    Prova indutiva:
    
    Lema: Se ~ e compativel com toggles, entao e compativel com adicao.
    
    Prova: Seja z em F_2^n com d_H(0, z) = d.
    Se d = 0: z = 0, trivial.
    Se d > 0: z = e_{i_1} + ... + e_{i_d}.
    
    Defina x_0 = x, x_k = x_{k-1} + e_{i_k}.
    Defina y_0 = y, y_k = y_{k-1} + e_{i_k}.
    
    Se x ~ y:
      x_0 ~ y_0 (hipotese)
      x_1 ~ y_1 (toggle: x_0 + e_{i_1} ~ y_0 + e_{i_1})
      x_2 ~ y_2 (toggle: x_1 + e_{i_2} ~ y_1 + e_{i_2})
      ...
      x_d ~ y_d (toggle: x_{d-1} + e_{i_d} ~ y_{d-1} + e_{i_d})
    
    Logo x + z = x_d ~ y_d = y + z.
    """
    vertices = list(product(range(2), repeat=n))
    
    print(f"\nVerificacao estrutural para n={n}:")
    print()
    
    count = 0
    total = 0
    
    for x in vertices:
        for y in vertices:
            for z in vertices:
                bits = [i for i in range(n) if z[i] == 1]
                
                chain_x = [x]
                for i in bits:
                    prev = chain_x[-1]
                    next_v = list(prev)
                    next_v[i] = 1 - next_v[i]
                    chain_x.append(tuple(next_v))
                
                chain_y = [y]
                for i in bits:
                    prev = chain_y[-1]
                    next_v = list(prev)
                    next_v[i] = 1 - next_v[i]
                    chain_y.append(tuple(next_v))
                
                total += 1
                if chain_x[-1] == tuple((a + b) % 2 for a, b in zip(x, z)):
                    count += 1
    
    print(f"Cadeias verificadas: {count}/{total}")
    print(f"Todas as cadeias chegam em x + z: {count == total}")
    print()
    
    if n == 2:
        print("Exemplo para n=2:")
        x = (1, 0)
        y = (0, 1)
        z = (1, 1)
        
        bits = [i for i in range(n) if z[i] == 1]
        print(f"  x = {x}, y = {y}, z = {z}")
        print(f"  Bits de z: {bits}")
        print()
        
        chain_x = [x]
        for i in bits:
            prev = chain_x[-1]
            next_v = list(prev)
            next_v[i] = 1 - next_v[i]
            chain_x.append(tuple(next_v))
        
        chain_y = [y]
        for i in bits:
            prev = chain_y[-1]
            next_v = list(prev)
            next_v[i] = 1 - next_v[i]
            chain_y.append(tuple(next_v))
        
        print(f"  Cadeia de x: {' -> '.join(str(v) for v in chain_x)}")
        print(f"  Cadeia de y: {' -> '.join(str(v) for v in chain_y)}")
        print(f"  x + z = {tuple((a + b) % 2 for a, b in zip(x, z))} = {chain_x[-1]}")
        print(f"  y + z = {tuple((a + b) % 2 for a, b in zip(y, z))} = {chain_y[-1]}")
        print()


def main():
    print("=" * 60)
    print("PASSO 2: Compatibilidade com Adicao")
    print("=" * 60)
    print()
    print("Lema 1: Se ~ e compativel com toggles,")
    print("        entao ~ e compativel com adicao.")
    print()
    
    for n in [2, 3]:
        verify_lemma1_structural(n)
    
    print("=" * 60)
    print("VERIFICACAO POR ENUMERACAO EXAUSTIVA")
    print("=" * 60)
    print()
    
    for n in [2, 3]:
        ok, fail = verify_lemma1_brute_force(n)
        if fail == 0:
            print(f"  n={n}: LEMA CONFIRMADO (todas as particoes admissiveis sao compativeis com adicao)")
        else:
            print(f"  n={n}: LEMA REFUTADO ({fail} particoes admissiveis NAO sao compativeis)")
        print()
    
    print("=" * 60)
    print("CONCLUSAO")
    print("=" * 60)
    print()
    print("O Lema 1 e verdadeiro: compatibilidade com toggles implica")
    print("compatibilidade com adicao.")
    print()
    print("Prova informal:")
    print("  1. Todo z em F_2^n e soma de toggles: z = e_{i_1} + ... + e_{i_d}")
    print("  2. Se x ~ y, entao x + e_i ~ y + e_i (admissibilidade)")
    print("  3. Por inducao: x + z ~ y + z (composicao de toggles)")
    print()
    print("Prova formal:")
    print("  Seja z = e_{i_1} + ... + e_{i_d}. Defina:")
    print("    x_0 = x,  x_k = x_{k-1} + e_{i_k}")
    print("    y_0 = y,  y_k = y_{k-1} + e_{i_k}")
    print("  Por admissibilidade: x_{k-1} ~ y_{k-1} => x_k ~ y_k")
    print("  Por hipotese: x_0 ~ y_0")
    print("  Por inducao: x_d ~ y_d, ou seja, x + z ~ y + z. QED")


if __name__ == "__main__":
    main()
