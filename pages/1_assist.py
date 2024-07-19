import streamlit as st
import streamlit.components.v1 as components
from test_algo import get_sector_info
# from streamlit.components.v1 import html
import variables



page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://w0.peakpx.com/wallpaper/139/711/HD-wallpaper-financial-stock-market-graph-on-stock-market-investment-trading-bullish-point-bearish-point-trend-of-graph-for-business-idea-and-all-art-work-design-vector-illustration-5299428-vector-art-at-vecteezy.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

another_img="https://w0.peakpx.com/wallpaper/139/711/HD-wallpaper-financial-stock-market-graph-on-stock-market-investment-trading-bullish-point-bearish-point-trend-of-graph-for-business-idea-and-all-art-work-design-vector-illustration-5299428-vector-art-at-vecteezy.jpg"
sec_img="https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp"


import streamlit as st

st.title("Stock Wishlist App")

# Create an input field for comma-separated stock names
stock_input = st.text_input("Enter comma-separated stock names:")

# Initialize an empty list for the wishlist
wishlist = []

# Add stocks to the wishlist when the user submits
if st.button("Add to Wishlist"):
    stocks = stock_input.split(",")
    wishlist.extend([stock.strip() for stock in stocks])

# Display the wishlist
if wishlist:
    st.header("Your Wishlist:")
    for stock in wishlist:
        st.write(stock)
    sector_list = []
    for stock in wishlist:
     sector_list.append(get_sector_info(stock))

    for sector in sector_list:
      st.write(sector)


else:
    st.info("Your wishlist is empty.")

div=st.button('proceed for diversification' )
for stock in wishlist:
    st.write(stock)
if(div==True):
    sector_list=[]
    for stock in wishlist:
        st.write(stock)
    for stock in wishlist:
     sector_list.append(get_sector_info(stock))

    for sector in sector_list:
      st.write(sector)

# my_js = f'''
#     // Get the canvas element
#             var ctx = document.getElementById('myChart').getContext('2d');
#
#             // Define data for the chart
#             var data = {{
#                 labels: ['January', 'February', 'March', 'April', 'May'],
#                 datasets: [{{
#                     label: 'Sample Data',
#                     data: [12, 19, 3, 5, 2],
#                     backgroundColor: 'rgba(75, 192, 192, 0.2)',
#                     borderColor: 'rgba(75, 192, 192, 1)',
#                     borderWidth: 1
#                 }}]
#             }};
#
#             // Create a new bar chart
#             var myChart = new Chart(ctx, {{
#                 type: 'bar',
#                 data: data,
#                 options: {{
#                     scales: {{
#                         y: {{
#                             beginAtZero: true
#                         }}
#                     }}
#                 }}
#             }});
#
#     '''

my_js2= f'''

                // Sample data for the pie chart
                var data = {{
                labels: ['IT', 'INFRASTRUCTURE', 'AUTOMOBILE'],
                datasets: [{{
                  data: [10, 20, 30],
                  backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                  hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
                }}]
                }};
                
                // Get the canvas element
                var ctx = document.getElementById('myPieChart').getContext('2d');
                
                // Create a pie chart
                var myPieChart = new Chart(ctx, {{
                type: 'pie',
                data: data
                }});
                
                
                '''

# if variables.login_switch=='ok' :
if(1==1):


    second = st.button('Proceed')
    if (second == True):
        st.write('STOXEDGE SECTOR CHARTS')

        components.html(f"""
        <!DOCTYPE html>
        <html>
        <head>
        
            
            <style>
            body{{
            background-image: url('stock1.jpg');
            background-size: cover;
            background-color: white;
            }}
            [data-testid="stSidebar"]{{
            min-width: 100px;
            max-width: 100px;
            }}
            </style>
           
        
        
        
        <title>Simple Pie Chart Example</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body style="background:url('./stock1.png')">
        <img src="/stock1.png">
        <canvas id="myPieChart" width="100" height="100"></canvas>
        
        <script>
        {my_js2}
        </script>
        
        </body>
        </html>
        
            """
               , height=600         )




     # for c in my_stocks.columns.values:  # c is columns for every column
     #     plt.plot(my_stocks[c], label=c)
     #
     # plt.title('stock chart')
     # plt.xlabel('Date', fontsize=18)
     # plt.ylabel('Adj. Price', fontsize=18)
     # plt.legend(my_stocks.columns.values, loc='upper left')
     # plt.show()
     # fig = plt.figure(figsize=(8, 8))
     # st.pyplot(fig)
     #









else:
    st.write('no sorry')
    st.write(variables.login_switch)


