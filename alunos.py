import pandas as pd

df = pd.read_csv('alunos_lp.csv', sep=';')

# df.head()

if __name__ == '__main__':
    # print(df.head(100))

    df_search = df[df['Matricula'] == 1210481812044]
    if len(df_search) > 0:
        print(df_search['Nome'].values[0])
    else:
        print('Aluno não encontrado.')