import streamlit as st
import pandas as pd

df=pd.read_csv("data/books.csv")
df["price"]=df["price"].str.replace("Â£", "").astype(float)

st.title("Book Data Dashboard")
st.dataframe(df)
ratings=df["rating"].value_counts(normalize=False)
st.subheader("Ratings Distribution")
st.bar_chart(ratings)

avg_price=df.groupby("rating")["price"].mean() 
st.subheader("Average Price by Rating")
st.bar_chart(avg_price)

st.subheader("Search Books")
search=st.text_input("Search by title")
if search:
    filtered=df[df["title"].str.contains(search)]
    st.dataframe(filtered)
else:
    pass
