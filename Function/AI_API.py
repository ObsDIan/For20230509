import os
import openai

def generate_text(key, model, question, prompt):
    #API 基本資訊
    openai.api_key = key
    openai.api_base = "https://api.openai.com/"
    openai.api_type = 'openai'
    openai.api_version = '2020-04-01'
    
    response = openai.Completion.create(model = model,
                                            )