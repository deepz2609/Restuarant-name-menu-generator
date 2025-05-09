import warnings
from langchain_community.llms import Ollama 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os

# Suppress warnings
warnings.filterwarnings("ignore")



import getpass
import os

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = "" #add an API key here if you have one 

from langchain.chat_models import init_chat_model

ollama_llm = init_chat_model("llama3-8b-8192", model_provider="groq")


def generate_menu(cusine):
    prompt_template_name = PromptTemplate(
        input_variables=["cusine"],
        template="I want to open a restaurant for {cusine} food. Suggest a only one fancy name for it without explaination about it and without communication.",
    )
    name_chain = LLMChain(
        llm=ollama_llm,
        prompt=prompt_template_name,
        output_key="restaurant_name",
    )

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""only Suggest some menu items for {restaurant_name}. Return it as a comma separated list without any communication.""",
    )

    food_items_chain = LLMChain(
        llm=ollama_llm,
        prompt=prompt_template_items,
        output_key="menu_items",
    )

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cusine"],
        output_variables=["menu_items", "restaurant_name"],
    )

    response = chain({"cusine": cusine})

    return response

if __name__ == "__main__":
    print(generate_menu("Italian"))
