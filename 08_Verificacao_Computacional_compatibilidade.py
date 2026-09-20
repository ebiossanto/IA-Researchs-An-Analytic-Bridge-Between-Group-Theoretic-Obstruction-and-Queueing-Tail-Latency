"""
Experimento Concreto: Compatibilidade Dinamica para n=3, m=6
=============================================================

Para cada phi: F_2^3 -> {0,...,5}, enumeramos:
  1. E_s (erro estatico com melhor decodificador)
  2. Melhor tau_tilde_i para cada i
  3. E_dyn (erro dinamico com melhor tau_tilde)
  4. A (ambiguidade)
  5. Verificamos se phi o tau_i = tau_tilde_i o phi (comutatividade)

Pergunta central: Existe phi com E_s = 1/12 E compatibilidade dinamica perfeita?

Autor: Euzebio Soares dos Santos
Email: euambiente@gmail.com
Data: 19/Set/2026
"""
import numpy as np
from itertools import product
from collections import defaultdict
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def bits_of(val, nbits):
    return tuple((val >> (nbits - 1 - i)) & 1 for i in range(nbits))


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def compute_E_static(phi, n):
    m = max(phi.values()) + 1
    nbits = max(1, int(np.ceil(np.log2(m)))) if m > 1 else 1
    total_bits = (2 ** n) * n
    errors = 0
    for x in product(range(2), repeat=n):
        color = phi[x]
        color_bits = bits_of(color, nbits)
        for i in range(min(n, nbits)):
            if x[i] != color_bits[i]:
                errors += 1
    return errors / total_bits


def compute_E_static_best_decoder(phi, n):
    m = max(phi.values()) + 1
    vertices = list(product(range(2), repeat=n))
    
    bit_counts = defaultdict(lambda: [0] * n)
    for x in vertices:
        q = phi[x]
        for i in range(n):
            bit_counts[q][i] += x[i]
    
    c = {}
    for q in range(m):
        if q in bit_counts:
            c[q] = tuple(1 if bit_counts[q][i] > 0.5 else 0 for i in range(n))
        else:
            c[q] = (0,) * n
    
    total_bits = len(vertices) * n
    errors = 0
    for x in vertices:
        q = phi[x]
        errors += hamming(x, c[q])
    
    return errors / total_bits, c


def find_best_compressed_operators(phi, n):
    m = max(phi.values()) + 1
    vertices = list(product(range(2), repeat=n))
    
    tau_tilde = []
    for i in range(n):
        freq = defaultdict(int)
        for x in vertices:
            q = phi[x]
            x_toggled = list(x)
            x_toggled[i] = 1 - x_toggled[i]
            x_toggled = tuple(x_toggled)
            q_next = phi[x_toggled]
            freq[(q, q_next)] += 1
        
        best = {}
        for q in range(m):
            best_q_next = q
            best_q_next_count = 0
            for q_next in range(m):
                count = freq.get((q, q_next), 0)
                if count > best_q_next_count:
                    best_q_next = q_next
                    best_q_next_count = count
            best[q] = best_q_next
        tau_tilde.append(best)
    
    return tau_tilde


def compute_E_dyn_with_operators(phi, tau_tilde, n):
    m = max(phi.values()) + 1
    vertices = list(product(range(2), repeat=n))
    total = n * len(vertices)
    errors = 0
    
    for x in vertices:
        for i in range(n):
            x_toggled = list(x)
            x_toggled[i] = 1 - x_toggled[i]
            x_toggled = tuple(x_toggled)
            
            q = phi[x]
            q_expected = phi[x_toggled]
            q_actual = tau_tilde[i][q]
            
            if q_actual != q_expected:
                errors += 1
    
    return errors / total


def compute_ambiguity(phi, tau_tilde, n):
    m = max(phi.values()) + 1
    vertices = list(product(range(2), repeat=n))
    
    total_transitions = n * len(vertices)
    ambiguous = 0
    
    for x in vertices:
        for i in range(n):
            x_toggled = list(x)
            x_toggled[i] = 1 - x_toggled[i]
            x_toggled = tuple(x_toggled)
            
            q = phi[x]
            q_expected = phi[x_toggled]
            q_actual = tau_tilde[i][q]
            
            if q_actual != q_expected:
                ambiguous += 1
    
    return ambiguous / total_transitions


def check_commutativity(phi, tau_tilde, n):
    vertices = list(product(range(2), repeat=n))
    
    for x in vertices:
        for i in range(n):
            x_toggled = list(x)
            x_toggled[i] = 1 - x_toggled[i]
            x_toggled = tuple(x_toggled)
            
            left = phi[x_toggled]
            right = tau_tilde[i][phi[x]]
            
            if left != right:
                return False
    return True


