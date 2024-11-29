def g(N, r, K):
    return N + r * N * (1 - N / K)

def fixed_point_method(N0, r, K, tol=0.001, max_iter=100):
    N = N0
    for i in range(max_iter):
        N_next = g(N, r, K)
        print(f"Iteración {i+1}: N = {N_next:.6f}")
        if abs(N_next - N) < tol:
            return N_next
        N = N_next
    return N

# Parámetros
r = 0.1
K = 1000
N0 = 100

# Encontrar el punto fijo
punto_fijo = fixed_point_method(N0, r, K)

print(f"Punto fijo encontrado: N = {punto_fijo:.6f}")

