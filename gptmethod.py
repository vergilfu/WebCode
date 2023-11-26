import openai, jsonpath, json, asyncio, time


def getanswer(data):
    with open('configjson.json', encoding='utf-8') as f:
        configs = json.load(f)
    openai.api_base = configs['openai.api_base']
    openai.api_key = configs['openai.api_key']
    question = str(data['question'])

    start_time = time.time()
    response = openai.ChatCompletion.create(
        model='gpt-4-32k',
        messages=[
            {'role': 'user', 'content': question}
        ],
        temperature=0,
        stream=True  # again, we set stream=True
    )

    collected_messages = []

    for chunk in response:
        if jsonpath.jsonpath(chunk, "$..content"):
            finish_reason = chunk["choices"][0]["finish_reason"]

            if "content" in chunk["choices"][0]["delta"]:
                chunk_message = jsonpath.jsonpath(chunk, "$..content")[0]  # extract the message
                print(chunk_message)
                collected_messages.append(chunk_message)  # save the message
                response.send(chunk_message)
            elif finish_reason:
                full_reply_content = ''.join([m for m in collected_messages])
                print(full_reply_content)
        # return full_reply_content
