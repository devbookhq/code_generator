from langchain.llms.openai import OpenAIChat
from code_generator.tools.javascript.tool import JavascriptEvalTool
from code_generator.js_agent.base import create_js_agent
# from tools.javascript.tool import JavascriptEvalTool
# from js_agent.base import create_js_agent

def generate(prompt: str):
  executor = create_js_agent(
      llm=OpenAIChat(temperature=0, max_tokens=1000),
      tool=JavascriptEvalTool(),
      verbose=True,
  )
  js_code = executor.run(prompt).strip('`').strip()
  return js_code