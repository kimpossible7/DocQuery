from functools import lru_cache
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.openai import OpenAIEmbeddings


class QuestionAnsweringService:
    def __init__(self, document: str, openai_api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.vectorstore = FAISS.from_texts([document], self.embeddings)
        self.retriever = self.vectorstore.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=self.retriever)
    
    @lru_cache(maxsize=100)
    def answer_questions(self, questions: list) -> list:
        answers = []
        for question in questions:
            answer = self.qa_chain.run(question)
            answers.append({"question": question, "answer": answer})
        return answers