def main():
    print("=" * 70)
    print("EXPERIMENTO: Compatibilidade Dinamica para n=3, m=6")
    print("=" * 70)
    print()
    print("Enumerando todos os 6^8 = 1.679.616 mapeamentos")
    print("Para cada: E_s, melhor tau_tilde, E_dyn, A, comutatividade")
    print()
    
    n = 3
    m = 6
    vertices = list(product(range(2), repeat=n))
    total_maps = m ** len(vertices)
    
    print(f"Total de mapas: {total_maps:,}")
    print()
    
    t0 = time.time()
    
    results = {
        'E_s_min': 1.0,
        'E_dyn_min': 1.0,
        'E_s_eq_1_12': [],
        'commutative_maps': [],
        'pareto': [],
        'all_Es_Ed': [],
    }
    
    count = 0
    for colors in product(range(m), repeat=len(vertices)):
        phi = {v: c for v, c in zip(vertices, colors)}
        
        E_s, c_decoder = compute_E_static_best_decoder(phi, n)
        tau_tilde = find_best_compressed_operators(phi, n)
        E_dyn = compute_E_dyn_with_operators(phi, tau_tilde, n)
        A = compute_ambiguity(phi, tau_tilde, n)
        is_commutative = check_commutativity(phi, tau_tilde, n)
        
        results['all_Es_Ed'].append((E_s, E_dyn, A, is_commutative))
        
        if E_s < results['E_s_min']:
            results['E_s_min'] = E_s
        if E_dyn < results['E_dyn_min']:
            results['E_dyn_min'] = E_dyn
        
        if abs(E_s - 1/12) < 1e-10:
            results['E_s_eq_1_12'].append((E_dyn, A, is_commutative))
        
        if is_commutative:
            results['commutative_maps'].append((E_s, E_dyn, A))
        
        count += 1
        if count % 200000 == 0:
            elapsed = time.time() - t0
            pct = 100 * count / total_maps
            print(f"  {count:>10,}/{total_maps:,} ({pct:.1f}%) [{elapsed:.1f}s]", flush=True)
    
    t1 = time.time()
    
    print()
    print("=" * 70)
    print("RESULTADOS")
    print("=" * 70)
    print()
    
    print(f"E_s* (minimo estatico): {results['E_s_min']:.6f}")
    print()
    
    print(f"E_dyn* (minimo dinamico com tau_tilde): {results['E_dyn_min']:.6f}")
    print()
    
    E_s_1_12 = results['E_s_eq_1_12']
    print(f"Mapas com E_s = 1/12: {len(E_s_1_12)}")
    if E_s_1_12:
        E_dyn_vals = [x[0] for x in E_s_1_12]
        A_vals = [x[1] for x in E_s_1_12]
        comm_vals = [x[2] for x in E_s_1_12]
        print(f"  E_dyn min: {min(E_dyn_vals):.6f}")
        print(f"  E_dyn max: {max(E_dyn_vals):.6f}")
        print(f"  A min: {min(A_vals):.6f}")
        print(f"  A max: {max(A_vals):.6f}")
        print(f"  Comutativos: {sum(comm_vals)}")
    print()
    
    comm = results['commutative_maps']
    print(f"Mapas comutativos (phi o tau_i = tau_tilde_i o phi): {len(comm)}")
    if comm:
        print(f"  E_s range: [{min(x[0] for x in comm):.6f}, {max(x[0] for x in comm):.6f}]")
        print(f"  E_dyn range: [{min(x[1] for x in comm):.6f}, {max(x[1] for x in comm):.6f}]")
        
        comm_Ed0 = [(Es, Ed, A) for Es, Ed, A in comm if abs(Ed) < 1e-10]
        print(f"  Comutativos com E_dyn=0: {len(comm_Ed0)}")
        if comm_Ed0:
            print(f"    E_s range: [{min(x[0] for x in comm_Ed0):.6f}, {max(x[0] for x in comm_Ed0):.6f}]")
    print()
    
    all_data = results['all_Es_Ed']
    pareto = []
    for Es, Ed, A, is_comm in all_data:
        dominated = False
        for Es2, Ed2, A2, _ in all_data:
            if Es2 <= Es and Ed2 <= Ed and (Es2 < Es or Ed2 < Ed):
                dominated = True
                break
        if not dominated:
            pareto.append((Es, Ed, A, is_comm))
    
    pareto.sort(key=lambda x: (x[0], x[1]))
    
    print(f"Fronteira de Pareto: {len(pareto)} pontos")
    print()
    print(f"  {'E_s':>10} | {'E_dyn':>10} | {'A':>10} | {'Comutativo':>10}")
    print(f"  {'----------':>10} | {'----------':>10} | {'----------':>10} | {'----------':>10}")
    for Es, Ed, A, is_comm in pareto[:20]:
        print(f"  {Es:>10.6f} | {Ed:>10.6f} | {A:>10.6f} | {'SIM' if is_comm else 'NAO':>10}")
    
    print()
    print("=" * 70)
    print("CONCLUSAO")
    print("=" * 70)
    print()
    
    if E_s_1_12:
        comm_Es_1_12 = [x for x in E_s_1_12 if x[2]]
        if comm_Es_1_12:
            print("RESPOSTA: SIM, existe phi com E_s=1/12 E compatibilidade dinamica perfeita.")
            print("A incompatibilidade NAO e estrutural para (n=3, m=6).")
        else:
            Ed_min_1_12 = min(x[0] for x in E_s_1_12)
            print(f"RESPOSTA: NAO, nenhum mapa com E_s=1/12 e comutativo.")
            print(f"O menor E_dyn para E_s=1/12 e {Ed_min_1_12:.6f}.")
            print("HA incompatibilidade estrutural.")
    else:
        print("Nenhum mapa com E_s=1/12 encontrado.")
    
    print()
    print(f"Tempo total: {t1-t0:.1f}s")


if __name__ == "__main__":
    main()
