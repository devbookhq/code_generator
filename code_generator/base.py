from langchain.llms.openai import OpenAIChat, OpenAI
from code_generator.tools.javascript.tool import JavascriptEvalTool
from code_generator.js_agent.base import create_js_agent
# from tools.javascript.tool import JavascriptEvalTool
# from js_agent.base import create_js_agent


server_template = """
const express = require('express');
const app = express();

app.use(express.json());

// Insert the handler here.
[HANDLER]
///////////////////////////

app.listen(8080, () => console.log('Listening on port 8080'));
"""

def generate(prompt: str) -> str:
  OpenAI(temperature=0, model_name='code-davinci-002', max_tokens=1000)
  executor = create_js_agent(
      llm=OpenAIChat(temperature=0, max_tokens=1000),
      tool=JavascriptEvalTool(),
      verbose=True,
  )
  handler_code = executor.run(prompt).strip('`').strip()
  server_code = server_template.replace('[HANDLER]', handler_code)
  return server_code