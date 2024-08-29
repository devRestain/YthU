from typing import List, Literal
from pydantic import BaseModel, Field


class Conversation(BaseModel):
    """Information about a conversation"""

    person: Literal["patient", "doctor"] = Field(
        description="The person who spoke the content of the conversation"
    )
    content: str = Field(description="The content of the conversation")


class Script(BaseModel):
    """Information about all the conversation"""

    content: List[Conversation]


class Treatment(BaseModel):
    """Information about a treatment"""

    cc: List[Conversation] = Field(
        description="""The reason why the patient have to get a medical encounter now. The current symptoms, problems, or conditions."""
    )
    hx: List[Conversation] = Field(
        description="""The health conditions that seem to affect current symptoms or have been experienced in the past."""
    )
    dignosis: List[Conversation] = Field(
        description="""The diagnosis of the patient's current symptoms"""
    )
    plan: List[Conversation] = Field(
        description="""The future treatment plans for the patient's symptoms"""
    )


if __name__ == "__main__":
    print(Treatment.model_json_schema())
