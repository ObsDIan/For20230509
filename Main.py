import Function.EmbeddingAPI as EmbeddingAPI
import Function.CSVReader as CSVReader
import Function.AI_API as AI_API

key = 'api_key'
model = 'model'
question = 'question'
prompt = 'prompt'
text = 'text'
path = 'path'
new_path = 'new_path'

EmbeddingAPI.embedding(key, text)
CSVReader.CSVReader(path, new_path)
AI_API.generate_text(key, model, question, prompt)