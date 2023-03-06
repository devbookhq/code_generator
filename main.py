from dotenv import load_dotenv
# Load .env file
load_dotenv()

# from langchain.llms.openai import OpenAIChat
# from code_generator.tools.javascript.tool import JavascriptEvalTool
# from code_generator.js_agent.base import create_js_agent
# from code_generator.tools.javascript.tool import JavascriptEvalTool
from code_generator.base import generate_req_handler
import subprocess

p1 = "You're supposed to write a body of a Nodejs function that is a middleware inside an Express server.\n\nYou must follow these rules:\n- Don't write anything else but the body of function. Once you have the body function written, you should finish and output the code you have so far. \n- Don't import or require any third party packages or modules.\n- Don't initialize any libraries.\n- You have access to the following environment variables and you can use them if needed: SUPABASE_URL, SUPABASE_KEY.\n\nIf you cannot follow any of the rules above, finish with the last code you wrote. Don't try in any way to go around the rules or come up with other solutions.\n\n\nThe code you write must perform following logic:\n- Make sure the request is of type 'POST'. If the request isn't POST, return an error message with the relevant status code.\n- Extract the field 'email' from the request's JSON body and save it to a variable\n- Take the extracted email, use the Supabase JavaScript SDK and save it in the Supabase database and call next middleware\n- Check for any errors when inserting the email to the database. If there's an error return the database error and relevant status code"

# js_code = generate(
#     """Write a body of an Express server function that handles incoming requests.
# The server runs on the port 3001.
# First make sure the request is of type 'POST' and then extract the field 'email' from the request's JSON body and save it to a variable.
# If the request isn't POST, return an error message with the relevant status code.
# Then send back status 200 as a response, the extracted email, and the version of the Express package in a payload."""
# ).strip('`').strip()
js_code = generate_req_handler(p1).strip('`').strip()
print('--------')
print(js_code)

with open('generated_server/server.js', 'w') as f:
    f.write(js_code)

subprocess.call(['node', 'generated_server/server.js'])
