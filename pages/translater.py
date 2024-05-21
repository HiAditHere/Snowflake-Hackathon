'''import modules'''

import os

import streamlit as st
from snowflake.cortex import Sentiment #To Calculate Sentiment
from snowflake.snowpark import Session

from src.english_translator import english_translator

# UI

st.title("Translater and Sentiment Analysis")

# Dropdown
options = st.selectbox(
    "Choose Type of comments",
    (
        "English Social Media feed",
        "Hindi comments feed",
    ),
    placeholder="Choose Type of comments",
)

# Button
button = st.button("Get Sentiments", key=1003)

# If Button clicked
if button:

    # Create connection with Snowpark
    connection_parameters = {
        "user": st.secrets["streamlit"]["user"],
        "password": st.secrets["streamlit"]["password"],
        "account": st.secrets["streamlit"]["account"],
        "warehouse": st.secrets["streamlit"]["warehouse"],
        "database": st.secrets["streamlit"]["database"],
        "schema": st.secrets["streamlit"]["schema"],
    }

    session = Session.builder.configs(connection_parameters).create()

    # Set Replicate API Token for snowflake arctic
    os.environ['REPLICATE_API_TOKEN'] = st.secrets["replicate"]["replicate_api_key"]

    # Create a staging
    CREATE_STAGING = "CREATE OR REPLACE STAGE staging_from_s3 "

    # Select S3 bucket URL

    if options == "English Social Media feed":
        BUCKET_STRING = f"URL='{st.secrets['s3_bucket_url']['english']}'"
    else:
        BUCKET_STRING = f"URL='{st.secrets['s3_bucket_url']['hindi']}'"

    # Authenticate with AWS account
    CREDENTIALS = f"CREDENTIALS=(AWS_KEY_ID='{st.secrets['aws']['access_key']}' AWS_SECRET_KEY='{st.secrets['aws']['secret_key']}') "

    # Storing the results into a CSV file
    FORMAT_STRING = "FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '\"' SKIP_HEADER = 1); "

    # Staging Query
    staging_query = CREATE_STAGING + BUCKET_STRING + CREDENTIALS + FORMAT_STRING

    # Execute Staging Query
    session.sql(staging_query).collect()

    # Create a Staging Table
    session.sql(
        """CREATE OR REPLACE TABLE
        staging_table(id INTEGER, comments STRING)"""
    ).collect()

    # Select Warehouse to be Used for staging
    #session.sql(f"USE WAREHOUSE {st.secrets['warehouse']};").collect()

    # Copy staged data from csv file to Staging Table
    session.sql(
        """COPY INTO staging_table 
        FROM @staging_from_s3"""
    ).collect()


    # Query the staging table
    df = session.table("staging_table").to_pandas()

    # Translate the sentences to english
    df["TRANSLATED"] = df['COMMENTS'].apply(english_translator)

    # Find sentiment scores of the translated sentences
    df["SENTIMENT"] = df['TRANSLATED'].apply(lambda comment: Sentiment(comment, session = session))

    # Displaying them results
    st.dataframe(df.drop(columns = ["ID"]))

    # Close the session when done
    session.close()
