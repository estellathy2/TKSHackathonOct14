#combines a llm with a prompt, put a buch of these building blocks tgt to carry out of sequence of operations

import os

#chatmodel
from langchain.chat_models import ChatOpenAI
#prompt
from langchain.prompts import ChatPromptTemplate
#chain
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

llm = ChatOpenAI(temperature=0.9, model_kwargs={'engine':'gpt-35-turbo'})

# prompt template 1
first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe \
    a company that makes {product}?"
)

# Chain 1
chain_one = LLMChain(llm=llm, prompt=first_prompt)

# prompt template 2
second_prompt = ChatPromptTemplate.from_template(
    "Write a 20 words description for the following \
    company:{company_name}"
)
# chain 2
chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(
    chains=[chain_one,chain_two],
    verbose=True
)

product = "Queen size sheet set"

print(overall_simple_chain.run(product))