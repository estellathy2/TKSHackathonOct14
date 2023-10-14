#combines a llm with a prompt, put a buch of these building blocks tgt to carry out of sequence of operations

import os

#chatmodel
from langchain.chat_models import ChatOpenAI
#prompt
from langchain.prompts import ChatPromptTemplate
#chain
from langchain.chains import LLMChain

llm = ChatOpenAI(temperature=0.9, model_kwargs={'engine':'gpt-35-turbo'})

prompt = ChatPromptTemplate.from_template(
    "What is the best name to desribe a company that makes {product} ?"
)

chain = LLMChain(llm=llm, prompt=prompt)

product = "Queen size sheet set"
print(chain(product))