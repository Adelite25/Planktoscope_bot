# https://python.langchain.com/docs/modules/agents/how_to/agent_vectorstore

#######################################################################################################
####################### AGENT ####################################################################
#############################################################################################

# pip install google-api-python-client>=2.100.0

from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.document_loaders import DirectoryLoader

from dotenv import load_dotenv
import os
env_path = os.path.join(os.path.dirname(__file__),  '.env') 	# Relative path to .env file
load_dotenv(env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# in the Google Cloud Console > Library > enable Custom Search API 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# in the Google Programmable Search Engine
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name='gpt-4', temperature=0.0)
tool = load_tools(["google-search"], llm=llm, google_api_key=GOOGLE_API_KEY , google_cse_id=GOOGLE_CSE_ID)

#agent = initialize_agent(tool, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,Verbose=True, return_intermediate_steps=True)
agent = initialize_agent(tool, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, return_intermediate_steps=False)




#query = "Quelles sont les lois de maxwell?"
#query = "What is a planktoscope?"
#query = "Who invented the Planktoscope?" 
#query = "what is the fraction size of the particles that can be imaged by the PlanktoScope?" 
#query = "what are the components of a planktoscope?" 
#query = "What is the difference in between PlanktoScope and Flowcam ?" 
#query = "what is the url to reach the GUI of the Planktoscope?" 



query = "what is the software that controls the Planktoscope?" 



#agent.run(query)
#agent.run(query)['output']
print(agent(query)['output'])


""" 
# https://github.com/langchain-ai/langchain/issues/3091 
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    #cb.on_llm_new_token = OPENAI_API_KEY
    # out = agent(inputs=[query])
    print(agent(inputs=[query])['output'])
 """




#print(agent("quelles sont les lois de maxwell?")['output'])
#agent.run("Who is the inventor of Planktoscope?")
#agent.run("What is a Planktoscope?")


#qa_with_sources : langchain agent ValueError: `run` not supported when there is not exactly one output key
# agent = initialize_agent(tools, llm, agent="zero-shot-react-description", return_intermediate_steps=True, memory=ConversationBufferMemory(memory_key="chat_history", input_key='input', output_key="output"), verbose=True)
