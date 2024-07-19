import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn

import plotly.express as px
import plotly.graph_objects as go

from test_algo import get_stock_data, complete_stock_data

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp");
background-size: cover;
}
.css-1aumxhk {
background-color: #011839;
background-image: none;
color: #ffffff
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

selected_option = st.sidebar.selectbox("Select Stock Type:", ["Indian Stocks", "International stocks"])
stock_input= st.sidebar.text_input('Enter stock Name')
if (selected_option=="Indian Stocks"):
  NorB= st.sidebar.radio("Choose Your exchange:", ["BSE", "NSE"])
  if (NorB=="NSE"):
   stock_input=stock_input+'.ns'
  elif(NorB=="BSE"):
   stock_input = stock_input + '.bo'
start_date=st.sidebar.date_input(":spiral_calendar_pad: Start Date:")
end_date=st.sidebar.date_input(':watch: End Date:')

closed_prices = complete_stock_data(stock_input,start_date,end_date)['Adj Close']

st.write(closed_prices)

seq_len = 15

mm = MinMaxScaler()
scaled_price = mm.fit_transform(np.array(closed_prices)[..., None]).squeeze()

X = []
y = []

for i in range(len(scaled_price) - seq_len):
    X.append(scaled_price[i: i + seq_len])
    y.append(scaled_price[i + seq_len])

X = np.array(X)[..., None]
y = np.array(y)[..., None]

train_x = torch.from_numpy(X[:int(0.8 * X.shape[0])]).float()
train_y = torch.from_numpy(y[:int(0.8 * X.shape[0])]).float()
test_x = torch.from_numpy(X[int(0.8 * X.shape[0]):]).float()
test_y = torch.from_numpy(y[int(0.8 * X.shape[0]):]).float()


class Model(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        output, (hidden, cell) = self.lstm(x)
        return self.fc(hidden[-1, :])


model = Model(1, 64)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

num_epochs = 100

for epoch in range(num_epochs):
    output = model(train_x)
    loss = loss_fn(output, train_y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0 and epoch != 0:
        print(epoch, "epoch loss", loss.detach().numpy())

model.eval()
with torch.no_grad():
    output = model(test_x)

pred = mm.inverse_transform(output.numpy())
real = mm.inverse_transform(test_y.numpy())



pred_flat = pred.flatten()
real_flat = real.flatten()

pred_column = pd.DataFrame({'Predicted':pred_flat})

# Make sure the lengths of 'Predicted', 'Real', and 'Date' arrays match
dates = complete_stock_data(stock_input,start_date,end_date).index[int(0.8 * X.shape[0]):]
min_len = min(len(dates), len(pred_flat), len(real_flat))

# Create a DataFrame from the data
data = pd.DataFrame({
    'Date': dates[:min_len],
    'Predicted': pred_flat[:min_len],
    'Real': real_flat[:min_len]
})
closed_prices = pd.concat([closed_prices, pred_column], axis=1)

st.write(pred)
st.write(pred_flat)
st.write(pred_column)
st.write(closed_prices)
line = px.line(closed_prices, title='Single stock visualizer')  # Specify 'Date' column as x-axis
line.update_layout(height=350, width=900)
st.plotly_chart(line)
