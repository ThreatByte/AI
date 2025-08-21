# AI
## I wanted to share an automation script I created in my home lab to see the capabilities of using large language models in digital forensics and incident response. The script is leveraging lang chain dependencies, a framework that helps develop various applications using large language models.

## The large language model used was "Granite3.3" (IBM Foundational Model). The chat prompt highlights having decades of experience answering questions about DFIR, knowledgeable in Windows, macOS, and Linux operating systems. The task is to answer various questions about Windows, macOS, and Linux artifacts. You do not need internet access to interact with the LLM. The only time you need internet access is to download tools, dependencies, and models from Ollama. 

## Important Note:
- Be careful when downloading models. Watch out for model theft and poisoning.
- Verify models' answer to output.
- Don't use on actual data.

## Tools used:
- Python
- Ollama
- Visual Studio Code

## Dependencies:
- Lang chain
