# Load .env file

# from langchain.llms.openai import OpenAIChat
# from code_generator.tools.javascript.tool import JavascriptEvalTool
# from code_generator.js_agent.base import create_js_agent
# from code_generator.tools.javascript.tool import JavascriptEvalTool
from dbk_aicode.base import generate_req_handler
# import subprocess
# from supabase import create_client, Client

def main():
    # url: str = os.environ.get("SUPABASE_URL")
    # key: str = os.environ.get("SUPABASE_KEY")

    # supabase: Client = create_client(url, key)
    # supabase.table('deployments').upsert(
    #     json={
    #         'id': '50210162-c5b1-40ac-8b8e-8a119492ef89',
    #         'logs': ['b'],
    #     },

    # ).execute()


    blocks = [
        "Make sure the request is of type 'POST'. If the request isn't POST, return an error message with the relevant status code.",
        "Extract the field 'email' from the request's JSON body and save it to a variable",
        "Take the extracted email, use the Supabase JavaScript SDK and save it in the Supabase database and call next middleware",
        "Check for any errors when inserting the email to the database. If there's an error return the database error and relevant status code",
    ]

    prompt, code = generate_req_handler(project_id='460355b3', blocks=blocks, method='post')

    # print(js_code)

    # with open('generated_server/server.js', 'w') as f:
    #     f.write(js_code)

    # subprocess.call(['node', 'generated_server/server.js'])


main()