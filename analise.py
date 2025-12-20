import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def limpar_nota(nota):
    """Transforma '8.5/10' em 8.5 (float)"""
    try:
        if pd.isna(nota) or nota == 'Sem Avaliação':
            return 0.0
        return float(str(nota).split('/')[0])
    except:
        return 0.0

def analisar_dados():
    if not os.path.exists('movies.csv'):
        print("Arquivo movies.csv não encontrado! Rode o scraper primeiro.")
        return

    colunas = ['Titulo', 'Ano', 'Nota', 'Sinopse']
    
    try:
        df = pd.read_csv('movies.csv', names=colunas, header=None)
        
        df['Nota_Valor'] = df['Nota'].apply(limpar_nota)
        df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce')

        print("\n=== TOP 5 FILMES (MAIORES NOTAS) ===")
        print(df.nlargest(5, 'Nota_Valor')[['Titulo', 'Ano', 'Nota']])

        print("\n=== ESTATÍSTICAS ===")
        print(f"Total de Filmes: {len(df)}")
        print(f"Média Geral das Notas: {df[df['Nota_Valor'] > 0]['Nota_Valor'].mean():.2f}")
        
        print("\n=== CONTAGEM POR ANO ===")
        print(df['Ano'].value_counts().sort_index())

    except Exception as e:
        print(f"Erro ao analisar: {e}")

if __name__ == '__main__':
    analisar_dados()