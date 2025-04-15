from openai import OpenAI

client = OpenAI(
    # Use one of the methods below to read in your API key (get it from https://platform.openai.com/account/api-keys)
    #api_key = os.getenv("OPENAI_API_KEY")
    api_key=""
)

history = [

]

def chat_with_gpt(prompt, model="gpt-4.1"):
    try:
        response = client.responses.create(
            model=model,
            instructions="You are a helpful MMORPG assistant named Simu. You are polite yet casual.",
            input=prompt,
        )
        return response
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # prompt one, ask simu to remember something
    user_prompt = input("Ask Simu: ")
    history.append({ "role": "user", "content": user_prompt })
    reply = chat_with_gpt(history)
    history += [{"role": el.role, "content": el.content} for el in reply.output]
    print("Simu says:", reply.output_text)
    # prompt two, ask simu to recall something from prompt one
    user_prompt = input("Ask Simu: ")
    history.append({"role": "user", "content": user_prompt})
    reply = chat_with_gpt(history)
    history += [{"role": el.role, "content": el.content} for el in reply.output]
    print("Simu says:", reply.output_text)

    foo = input("type to print history")
    print(history)
