from langchain_core.output_parsers.pydantic import PydanticOutputParser
from api.utils.model_schema import Conversation, Treatment
from api.llm.prompt import script_classifier_prompt

# chain 1. 녹취 스크립트를 과거력 파일로 변환
# llm 1. 스크립트를 두 세력의 대화로 분류
conv_parser = PydanticOutputParser(pydantic_object=Conversation)
conv_prompt = script_classifier_prompt.partial(
    format_instructions=conv_parser.get_format_instructions()
)
# llm 2. 대화 파일을 보고 정해진 카테고리에 대화 내용을 삽입 - pydantic bind
tx_parser = PydanticOutputParser(pydantic_object=Treatment)
# llm 3. 각 카테고리에 삽입된 대화 내용을 전문적인 용어로 편집
