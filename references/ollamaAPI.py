from langchain_openai import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache, SQLiteCache
import os

#run 'source .zsh file' to set the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
set_llm_cache(SQLiteCache(database_path=".langcache.db"))


llm = ChatOpenAI(model_name="gpt-3.5-turbo", 
                   api_key=openai_api_key,
                   max_tokens=100)

if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set")