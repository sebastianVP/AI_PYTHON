
def print_llm_response(response):
    if isinstance(response, dict) and "choices" in response:
        print(response["choices"][0]["message"]["content"])
    elif isinstance(response, str):
        print(response)
    else:
        print(response)
