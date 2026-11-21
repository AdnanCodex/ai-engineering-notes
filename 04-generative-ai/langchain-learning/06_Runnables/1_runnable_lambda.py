from langchain_core.runnables import RunnableLambda

word_count = RunnableLambda(lambda text: len(text.split()))
print(word_count.invoke("LangChain makes runnables easy"))
