import gradio as gr
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv, find_dotenv
import warnings

_ = load_dotenv(find_dotenv()) # read local .env file

warnings.filterwarnings('ignore')


llm = ChatOpenAI(temperature = 0.9, model = llm_model)


prompt_1 = ChatPromptTemplate.from_template("Make sure this message does not contain anything similar with It’s your lucky day!")
chain_1 = LLMChain(llm = llm, prompt = prompt_1, output_key = "lucky_day")


prompt_2 = ChatPromptTemplate.from_template("Make sure this message is not talking about a prize")
chain_2 = LLMChain(llm = llm, prompt = prompt_2, output_key = "prize")


prompt_3 = ChatPromptTemplate.from_template("Make sure this message is not telling me to visit a link")
chain_3 = LLMChain(llm = llm, prompt = prompt_3, output_key = "visit_link")


prompt_4 = ChatPromptTemplate.from_template("Make sure this message does not say something urgent is happening")
chain_4 = LLMChain(llm = llm, prompt = prompt_4, output_key = "urgent")


prompt_5 = ChatPromptTemplate.from_template("Make sure the person texting me does not have a number starting with 604")
chain_5 = LLMChain(llm = llm, prompt = prompt_5, output_key = "604")


prompt_6 = ChatPromptTemplate.from_template("Make sure the person texting me does not have a number starting with 778")
chain_6 = LLMChain(llm = llm, prompt = prompt_6, output_key = "778")


prompt_7 = ChatPromptTemplate.from_template("Make sure the person texting me does not have a number starting with 236")
chain_7 = LLMChain(llm = llm, prompt = prompt_7, output_key = "236")


prompt_8 = ChatPromptTemplate.from_template("Make sure the person texting me does not have a number starting with 672")
chain_8 = LLMChain(llm = llm, prompt = prompt_8, output_key = "672")


prompt_9 = ChatPromptTemplate.from_template("Make sure the message is not asking for a payment")
chain_9 = LLMChain(llm = llm, prompt = prompt_9, output_key = "payment")


def predict(input, history=[]):


    azure_model_name = "gpt-35-turbo"
    chat = AzureChatOpenAI(
                deployment_name=azure_model_name,
                model_name=azure_model_name,
                temperature=0.0,
                max_tokens=2000
        )


    history_chat.append(HumanMessage(content=input))
    print(f"******{history_chat}")
    response = chat(history_chat)
    history_chat.append(AIMessage(content=response.content))
    history.append((input, response.content))


    return history, history


history_chat = [
    SystemMessage(content="You are a helpful assistant that helps teenagers plan their university, major, and future career path."),
]
demo = gr.Interface(fn=predict,
             inputs=["text",'state'],
             outputs=["chatbot",'state']).launch(debug = True, share = True)


demo.launch()
