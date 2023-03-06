from dotenv import load_dotenv
# Load .env file
load_dotenv()

# from langchain.llms.openai import OpenAIChat
# from code_generator.tools.javascript.tool import JavascriptEvalTool
# from code_generator.js_agent.base import create_js_agent
# from code_generator.tools.javascript.tool import JavascriptEvalTool
from code_generator.base import generate_req_handler
import subprocess

blocks = [
    "Make sure the request is of type 'POST'. If the request isn't POST, return an error message with the relevant status code.",
    "Extract the field 'email' from the request's JSON body and save it to a variable",
    "Take the extracted email, use the Supabase JavaScript SDK and save it in the Supabase database and call next middleware",
    "Check for any errors when inserting the email to the database. If there's an error return the database error and relevant status code",
]

prompt, code = generate_req_handler(blocks, 'post')

# print(js_code)

# with open('generated_server/server.js', 'w') as f:
#     f.write(js_code)

# subprocess.call(['node', 'generated_server/server.js'])
