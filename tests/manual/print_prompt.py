from lib.prompter import enriched_prompt

rsp = enriched_prompt("how is leftpad tested?")
print(rsp["answer"])
print(rsp)
