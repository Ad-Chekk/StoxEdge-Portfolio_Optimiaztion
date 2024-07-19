import streamlit as st
import streamlit.components.v1 as components
# from streamlit.components.v1 import html
import matplotlib.pyplot as plt
from test_algo import get_stock_data, High_data, complete_stock_data, full_exceptVolume, Low_data
import plotly.express as px
import pandas as pd

bg2="https://img.freepik.com/free-vector/gradient-network-connection-background_23-2148865393.jpg?w=1060&t=st=1699464243~exp=1699464843~hmac=060c8dff6d47a8c910de4b4eaf65a16e5974218ef2e67ea7defef04400ecbd15"
st.set_page_config(page_title="Stocks analysis", page_icon=":bar_chart:", layout="wide")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://cdn.pixabay.com/photo/2015/10/15/21/37/texture-990104_1280.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
import variables
# if variables.login_switch=='ok' :
if(1==1):
#
 # st.write('you can proceed')
 selected_option = st.sidebar.selectbox("Choose an option:", ["Indian Stocks", "International stocks"])
 stock_input= st.sidebar.text_input('Enter stock Name')
 if (selected_option=="Indian Stocks"):
  NorB= st.sidebar.radio("Choose Your exchange:", ["BSE", "NSE"])
  if (NorB=="NSE"):
   stock_input=stock_input+'.ns'
   # st.write(stock_input)
  elif(NorB=="BSE"):
   stock_input = stock_input + '.bo'
   # st.write(stock_input)
 start_date=st.sidebar.date_input(":spiral_calendar_pad: Start Date:")
 end_date=st.sidebar.date_input(':watch: End Date:')

 #stock_input =st.text_input("Enter your desired stock")
 #stock_input = [s.strip() for s in stock_input.split(",")]
 col1, col2 = st.columns(2)
 BL,BM, BR = st.columns(3)
 if stock_input:
  stock_data = get_stock_data(stock_input, start_date, end_date)
  low_stock_data= Low_data(stock_input, start_date, end_date)
  HIGHdf = High_data(stock_input, start_date, end_date)
  but= st.button('Get stock Data')
  if but:
   st.write('this is adjacent close  data')
   st.write(stock_data)
   st.write('this is high data')
   st.write(HIGHdf)
  with col1:
   fig = px.area(low_stock_data,title='Volume Visualizer')
   # Customize the figure layout (e.g., transparent background and gradient color)
   fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent plot area
    showlegend=True,  # Show legend
    xaxis=dict(title='Date'),  # X-axis title
    yaxis=dict(title='Value'),  # Y-axis title
    coloraxis=dict(colorscale='Cividis'),  # Gradient color scheme
   )
   fig.update_layout(height=270, width=400)
   # Display the Plotly figure in Streamlit
   st.plotly_chart(fig, use_container_width=True)

  with col2:
   # stock_data = get_stock_data(stock_input)
   # Get the maximum high value
   # HIGH = HIGHdf['High'].max()

   # Create a DataFrame for Plotly Express
                                                                                                     # Create a bar chart
   fig = px.bar(HIGHdf,title='High Prices of Various Stocks')

   # Customize the layout (optional)
   fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(title='Date'),  # X-axis title
    yaxis=dict(title='Value'),  # Y-axis title
    coloraxis=dict(colorscale='Cividis'),
    height=270, width=600
   )
   st.plotly_chart(fig)


  #with col3:
   # stock_data= get_stock_data(stock_input)

  with BL:
   line = px.line(stock_data, title='Single stock visualizer')                 # line wala
   # line.update_layout(
   # paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
   # plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
   # )
   line.update_layout(height=375, width=750)
   st.plotly_chart(line)

  with BR:
   max_adj_close_values = stock_data.max()
   # Create a pie chart
   fig = px.pie(values=max_adj_close_values, names=max_adj_close_values.index,
                title='Max Adjusted Close Prices Comparison')

   # Update layout if needed
   fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',
    height=375, width=650)

   # Show the chart in Streamlit
   st.plotly_chart(fig)



  #LOL = st.line_chart(stock_data, width=8000)

  #################
  # stock_data = closely(stock_input)
  #st.write(stock_data)
  st.write('Area chart showing high and low')
  # Create an area chart using Matplotlib
  stock_data=full_exceptVolume(stock_input,start_date,end_date)
  plt.fill_between(stock_data.index, stock_data['Low'], stock_data['High'], alpha=0.3, label='Low-High Range')
  plt.title(f'{stock_input} Stock Price Range')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.legend()
  # Display the area chart in Streamlit
  st.pyplot(plt)


else:
  st.write('no sorry')
  st.write(variables.login_switch)


