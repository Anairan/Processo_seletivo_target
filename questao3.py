def faturamento_distribuidora(faturamento):
    #Maior valor de faturamento diário
    faturamento_valido = [f for f in faturamento if f != 0.0]
    menor = min(faturamento_valido)
    maior = max(faturamento_valido)

    #Média mensal de faturamento
    media = sum(faturamento_valido) / len(faturamento_valido)

    #Número de dias em que o faturamento foi superior à média mensal
    dias_acima_da_media = sum(1 for f in faturamento_valido if f > media)

    return menor, maior, dias_acima_da_media

faturamento = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
menor, maior, dias_acima_da_media = faturamento_distribuidora(faturamento)

print(f"Menor valor de faturamento diário: R$ {menor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
