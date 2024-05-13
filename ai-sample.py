import os
import google.generativeai as genai


api_key = "AIzaSyBXYEyp9-OxQFrvOVMrGNZ9v96WcYUrFnU"

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 50,
  "max_output_tokens": 10,
}

question = "The opposite of hot is"

model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        #generation_config=generation_config,
    )

# temprature = determinismo / 0 mais -- 1 menos
# topP = vocabulario rico
# topK = possibilidades de palavras

# print(model.count_tokens(question))
response = model.generate_content(question)
#print(response)
print(response.text)

