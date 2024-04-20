import langchain
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers.transform import BaseTransformOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
import os
#from sentence_transformers import SentenceTransformer
from typing import List

from prompt_templates import *


class SBERTEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-minilm-l6-v2")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.model.encode(t).tolist() for t in texts]


llm_type = "gpt-4" # either gpt-4 or claude-3

if llm_type == "gpt-4":
    open_api_key = os.getenv('OPENAI_API_KEY')
    llm = ChatOpenAI(model="gpt-4-turbo-preview", openai_api_key=open_api_key, temperature=0)
elif llm_type == "claude-3":
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
    llm = ChatAnthropic(model='claude-3-opus-20240229', api_key=anthropic_api_key)
else:
    raise Exception(f"Unknown LLM type: {llm_type}")


def get_acceptance_ratios(preface_text):
    sys_prompt = SystemMessagePromptTemplate.from_template(acceptance_ratio_system_template)
    human_prompt = HumanMessagePromptTemplate.from_template(acceptance_ratio_human_template)
    chat_prompt = ChatPromptTemplate.from_messages([sys_prompt, human_prompt])
    result = llm.invoke(chat_prompt.format_prompt(preface_text=preface_text).to_messages())
    return result.content

def get_important_dates(website_text):
    sys_prompt = SystemMessagePromptTemplate.from_template(deadline_system_template)
    human_prompt = HumanMessagePromptTemplate.from_template(deadline_human_template)
    chat_prompt = ChatPromptTemplate.from_messages([sys_prompt, human_prompt])
    result = llm.invoke(chat_prompt.format_prompt(website_text=website_text).to_messages())
    return result.content

def get_conf_topics(preface_text):
    topic_prompt = ChatPromptTemplate.from_template(main_topics_extraction_template, stop_sequence=stop_sequence)
    topic_chain = topic_prompt | llm 
    result = topic_chain.invoke({"preface_text": preface_text})
    return result.content

def get_oc_member_roles(preface_text):
    ar_prompt = ChatPromptTemplate.from_template(oc_role_extraction_template, stop_sequence=stop_sequence)
    acceptance_ratio_chain = ar_prompt | llm
    result = acceptance_ratio_chain.invoke({"preface_text": preface_text})
    return result.content

def get_name_list_from_text(names_text):
    sys_prompt = SystemMessagePromptTemplate.from_template(ner_person_system_template)
    human_prompt = HumanMessagePromptTemplate.from_template(ner_person_human_template)
    chat_prompt = ChatPromptTemplate.from_messages([sys_prompt, human_prompt])
    result = llm.invoke(chat_prompt.format_prompt(names_text=names_text).to_messages(), stop=[stop_sequence])
    return result.content
