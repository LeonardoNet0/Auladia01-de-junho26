# pip install sqlalchemy
# pip  install pymysql

from sqlalchemy import create_engine
import pandas as pd 

host = 'localhost' #127.0.0.1
user = 'root'
password = ''
database = 'bd_mod02_aula03'

#Url de conexao

engine = create_engine (
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)


query = '''
     SELECT *
     FROM cadastro_produtos
     WHERE marca = 'hashtag'
     AND `preço unitario` < 25;
'''

#recebendo os dados

df_produtos = pd.read_sql(query, engine)
print(df_produtos)