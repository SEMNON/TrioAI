import os 
import sys

from langchain.document_loaders import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = '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'



# query = sys.argv[1]
query = "Please summarize the document?"

print(query)

loader = TextLoader('KandidatenBackForthGerman.txt')
# loader = TextLoader('crelate2/Submittals.csv')
#loader = DirectoryLoader(".", glob="*.csv")
# loader = CSVLoader(file_path='Submittals.csv')
# data = loader.load()

# print(data)

index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query, llm=ChatOpenAI() ) )
print(index.query(query))
