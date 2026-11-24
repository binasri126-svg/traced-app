
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain the basic steps involved in an export shipment from India. Keep it short.",

    "Write a short email to a customer informing them that the vessel ETD has been delayed.",

    "What are the main responsibilities of a freight forwarder, CHA, shipping line and overseas agent? Explain briefly."
]

for i, prompt in enumerate(prompts, start=1):
    print(f"\n--- RUN {i} ---")
    print(f"Prompt: {prompt}")

    response = llm.invoke(prompt)

    print(f"Response: {response.content}")
