import csv
import pandas as pd

if __name__ == '__main__':
    

df_original = pd.read_csv("productos.csv")

columnas_deseadas = ['producto', 'cant_req']
df_nuevo = df_original[columnas_deseadas]
df_nuevo.to_csv('archivo_nuevo.csv', index=False)
    data = make_csv('productos.csv')
    print(data)