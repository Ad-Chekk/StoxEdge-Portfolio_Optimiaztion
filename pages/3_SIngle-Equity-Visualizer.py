import pandas as pd
import streamlit as st
from test_algo import full_exceptVolume, complete_stock_data
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(page_title="Single Equity analysis", page_icon=":bar_chart:", layout="wide")

# st.markdown(
#     """
# <style>
# .sidebar .sidebar-content {
#     background-image: linear-gradient(#2e7bcf,#2e7bcf);
#     color: white;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )

bg1="https://b2316719.smushcdn.com/2316719/wp-content/uploads/2022/03/bg_06-768x384.jpg?lossy=1&strip=1&webp=1"
bg2="https://img.freepik.com/free-photo/abstract-luxury-gradient-blue-background-smooth-dark-blue-with-black-vignette-studio-banner_1258-52393.jpg?w=1380&t=st=1699467722~exp=1699468322~hmac=c04d81ce6221678b8377e6b4850bbb25a939a155a3973902fafbd186fba9de86"
bg="https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp"
bg3="https://cdn.pixabay.com/photo/2015/10/15/21/37/texture-990104_1280.jpg"
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1601333924581-7b48591a926c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

dash_width=700
full_width=900

# def full(stock_input):
#     df = yf.download(stock_input, start=stocksstartdate, end=today)
#     return  df
# lol = full('tcs.ns')
# st.write(lol)

emoj=':globe_with_meridians:'
emoj2=":chart_with_upwards_trend:"
emoj3=':chart_with_downwards_trend:'
file_emoj4=':clipboard:'
emojis= ''':alarm_clock:
1743	⏱️	:stopwatch:
1744	⏲️	:timer_clock:
1745	⏳	:hourglass_flowing_sand:'''

TL, M, TR, TMR = st.columns(4)
col1, col2 , col3= st.columns(3)

width= st.sidebar.selectbox('Select DashBoard Layout:', ["Dash-View", "Full-View"])
if width=="Dash-View":
 width1=dash_width
elif width=="Full-View":
 width1=full_width

selected_option = st.sidebar.selectbox("Select Stock Type:", ["Indian Stocks", "International stocks"])
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


if stock_input:
 st.write(stock_input)
 full_data= full_exceptVolume(stock_input,start_date,end_date)
 complete_data = complete_stock_data(stock_input,start_date,end_date)
 volume_data = complete_data['Volume']
 Database_view=st.button('View the complete database')
 if Database_view:
  st.write(complete_data)
 SingleStock_linechart=(st.line_chart
                        (full_data, use_container_width=True))

 with col1:
  line = px.line(full_data, title='Single stock visualizer')                 #line wala
  # line.update_layout(
  # paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
  # plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  # )
  line.update_layout( height=350, width=width1)
  st.plotly_chart(line)


 bar = px.bar(full_data, title='Single stock visualizer')                        #bar wala
 st.plotly_chart(bar, width=500)


 area = px.area(full_data, title='Single stock visualizer')
 st.plotly_chart(area)

 candle = px.histogram(full_data, title='Single stock visualizer')                #hist
 st.plotly_chart(candle)

 with col3:                                                                                           #donut wala
  # Calculate normalized price change and volume
  price_change = (complete_data['Close'] - complete_data['Open']).mean()
  normalized_volume = (complete_data['Volume'] - complete_data['Volume'].min()) / (
           complete_data['Volume'].max() - complete_data['Volume'].min())

  # Create the Donut Chart
  donut_data = pd.DataFrame({
   'Attribute': ['Price Change', 'Volume'],
   'Value': [price_change, normalized_volume.mean()]
  })

                                                                                                    # Create the Donut Chart
  fig = px.pie(donut_data, names='Attribute', values='Value', hole=0.5)
  fig.update_layout(
   paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
   plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  )
  fig.update_traces(textposition='inside', textinfo='percent+label')
  fig.update_layout(
   title='Price Change vs. Volume (Mean)',
   showlegend=False, height=350, width=300
  )
  st.plotly_chart(fig, use_container_width=True)

  # Display the Donut Chart in Streamlit

 with TL:                                                                  # gauge chart
  avg_volume=complete_data['Volume'].mean()
  fig = go.Figure(go.Indicator(
   mode="gauge+number",
   value=avg_volume,
   title={'text': "Average Trading Volume"},
   domain={'x': [0, 1], 'y': [0, 1]}
  ))                                                                         # Display the gauge chart in Streamlit
  fig.update_layout(
  paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
  plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  )
  fig.update_layout(width=300, height=270)
  st.plotly_chart(fig)

 with M:
  returns = full_data['Adj Close'].pct_change().dropna()
  volatility = returns.std()
  fig = go.Figure(go.Indicator(
   mode="gauge+number",
   value=volatility,
   title={'text': "volatility"},
   domain={'x': [0, 1], 'y': [0, 1]}
  ))
  fig.update_layout(
  paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
  plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  )
  fig.update_layout(width=300, height=270)
  # Display the gauge chart in Streamlit
  st.plotly_chart(fig)

 with TMR:                                                                                                       #  indicator
  fig = go.Figure()
  maximum = full_data['High'].max()
  minimum= full_data['Low'].min()
  fig.add_trace(go.Indicator(
   mode="number+delta",
   value=maximum,
   title={
    "text": stock_input+"s:<br><span style='font-size:0.8em;color:gray'>MAX returns</span><br><span style='font-size:0.8em;color:gray'>High-Low</span>"},
   delta={'reference': minimum, 'relative': True},
   domain={'x': [0, 1], 'y': [0, 1]}))
  fig.update_layout(height=270,width=300,
  paper_bgcolor = 'rgba(0, 0, 0, 0)',  # Transparent background
  plot_bgcolor = 'rgba(0, 0, 0, 0)',
  )
  st.write(fig, align='center')

 with TR:
  volume_data = complete_data['Volume']
  line = px.line(volume_data, title='Stock volume Visualizer')  # line wala
  line.update_layout(
   paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
   plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot area
  )
  line.update_layout(width=300, height=270)
  st.plotly_chart(line)

