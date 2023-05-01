import openai
import os
import pandas as pd
import csv

def embedding (key, text):
    
    # API 基本資訊
    openai.api_key = key
    openai.api_base = "https://api.openai.com/"
    openai.api_type = 'openai'
    openai.api_version = '2020-04-01'
    
    # embedding模組設定
    embedding = 'text-embedding-ada-002'
    
    # 調用 text-embedding-ada-002 模型進行 Embedding
    response = openai.Embedding.create(input=text, engine=embedding)
    embeddings = response['data'][0]['embedding']
    
    return embeddings


