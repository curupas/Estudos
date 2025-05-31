def divisao_euclidiana():
    # Solicita os valores ao usuário
    a = int(input("Digite o dividendo (a): "))
    b = int(input("Digite o divisor (b): "))
    
    if b == 0:
        print("Erro: Divisão por zero não é permitida!")
        return
    
    print(f"\nDividendo (a) = {a}")
    print(f"Divisor (b) = {b}\n")
    
    # Caso ambos sejam positivos
    if a >= 0 and b > 0:
        q = a // b
        r = a % b
        print(f"Divisão euclidiana tradicional (ambos positivos):")
        print(f"{a} = {b} × {q} + {r}")
        print(f"Quociente (q) = {q}")
        print(f"Resto (r) = {r} (onde 0 ≤ {r} < {b})")
        return
    
    # Caso algum seja negativo (abordagem com módulos)
    print("Pelo menos um dos números é negativo. Vamos usar a abordagem com módulos:")
    
    # Passo 1: Calcular módulos e divisão nos naturais
    abs_a = abs(a)
    abs_b = abs(b)
    q_natural = abs_a // abs_b
    r_natural = abs_a % abs_b
    
    print(f"\n1. Calculamos os módulos e dividimos nos naturais:")
    print(f"|{a}| = {abs_a}, |{b}| = {abs_b}")
    print(f"{abs_a} = {abs_b} × {q_natural} + {r_natural}")
    
    # Passo 2: Ajustar para os valores originais
    if a < 0:
        q_temp = -q_natural
        r_temp = -r_natural
        print(f"\n2. Ajustamos para o dividendo negativo:")
        print(f"{a} = -({abs_b} × {q_natural} + {r_natural})")
        print(f"  = {b} × {q_temp} + {r_temp}")
    else:
        q_temp = q_natural
        r_temp = r_natural
    
    # Passo 3: Corrigir o resto se necessário
    if r_temp < 0:
        print(f"\n3. O resto é negativo ({r_temp}), precisamos corrigir:")
        print(f"Somamos e subtraímos |b| = {abs_b} para ajustar o resto:")
        
        # Calcula o ajuste
        if b > 0:
            ajuste = -1
        else:
            ajuste = 1
        
        q_final = q_temp + ajuste
        r_final = r_temp + abs_b
        
        print(f"{a} = {b} × {q_temp} + {r_temp}")
        print(f"  = {b} × {q_temp} + ({abs_b} - {abs_b}) + {r_temp}")
        print(f"  = {b} × {q_temp} + {b} × {ajuste} + ({r_temp + abs_b})")
        print(f"  = {b} × ({q_temp} + {ajuste}) + {r_final}")
        print(f"  = {b} × {q_final} + {r_final}")
    else:
        q_final = q_temp
        r_final = r_temp
    
    # Resultado final
    print(f"\nResultado final:")
    print(f"{a} = {b} × {q_final} + {r_final}")
    print(f"Quociente (q) = {q_final}")
    print(f"Resto (r) = {r_final} (onde 0 ≤ {r_final} < {abs_b})")

# Executa a função
print("Divisão Euclidiana (incluindo números negativos)\n")
divisao_euclidiana()
