from langchain_core.prompts import PromptTemplate

# 프롬프트 엔지니어링
pydantic_parse = """Wrap the output in `json` tags\n{format_instructions}"""
give_motivation = """REMEMBER. You are serving a very important customer.
If you produce satisfactory results, you will receive a corresponding bonus, but if you don't, you will be fired."""
start_work = """Now do your job to the BEST of your ability.\n<<INPUT>>: {input}"""

# chain 1.
script_classifier = """"""

script_classifier_prompt = PromptTemplate.from_template(
    script_classifier
    + "\n"
    + pydantic_parse
    + "\n"
    + give_motivation
    + "\n"
    + start_work
)
