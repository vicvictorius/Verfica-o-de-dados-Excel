import pandas as pd

df = pd.read_excel('arquivo_excel', sheet_name='nome planilha') #Substitua os dados

colunas_esperadas = [
    'coluna1', 'coluna2', 'coluna3', 'coluna4' #Adicione mais coluna caso necessário
]

def verificar_colunas(df, colunas_esperadas):
    colunas_faltantes = [col for col in colunas_esperadas if col not in df.columns]
    colunas_extras = [col for col in df.columns if col not in colunas_esperadas]
    return colunas_faltantes, colunas_extras

colunas_faltantes, colunas_extras = verificar_colunas(df, colunas_esperadas)

# Separar dados fora do padrão
if colunas_faltantes or colunas_extras:
    df_fora_padrao = df.copy()
    df_fora_padrao['colunas_faltantes'] = ', '.join(colunas_faltantes)
    df_fora_padrao['colunas_extras'] = ', '.join(colunas_extras)
    
    # Salvar dados fora do padrão em uma nova planilha
    df_fora_padrao.to_excel('dados_fora_padrao.xlsx', index=False)
    print("Dados fora do padrão salvos em 'dados_fora_padrao.xlsx'.")
else:
    print("Todas as colunas estão dentro do padrão esperado.")

print("Colunas faltantes:", colunas_faltantes)
print("Colunas extras:", colunas_extras)
