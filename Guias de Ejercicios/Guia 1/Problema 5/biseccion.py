from funciones import f, calcular_error

def biseccion(a, b, tolerancia=1e-6, max_iter=50):
    print(f"Iter\ta\t\tb\t\tc\t\tf(c)")
    print("-" * 50)
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        print(f"{i+1}\t{a:.4f}\t\t{b:.4f}\t\t{c:.4f}\t\t{fc:.6f}")
        
        if abs(fc) < tolerancia:
            return c
        
        if f(a) * fc > 0:
            a = c
        else:
            b = c
    
    return c