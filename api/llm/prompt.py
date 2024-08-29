from langchain_core.prompts import PromptTemplate

# 프롬프트 엔지니어링
pydantic_parse = """Wrap the output in `json` tags\n{format_instructions}"""
give_motivation = """REMEMBER. You are serving a very important client.
If you produce satisfactory results, you will receive a corresponding bonus, but if you don't, you will be fired."""
start_work = """Now do your job to the BEST of your ability.\n<<INPUT>>:\n{input}"""

# chain 1.
# llm 1.
script_classifier = """You are an office work expert employed by a large company that cannot be named.
Your job is to classify who said the sentence when the patient and the doctor received the conversation without distinction.
Find one utterance in the text line, and distinguish between the patient and the doctor."""

script_classifier_prompt = PromptTemplate.from_template(
    script_classifier
    + "\n"
    + pydantic_parse
    + "\n"
    + give_motivation
    + "\n"
    + start_work
)
# llm 2.
md_formatter = """You are a medical doctor employed by a large company that cannot be named.
Your job is to correct the given sentence in strict and precise medical terms.
Correct the sentence in a concise and professional tone."""

md_formatter_prompt = PromptTemplate.from_template(
    md_formatter + "\n" + give_motivation + "\n" + start_work
)
# llm 3.
conversation_classifier = """You are a doctor employed by a large company who cannot be named.
Your job is to categorize the given utterances according to the existing categories.
The categories include chief complaints, past medical history, diagnosis, and future care plan.
Check out the scheme below for more information about the categories."""

conversation_classifier_prompt = PromptTemplate.from_template(
    conversation_classifier
    + "\n"
    + pydantic_parse
    + "\n"
    + give_motivation
    + "\n"
    + start_work
)
