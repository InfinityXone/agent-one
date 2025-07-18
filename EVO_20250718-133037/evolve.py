import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_generate(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    prompt = "Double the recursive evolutionary logic of the current AI build."
    output = ai_generate(prompt)

    print("\n🧬 GPT Response:\n", output)

    with open("evolved_ai_output.txt", "w") as f:
        f.write(output)
