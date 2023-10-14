# Import the gradio library for building interactive UIs.
import gradio as gr

# Import necessary classes from the langchain module.
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.embeddings import OpenAIEmbeddings

# Define a prediction function that uses the AzureChatOpenAI model.
def predict(input, history=[]):
    # Define the name of the Azure model.
    azure_model_name = "gpt-35-turbo"

    # Initialize an instance of AzureChatOpenAI.
    chat = AzureChatOpenAI(
                deployment_name=azure_model_name,
                model_name=azure_model_name,
                temperature=0.3,
                max_tokens=2000,
                chrochroma_persist_directory='vector_db',  # Directory to store vector embeddings
                openai_embedding_model="text-embedding-ada-002"
        )

    # Initialize an instance of OpenAIEmbeddings for embedding.
    openai_embedding = OpenAIEmbeddings(deployment="text-embedding-ada-002")

    # Append the user's input to the history.
    history.append(HumanMessage(content=input))

    # Convert history messages to a single text for embedding.
    history_text = " ".join([message.content for message in history])
    
    # Embed the conversation history.
    embedding = openai_embedding.embed_query(text=history_text)

    # Get the model's response by passing the history.
    response = chat(history)

    # Append the model's response to the history.
    history.append(AIMessage(content=response.content))

    # Append the input and response to the overall history.
    history.append((input, response.content))

    # Return a dictionary with the updated history and the embedding.
    return history, history

# Initialize the history_chat list with system messages.
history_chat = [
    SystemMessage(content="You are a helpful assistant that helps teenagers plan their university, major, and future career path."),
    SystemMessage(content="You need to start with asking about the future major of the user. "),
    SystemMessage(content="If the user doesn't know what major they want to pick, you will need to ask questions regarding their skills, interests, and hobbies. After gathering this information, you need to provide 2-4 possible majors for the user to choose from.")
]

# Create a Gradio interface for the predict function.
demo = gr.Interface(fn=predict,
             inputs=["text",'state'],  # Input fields: text and state
             outputs=["chatbot",'state']).launch(debug=True, share=True)  # Launch the interface in debug mode and allow sharing.

# Launch the Gradio interface.
demo.launch()