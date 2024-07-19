# from test_algo import full_exceptVolume
#
# # def full(stock_input):
# #     df = yf.download(stock_input, start=stocksstartdate, end=today)
# #     return  df
#
# # full_data= full_exceptVolume('m&m.ns')
# #
# # print(full_data)
#
#
# ######piechart code###########
# # Sector = st.button('Sectorwise Pie chart', key='keyo')      #second button
# #  if (Sector==True):
# #      stock_sector_data = {
# #          "TCS": "IT",
# #          "TATAMOTORS": "Automobile",
# #          "ABBOTT": "Pharma",
# #      }
# #
# #      # Streamlit UI for input
# #      st.title("Stock Sector Diversification")
# #
# #
# #
# #      # Input for stock names
# #      stocks = st.text_input("Enter stock names (comma-separated):")
# #      stocks = [s.strip() for s in stocks.split(",")]
# #
# #      # Create a pie chart based on the input
# #      sector_counts = {sector: 0 for sector in stock_sector_data.values()}
# #      for stock in stocks:
# #          if stock in stock_sector_data:
# #              sector = stock_sector_data[stock]
# #              sector_counts[sector] += 1
# #
# #      # Check if there are no stocks entered
# #      if sum(sector_counts.values()) == 0:
# #          st.warning("No stocks entered. Please input stock names.")
# #      else:
# #          # Generate the pie chart
# #          fig, ax = plt.subplots()
# #          ax.pie(sector_counts.values(), labels=sector_counts.keys(), autopct='%1.1f%%', startangle=90)
# #          ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# #
# #          # Display the pie chart in Streamlit
# #          st.pyplot(fig)
# #          plt.close(fig)
# ############################################################################################################
# import streamlit as st
# ss=st.set_page_config(layout="wide")
# container1 = st.container()
# col1, col2 = st.columns(2)
#
# with container1:
#     with col1:
#         st.write("hulla")
#
# with container1:
#     with col2:
#         st.write("col2")
#
#
# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
#
# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
#
# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#
# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
#
#
# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
#
# with st.expander("See explanation"):
#     st.write('''
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#     ''')
#     st.image("https://static.streamlit.io/examples/dice.jpg")
#
# import streamlit as st
#
# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )
#
# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
import streamlit as st
from test_algo import get_stock_data, closely, complete_stock_data, full_exceptVolume
#stock_input=st.text_input('give text')
selected_option = st.sidebar.selectbox("Choose an option:", ["Indian Stocks", "International stocks"])
if selected_option:
    stock_input= st.sidebar.text_input('Enter stock Name')
    if (selected_option=="Indian Stocks" and stock_input):
       NorB= st.sidebar.radio("Choose Your exchange:", ["BSE", "NSE"])
       if (NorB=="NSE"and stock_input):
        stock_input=stock_input+'.ns'
        st.write(stock_input)
       elif(NorB=="BSE"and stock_input ):
        stock_input = stock_input +'.bo'
        st.write(stock_input)
    start_date=st.sidebar.date_input(":spiral_calendar_pad: Start Date:")
    end_date=st.sidebar.date_input(':watch: End Date:')
    if stock_input and start_date and end_date :
     data = complete_stock_data(stock_input,start_date,end_date)
     st.write(data)

stock_input2 = st.text_input('give text')
if stock_input2 and start_date and end_date :
 data = complete_stock_data(stock_input2,start_date,end_date)
 st.write(data)
