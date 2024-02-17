# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

user_input = '''[INST] # Lesson Plan Generation

## Subject: Science
## Grade Level: 8th
## Topic: Force

## Learning Objectives:
* ... (Aim, Need to study this chapter, Pre-requisite knowledge)

## Opening Activity:

[PROMPT] Generate an engaging and interactive opening activity to introduce the topic of Force for a 8th class in Science, focusing on activating prior knowledge and sparking curiosity.

## Instructional Activities:

[PROMPT] Describe 2-3 differentiated instructional activities that effectively deliver key content related to Force and cater to various learning styles in a 8th Science class.

## Practice Activities:

[PROMPT] Create 4-5 diverse practice exercises, including open-ended and closed-ended questions, for students to solidify their understanding of Force within Science at the 8th level.

## Assessment:

[PROMPT] Suggest 2-3 formative and summative assessment strategies that accurately evaluate student learning of Force across different skill levels in Science for 8th students.

## Differentiation:

[PROMPT] Suggest strategies for differentiating instruction and assessment to cater to diverse learners in the 8th Science class.

[/INST]'''

# user_input = []
# while True:
#     line = input()
#     if line:
#         user_input.append(line)
#     else:
        # break

print(f"User: {user_input} \n T.A.:")

history = [
    {"role": "system", "content": "You are an intelligent teaching assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": user_input},
]

while True:
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
    )


    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})