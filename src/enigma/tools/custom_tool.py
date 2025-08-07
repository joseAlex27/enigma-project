from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
# from crewai_tools import BaseTool


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class document_parts(BaseTool):
    title:  str
    author:  str
    publication_date:  str 
    introduction: str
    methods:  str
    results: str
    conclusions: str

# class MyOwnRAGTool(BaseTool):
#     def __init__(self, vector_store):
#         super().__init__(
#             name="My Custom RAG Tool",
#             description="Busca información en documentos locales"
#         )
#         self.vector_store = vector_store

#     def _run(self, query: str) -> str:
#         results = self.vector_store.similarity_search(query)
#         return "\n".join([doc.page_content for doc in results])