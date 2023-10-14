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

major = input("Do you have a university major in mind that you want to choose in the future?")
uni = input("Do you have a university in mind that you want to apply for in the future?(full name please~)")

# prompt template 1: Major
first_prompt = ChatPromptTemplate.from_template(
    "Identify if the student knows what university major they want to take in the future, by analysing this text delimited by triple backticks: ```{Major}```. If yes, determine what major does the student want to take exactly, if no, output the boolean False."
)

chain_one = LLMChain(
    llm=llm, prompt=first_prompt, output_key="Major_Choice"
)

while major_choice == "False":
    #prompt template 1.1: Major choosing 
    major_exploration = input("Tell me about skills that you have(ex: leadership, coding, volleyball, etc.), hobbies that you like, and your interests. (As detailed as possible please~) ")
    first_prompt_1 = ChatPromptTemplate.from_template(
        "Help the student decide which university major they should choose in the future by analysing the text delimided by triple backtics ```{major_exploration}```, then explan why you choose that."
    )
    chain_one = LLMChain(
        llm=llm, prompt=first_prompt, output_key="Major_Recommendation"
    )

    # prompt template 1.2: Major verification
    second_prompt = ChatPromptTemplate.from_template(
        "Determine if the student has choosen what major they want to apply for in the future, if yes, return the full name of the major, if not, return False."
    )
    chain_two = LLMChain(
        llm=llm, prompt=second_prompt, output_key="Major_Choice"
    )

    overall_chain = SequentialChain(
        chains=[chain_one, chain_two],
        input_variables=["Major", "Uni"],  # Use square brackets for input variables
        output_variables=["Major_Choice", "Uni_Choice"],
        verbose=True
    )

    input_data = {"Major": major, "Uni": uni}
    output = overall_chain(input_data)  # Pass input data as a dictionary
    print(output)

# prompt template 2: University
second_prompt = ChatPromptTemplate.from_template(
    "Determine if the student is sure of what university they want to apply for in the future, if yes determine what university exactly does the student what to apply for, by analysing this text delimited by triple backticks: ```{Uni}``` "
)
# chain 3: input= Review and output= language
chain_two = LLMChain(
    llm=llm, prompt=second_prompt, output_key="Uni_Choice"
)

overall_chain = SequentialChain(
    chains=[chain_one, chain_two],
    input_variables=["Major", "Uni"],  # Use square brackets for input variables
    output_variables=["Major_Choice", "Uni_Choice"],
    verbose=True
)

input_data = {"Major": major, "Uni": uni}
output = overall_chain(input_data)  # Pass input data as a dictionary
print(output)
