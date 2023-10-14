import gradio as gr
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


def predict(input, history=[]):

    azure_model_name = "gpt-35-turbo"
    chat = AzureChatOpenAI(
                deployment_name=azure_model_name,
                model_name=azure_model_name,
                temperature=0.3,
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