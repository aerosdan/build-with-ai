import PIL.Image
import google.generativeai as genai


model = genai.GenerativeModel('gemini-pro-vision')

api_key = "AIzaSyBXYEyp9-OxQFrvOVMrGNZ9v96WcYUrFnU"

genai.configure(api_key=api_key)

#img = PIL.Image.open(r'C:\Users\danie\Codes\build-with-ai\doug.webp')
#response = model.generate_content(["which characters are being shown in this picture?", img])

img = PIL.Image.open(r'C:\Users\danie\Codes\build-with-ai\car.jpg')
response = model.generate_content(["what happening on this picture?", img])

print(response.text)