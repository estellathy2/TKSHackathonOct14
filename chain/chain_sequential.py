#combines a llm with a prompt, put a buch of these building blocks tgt to carry out of sequence of operations

import os

#chatmodel
from langchain.chat_models import ChatOpenAI
#prompt
from langchain.prompts import ChatPromptTemplate
#chain
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = ChatOpenAI(temperature=0.9, model_kwargs={'engine':'gpt-35-turbo'})


#prompt template 1: translate to english
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following to english:"
    "\n\n{Review}"
)
#chain 1: input-review, output-english_review
chain_one = LLMChain(
    llm=llm, prompt=first_prompt, output_key="English_Review"
)


#prompt template 2: summarizing the review
second_prompt = ChatPromptTemplate.from_template(
    "Can you summarize the folowing review in 1 sentence?"
    "\n\n{English_Review}"
)
#chain2 = input=english_review, output=language
chain_two = LLMChain(
    llm=llm, prompt=second_prompt, output_key="summary"
)


# prompt template 3: translate to english
third_prompt = ChatPromptTemplate.from_template(
    "What language is the following review:\n\n{Review}"
)
# chain 3: input= Review and output= language
chain_three = LLMChain(
    llm=llm, prompt=third_prompt, output_key="language"
)


# prompt template 4: follow up message
fourth_prompt = ChatPromptTemplate.from_template(
    "Write a follow up response to the following "
    "summary in the specified language:"
    "\n\nSummary: {summary}\n\nLanguage: {language}"
)
# chain 4: input= summary, language and output= followup_message
chain_four = LLMChain(
    llm=llm, prompt=fourth_prompt, output_key="followup_message"
)

overall_chain = SequentialChain(
    chains=[chain_one,chain_two,chain_three,chain_four],
    input_variables=["Review"],
    output_variables=["English_Review", "summary", "language", "followup_message"],
    verbose=True
)

review = "Soyez prudent lorsque vous achetez quelque chose dans ce magasin au Canada et demandez la politique de retour... J'ai acheté des Lego le matin et j'ai trouvé la boîte cassée l'après-midi, alors je suis retourné chez Toys R Us, le même magasin sur Decarie, pour le retourner le même jour... ils ont refusé de le retourner en disant que dans leur politique, ils ne retournent pas les Lego ! Je leur ai demandé où cette politique était écrite, et bien sûr, elle n'est écrite nulle part... Je leur ai dit qu'ils devraient l'écrire sur un grand panneau près de la section Lego... très mauvais magasin, je ne sais pas jusqu'à quand ils survivront... toujours des prix élevés, pas de correspondance de prix (c'est ce que le personnel m'a dit), pas de retour... ils ne respectent aucun des droits des clients au Canada."

print(overall_chain(review))