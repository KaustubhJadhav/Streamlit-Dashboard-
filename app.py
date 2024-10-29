import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("GitHub Repositories Dashboard using Streamlit!")
st.write("Exploring GitHub repositories data from multiple datasets as an Assignment")

github_data_url = 'data/github_dataset.csv'
github_df = pd.read_csv(github_data_url)

st.subheader("GitHub Dataset Preview")
st.write(github_df.head())

st.subheader("Basic Statistics for GitHub Dataset")
st.write(github_df.describe())

st.subheader("Top 10 Repositories by Stars")
top_stars = github_df.nlargest(10, 'stars_count')
st.bar_chart(top_stars[['repositories', 'stars_count']].set_index('repositories'))

st.subheader("Forks Distribution")
plt.hist(github_df['forks_count'], bins=20, color='skyblue', edgecolor='black')
st.pyplot(plt)

st.write("Thank You")
