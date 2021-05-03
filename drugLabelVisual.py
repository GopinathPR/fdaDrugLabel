import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as graph_obj

st.title(" Open FDA Drug Label Data Analysis")

df=pd.read_excel("./partA.xlsx")
df2=pd.read_excel("./partB.xlsx")

dataTypes=st.sidebar.selectbox('',["PartA","PartB"])
    
def line(cht_dt):
        fig = px.line(cht_dt, x="year", y="avg_number_of_ingredients")
        st.plotly_chart(fig)

def bar(df):
    fig = graph_obj.Figure(data=[
            graph_obj.Bar(name='Avg no of Ingredients', x=df["year"], y=df['avg_number_of_ingredients'])])
    st.plotly_chart(fig)
    
if dataTypes=="PartA":
    
    st.title("PartA")
    st.write(df)
    st.subheader("Year wise Avg Ingredients for AstraZeneca Products")
    bar(df)

elif dataTypes=="PartB":
    st.title("PartB")
    st.subheader("PartB Raw data")
    st.write(df2)
    df2["avg_number_of_ingredients"].round(2)
    option = st.sidebar.selectbox(
        '',
         df2['route'].unique())
    cht_dt=df2[(df2["route"]==option)][["year",'avg_number_of_ingredients']]
    st.subheader("Filtered Results")
    st.write(cht_dt)
    st.subheader("Line Chart based on Route Filter: "+option+"")
    line(cht_dt)

