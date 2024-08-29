from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai.llms import OpenAI
from api.utils.model_schema import Conversation, Script, Treatment
from api.llm.prompt import (
    script_classifier_prompt,
    md_formatter_prompt,
    conversation_classifier_prompt,
)

llm = OpenAI(temperature=0.1)


# chain 1. 녹취 스크립트를 과거력 파일로 변환
def convert_record_to_tx(raw_file: str) -> Treatment:

    # llm 1. 스크립트를 두 세력의 대화로 분류
    def generate_script(raw_file: str) -> Script:
        conv_parser = PydanticOutputParser(pydantic_object=Script)
        conv_prompt = script_classifier_prompt.partial(
            format_instructions=conv_parser.get_format_instructions()
        )
        chain_gen_script = conv_prompt | llm | conv_parser
        return chain_gen_script.invoke({"input": raw_file})

    # llm 2. 각 카테고리에 삽입된 대화 내용을 전문적인 용어로 편집
    def format_by_md(script: Script) -> Script:
        chain_format_by_md = md_formatter_prompt | llm
        return Script(
            [
                Conversation(
                    {
                        "content": chain_format_by_md.invoke(
                            {"input": conv.content}
                        ).content,
                        "person": conv.person,
                    }
                )
                for conv in script
            ]
        )

    # llm 3. 대화 파일을 보고 정해진 카테고리에 대화 내용을 삽입 - pydantic bind
    def generate_treatment(script: Script) -> Treatment:
        tx_parser = PydanticOutputParser(pydantic_object=Treatment)
        tx_prompt = conversation_classifier_prompt.partial(
            format_instructions=tx_parser.get_format_instructions()
        )
        chain_gen_tx = tx_prompt | llm | tx_parser
        return chain_gen_tx.invoke({"input": script})

    # llm 4. 대화 파일에서 추가할 수 있는 사항 없는지 재확인.

    # final chain 생성
    chain_num_first = (
        RunnableLambda(generate_script)
        | RunnableLambda(format_by_md)
        | RunnableLambda(generate_treatment)
    )
    return chain_num_first.invoke({"raw_file": raw_file})
