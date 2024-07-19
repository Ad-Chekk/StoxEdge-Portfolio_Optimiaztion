import streamlit as st
import wikipedia
import streamlit as st
import yfinance as yf
link3="https://images.unsplash.com/photo-1545486332-9e0999c535b2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1545486332-9e0999c535b2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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
st.write('''*What is a Stock?**
   - A stock represents ownership in a company. When you buy a stock, you become a shareholder, which means you have a stake in the company's assets and profits.

2. **Stock Exchanges:**
   - Stocks are bought and sold on stock exchanges. 

5. **Bull vs. Bear Markets:**
   - A bull market is when stock prices are rising, and a bear market is when they are falling.

6. **Diversification:**
   - Spreading your investments across different stocks and sectors can reduce risk.

8. **Long-Term vs. Short-Term Investing:**
   - Long-term investors hold stocks for years, while short-term investors aim to profit from short-term price fluctuations.

9. **Research and Analysis:**
   - Before investing, research a company's financial health, performance, and future prospects.

10. **Risks:**
    - Stock investing carries risks, including the potential for loss. Make sure to assess your risk tolerance.

 it's important to educate yourself and consider your financial goals and risk tolerance before you start investing in the stock market.

And here our application comes into picture wherein we try to convert investors emotions into faith by providing some interactive but robust features
1. Showcasing the percentage of diversification in investors portfolio(pie chart)
2. Historical data of a particular stock
3. Comparative study of varied stocks in graphical ways.

These features helps in enhancing investors powers by minimising risks and maximizing the profits.''')







