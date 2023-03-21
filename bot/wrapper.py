# Import required libraries
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os

# Set the openai_api_key in the environment
os.environ['openai_api_key'] = "ADD OPENAI API KEY"

# Define a function to create a vector index
def createVectorIndex(path):

  # Define maximum input size, tokens, chunk size and maximum chunk overlap
  max_input = 4096
  tokens = 256
  chunk_size = 600
  max_chunk_overlap = 20

  # Create prompt helper
  prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit= chunk_size )

  # Define LLM predictor
  llmPredictor = LLMPredictor(llm=OpenAI(temperature=0,model_name="text-ada-001", max_token=tokens ))

  # Load data from the given path
  docs = SimpleDirectoryReader(path).load_data()

  # Create vector index
  vectorIndex = GPTSimpleVectorIndex(documents=docs, llm_predictor=llmPredictor, prompt_helper=prompt_helper)
  
  # Save vector index to disk
  vectorIndex.save_to_disk('vectorIndex.json')
  return vectorIndex

# Create a vector index for the given path
vectorIndex = createVectorIndex("data")

