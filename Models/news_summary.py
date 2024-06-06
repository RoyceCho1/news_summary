from typing import Literal

from pydantic import BaseModel, Field



class InputModel(BaseModel):
    latest_news: str = Field(
        default='한국에서 석유가 발견됐어',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='뉴스 3줄 요약 결과',
    )
