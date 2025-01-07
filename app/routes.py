from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

from app.models import SummarizeInput, SummarizeOutput
from app.services import chat_client

router = APIRouter()

examples = [
    {
        "input": "The quick brown fox jumps over the lazy dog. The dog, being lazy, did not react to the fox's antics.",
        "output": "A fox jumps over a lazy dog, which does not react."
    },
    {
        "input": "In a faraway land, there was a small village surrounded by mountains. The villagers lived a peaceful life, farming and trading with neighboring villages.",
        "output": "A small village in a mountainous region lives peacefully through farming and trading."
    },
]

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=ChatPromptTemplate.from_messages(
        [
            ('human', '{input}'),
            ('ai', '{output}')
        ]
    )
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ('system',
         'You are an expert at text summary, your task is to summarize the provided text in a concise sentence.'),
        few_shot_prompt,
        ('human', '{input}')
    ]
)

chain = final_prompt | chat_client


@router.post("/summarize")
async def summarize_endpoint(summarize_input: SummarizeInput) -> SummarizeOutput:
    response = await chain.ainvoke(summarize_input)
    output = response["content"]
    return SummarizeOutput(output=output)
