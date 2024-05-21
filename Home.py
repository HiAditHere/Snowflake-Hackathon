'''module imports'''

import streamlit as st

# page headings
st.set_page_config(layout="wide", page_title="Snowflake Hackathon")
st.title("Translation and Transliteration")
st.header("Snowflake Arctic and Snowflake Cortex Sentiment")
st.subheader("Group : Its all ME (Adit Bhosle) :)")

st.markdown('''
            ## Problem Statement

This is more about a problem I faced few years back.
#### I was working on an application that scraped commnets of social media feeds and performed sentiment analysis.

- It was about 2 years back. The task of scraping was done. But the difficult part was Sentiment Analysis. 
- The client did not have too much data on his side. Initially we tried bag of words approach but it went horribly wrong.
- Developing the application from scratch using RNN was fine but we did not have enough data for training.
- We tried to incorporate pretrained models like BERT. But it did not do the trick. `Social media feeds consisted of comments from some Asian languages`. Models like BERT are good for `English` but `NOT` for others.
- We tried to use pretrained models of other Asian languages (which at the time were very few). But we got stuck again because these models were essentially trained purely for other languages and `NOT English`. Today luckily there are Multi-lingual models out there for Sentiment analysis.

While multilingual models are there today, training such models takes huge amount of resources and compute capacity. Just importing the model from huggingFace would take 1GB of space :(. 

That is why most of us retort to cloud. Deploy the model on cloud, setup an API end point and just make inferences. And now as we see, Snowflake as also entered the game with its LLM Arctic.

> Today, the Snowflake AI Research Team is thrilled to introduce Snowflake Arctic, a top-tier enterprise-focused LLM that pushes the frontiers of cost-effective training and openness. Arctic is efficiently intelligent and truly open. - Snowflake

#### While I never asked the client, I presumed, the use of the application was to see how crowds reacted to socio-economic reforms. They seemed like investors and consultants who would make decisions based on crowd reactions to mass changes or reforms introduced.

I could be wrong but this seems like a good use case. Stock price judgments can be made, either to buy or sell depending on how crowd is reacting.

Training a model for multilingual sentiment analysis is not easy. Lot of data and compute would be required. But nowadays, sentiment analysis models are being used for advanced cases. ```Models are specifically developed for finance.```

So there are 2 use cases
- Multilingual Sentiment analysis
- Fianance based Sentiment analysis

Training a model for both use case simulataneously is a tough task. You basically need financial data in more than 1 language. Amount of data needed will be huge, and collecting this data itself is challenging.

` But How About Not Training a Model for 2 use cases at all ? `

Lets just keep our financial model aside. Its does good when provided with english data. `Lets work on translating all the data into 1 language.`

This is where our dear LLM helps. They are so good already. They are smart enough to understand transliteration. They are so good that they could prolly do sentiment analysis as well, but what if there might be a different use instead of the traditional sentiment analysis?

`A usecase specific model will most likely be trained from with English sentences.`Lets use our current LLM for translation. 

## Solution


1) Scrape Comments and store in S3
2) Import comments from S3 to Snowflake and do transliteration/translation
3) Import comments from snowflake to Streamlit
4) Do sentiment analysis in streamlit and return sentiment scores'''
            )