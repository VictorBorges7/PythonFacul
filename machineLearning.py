import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf

# Dados fictícios
np.random.seed(42)
meses = np.arange(1, 13).reshape(-1, 1)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

dados = pd.DataFrame({'Mes': meses.flatten(), 'Vendas': vendas})

# Visualizar os dados
plt.scatter(dados['Mes'], dados['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Dados de Vendas ao Longo do Tempo')
plt.show()

# Dividir os dados
X = dados[['Mes']]
y = dados[['Vendas']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalização (escala 0-1)
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)

y_train_scaled = scaler_y.fit_transform(y_train)
y_test_scaled = scaler_y.transform(y_test)

# Modelo
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=8, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Treino
model.fit(X_train_scaled, y_train_scaled, epochs=500, verbose=0)

# Previsões
predictions_scaled = model.predict(X_test_scaled)
predictions = scaler_y.inverse_transform(predictions_scaled)

# Avaliação
y_test_inverse = scaler_y.inverse_transform(y_test_scaled)
erro_mse = mean_squared_error(y_test_inverse, predictions)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Visualizar resultados
plt.scatter(X_test, y_test_inverse, label='Dados Reais')
plt.scatter(X_test, predictions, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsões de Vendas (TensorFlow)')
plt.legend()
plt.show()

# Previsão para o próximo mês
proximo_mes = np.array([[13]])
proximo_mes_scaled = scaler_X.transform(proximo_mes)
previsao_scaled = model.predict(proximo_mes_scaled)
previsao = scaler_y.inverse_transform(previsao_scaled)[0, 0]

print(f'Previsão de Vendas para o Próximo Mês: {previsao:.2f}')
