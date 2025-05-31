def format_num(n):
    return f"({n})" if n < 0 else str(n)

def divisao_euclidiana():
    # Solicita os valores ao usuário
    a = int(input("Digite o dividendo (a): "))
    b = int(input("Digite o divisor (b): "))
    
    if b == 0:
        print("Erro: Divisão por zero não é permitida!")
        return
    
    print(f"\nDividendo (a) = {format_num(a)}")
    print(f"Divisor (b) = {format_num(b)}\n")
    
    # Caso 1: Divisão tradicional (a ≥ 0 e b > 0)
    if a >= 0 and b > 0:
        q = a // b
        r = a % b
        print(f"Divisão euclidiana tradicional (ambos positivos):")
        print(f"{a} = {b} × {q} + {r}")
        print(f"Quociente (q) = {q}")
        print(f"Resto (r) = {r} (onde 0 ≤ {r} < {b})")
        return
    
    # Caso 2: Divisor negativo (b < 0)
    abs_b = abs(b)
    abs_a = abs(a)
    
    # Passo 1: Calcula módulos e divisão nos naturais
    q_natural = abs_a // abs_b
    r_natural = abs_a % abs_b
    
    print(f"1. Calculamos os módulos e dividimos nos naturais:")
    print(f"|{format_num(a)}| = {abs_a}, |{format_num(b)}| = {abs_b}")
    print(f"{abs_a} = {abs_b} × {q_natural} + {r_natural}\n")
    
    # Passo 2: Ajusta para os sinais corretos
    if a >= 0 and b < 0:
        # Caso especial: dividendo positivo e divisor negativo
        q_final = -(q_natural)
        r_final = r_natural
        print(f"2. Ajustamos o quociente para compensar o divisor negativo:")
        print(f"{format_num(a)} = {format_num(b)} × {format_num(q_final)} + {r_final}")
    elif a < 0:
        # Caso geral: dividendo negativo (independente do divisor)
        q_temp = -q_natural if b > 0 else q_natural
        r_temp = -r_natural
        print(f"2. Ajustamos para o dividendo negativo:")
        print(f"{format_num(a)} = {format_num(b)} × {format_num(q_temp)} + {format_num(r_temp)}")
        
        # Passo 3: Corrige o resto se negativo
        if r_temp < 0:
            print(f"\n3. O resto é {format_num(r_temp)}, precisamos corrigir:")
            print(f"Adicionamos e subtraímos |b| = {abs_b}:")
            q_final = q_temp + (-1 if b > 0 else 1)
            r_final = r_temp + abs_b
            print(f"{format_num(a)} = {format_num(b)} × {format_num(q_final)} + {format_num(r_final)}")
        else:
            q_final = q_temp
            r_final = r_temp
    else:
        q_final = q_natural
        r_final = r_natural
    
    # Resultado final
    print(f"\nResultado final:")
    print(f"{format_num(a)} = {format_num(b)} × {format_num(q_final)} + {format_num(r_final)}")
    print(f"Quociente (q) = {format_num(q_final)}")
    print(f"Resto (r) = {format_num(r_final)} (onde 0 ≤ {r_final} < {abs_b})")

# Executa o programa
print("Divisão Euclidiana (incluindo números negativos)\n")
divisao_euclidiana()
