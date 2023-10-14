#combines a llm with a prompt, put a buch of these building blocks tgt to carry out of sequence of operations

import os

#chatmodel
from langchain.chat_models import ChatOpenAI
#prompt
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
#chain
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


llm = ChatOpenAI(temperature=0.9, model_kwargs={'engine':'gpt-35-turbo'})

system_template = "You are a helpful assistant that helps teenagers plan their university, major, and future career path."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

#prompt template 1: Major
major = input("Do you have a university major in mind that you want to choose in the future?")
first_prompt = ChatPromptTemplate.from_template(
    "Determine if the student is sure of what university major they want to take in the future, if yes determine what major does the student what to take exactly, by analysing this text delimited by triple backticks: ```{Major}``` "
)
#chain 1: input-yesorno, output-university choice
chain_one = LLMChain(
    llm=llm, prompt=first_prompt, output_key="Major_Choice"
)

'''
#how do i make this so that it gets skipped when they have a choosen major??????
#prompt template 1.1: Yes or No 
major_exploration = input("Tell me about skills that you have(ex: leadership, coding, volleyball, etc.), hobbies that you like, and your interests.")
first_prompt_1 = ChatPromptTemplate.from_template(
    "Help the student decide which university major they should choose in the future by analysing the text delimided by triple backtics ```{major_exploration}```, then explan why you choose that."
)
'''

#chain2 = input=skills, output=major
chain_two = LLMChain(llm=llm, prompt=first_prompt_1, output_key="Major_Choice")


# prompt template 2: University
uni = input("Do you have a university in mind that you want to apply for in the future?")
second_prompt = ChatPromptTemplate.from_template(
    "Determine if the student is sure of what university they want to apply for in the future, if yes determine what university exactly does the student what to apply for, by analysing this text delimited by triple backticks: ```{Uni}``` "
)
# chain 3: input= Review and output= language
chain_two = LLMChain(
    llm=llm, prompt=second_prompt, output_key="Uni_Choice"
)

overall_chain = SequentialChain(
    chains=[chain_one,chain_two],
    input_variables=[{"Major", "Uni"}],
    output_variables=["Major_Choice", "Uni_Choice"],
    verbose=True
)

print(overall_chain(major, uni))