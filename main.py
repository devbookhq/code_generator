from dotenv import load_dotenv
# Load .env file
load_dotenv()

from langchain.llms.openai import OpenAIChat
# from code_generator.tools.javascript.tool import JavascriptEvalTool
# from code_generator.js_agent.base import create_js_agent
from tools.javascript.tool import JavascriptEvalTool
from js_agent.base import create_js_agent
import subprocess


executor = create_js_agent(
    llm=OpenAIChat(temperature=0, max_tokens=1000),
    tool=JavascriptEvalTool(),
    verbose=True,
)
js_code = executor.run(
    """Write a body of an Express server function that handles incoming requests.
The server runs on the port 3001.
First make sure the request is of type 'POST' and then extract the field 'email' from the request's JSON body and save it to a variable.
If the request isn't POST, return an error message with the relevant status code.
Then send back status 200 as a response, the extracted email, and the version of the Express package in a payload."""
).strip('`').strip()
print('--------')
print(js_code)

with open('generated_server/server.js', 'w') as f:
    f.write(js_code)

subprocess.call(['node', 'generated_server/server.js'])
