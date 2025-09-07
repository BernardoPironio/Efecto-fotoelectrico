import pandas as pd

root = 'Mediciones/Barrido voltaje/barrido_voltaje_550nm.csv'
df = pd.read_csv('barrido_voltaje_550nm.csv')
print(df)

X, Y, V = df['X'], df['Y'], df['V']
X_medicion = -X


dataframe = pd.DataFrame({
    'X': X_medicion,
    'Y': Y,
    'V': V
})

dataframe.to_csv(root, index = False)