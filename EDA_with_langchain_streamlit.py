#Import required libraries
import os 

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#OpenAIKey
load_dotenv(find_dotenv())
#llm model
llm = OpenAI(temperature = 0)

@st.cache_data
def get_general_stats_about_data():
    st.write("**Data Overview**")
    st.write("Please see a sample of your data set below:")
    st.write(df.head())
    st.write("**Data Interpretation**")
    meaning_columns="What do the columns represent?"
    st.write(pandas_agent.run(meaning_columns))
    st.write("**Cleaning Data**")
    missing_values="How many missing values do we have?"
    st.write(pandas_agent.run(missing_values))
    duplicates="Do we have duplicates? How many?"
    st.write(pandas_agent.run(duplicates))
    st.write("**Data Summary**")
    st.write(df.describe())
    correlation="Calculate correlation between numerical variables, in order to identify relationships."
    st.write(pandas_agent.run(correlation))
    ouliers="Do we have outliers that can impact the anlysis. Which are they?"
    st.write(pandas_agent.run(ouliers))
    new_features="Which new featres should we create?"
    st.write(pandas_agent.run(new_features))


@st.cache_data
def steps_eda():
     return llm("What are the steps of EDA")
     
@st.cache_data
def get_details_about_variable():
    st.line_chart(df,y=[user_variable])
    summary_stats=f"What is the mean, mode, median, standrad deviation, skewness of the variable {user_variable}? "
    st.write(pandas_agent.run(summary_stats))
    distribution=f"What kind of distribution follows {user_variable}? "
    st.write(pandas_agent.run(distribution))
    outliers=f"Are there any outliers in  {user_variable}? Identify them."
    st.write(pandas_agent.run(outliers))
    missing_val=f"Are there any missing values in  {user_variable}? How many "
    st.write(pandas_agent.run(missing_val))
    return

def answer_user_question():
    dataframe_info = pandas_agent.run(user_question_dataframe)
    st.write(dataframe_info)
    return   

#Title
st.title('AI Assistant for Data Science 🤖')

#Welcoming message
st.write("Hello, 👋 I am your AI Assistant and I am here to help you with your data science projects.")

#Explanation sidebar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV File.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset.
    That's why I'd love for you to upload a CSV file.
    Once we have your data in hand, we'll dive into understanding it and have some fun exploring it.**
    ''')

    st.divider()

    st.caption("<p style ='text-align:center'> made with ❤️ by Dani</p>",unsafe_allow_html=True )

    with st.expander('What are the steps of EDA'):
                st.caption(steps_eda())

#Initialise the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked ={1:False}

#Function to udpate the value in session state
def clicked(button):
    st.session_state.clicked[button]= True
st.button("Let's get started", on_click = clicked, args=[1])
if st.session_state.clicked[1]:
    user_csv = st.file_uploader("Upload your file here", type="csv")
    if user_csv is not None:
        user_csv.seek(0)
        
        df = pd.read_csv(user_csv, low_memory=False)

        #Pandas agent
        pandas_agent = create_pandas_dataframe_agent(llm, df, verbose = True, allow_dangerous_code=True)
        
        #Main

        st.header('Exploratory data analysis')
        st.subheader('General information about the dataset')
        get_general_stats_about_data()

        st.subheader("**Variable analysis**")
        user_variable=st.text_input("Choose a variable you want to analyse more.")
        if user_variable is not None and user_variable !="":
            get_details_about_variable()

        st.subheader("**Further Study**")
       
        user_question_dataframe=st.text_input("Would you like to know more about your data set. Please type the question below.")
        if user_question_dataframe is not None and user_variable !="":
                answer_user_question()
        if user_question_dataframe in ("no", "No"):
                st.write("")




           

       