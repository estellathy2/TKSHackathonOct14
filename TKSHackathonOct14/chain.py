import gradio as gr
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chains import SequentialChain

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

import os
import json
from dotenv import load_dotenv, find_dotenv
import warnings

_ = load_dotenv(find_dotenv()) # read local .env file

warnings.filterwarnings('ignore')


llm = ChatOpenAI(temperature = 0.9, model = llm_model)

prompt_template = ChatPromptTemplate.from_template(
    """\
    This is a prompt engineered for a scam detection software.
    For the text message: "{message}", give a score for the confidence for the validity of each of the following 3 items:
    1. Using this text message, the sender intends to scam or decieve the recipient in some way for personal gain.
    2. Using this text message, the sender intends to steal the recipient's money.
    3. Using this text message, the sender intends to steal the recipient's identity.
    The confidence score should be a number from 0 (least confident) to 1 (most confident), to two decimal places. Refrain from using absolute confidence scores as they can be unrealistic.
    Format the output as JSON with the following keys:
    "scam"
    "money"
    "info"
    
    Output the JSON only. Do not provide explanation.
    """
)




def score(input):

    azure_model_name = "gpt-35-turbo"
    chat = AzureChatOpenAI(
                deployment_name=azure_model_name,
                model_name=azure_model_name,
                temperature=0.0,
                max_tokens=2000
        )

    prompt = prompt_template.format_messages(text=input())
    response = chat(prompt)

    return return json.loads(response)


history_chat = [
    SystemMessage(content="You are a helpful assistant that helps teenagers plan their university, major, and future career path."),
]

demo = gr.Interface(fn=predict,
             inputs=["text",'state'],
             outputs=["chatbot",'state']).launch(debug = True, share = True)


demo.launch()
