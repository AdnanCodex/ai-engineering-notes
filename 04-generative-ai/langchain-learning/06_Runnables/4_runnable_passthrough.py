from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough

chain = RunnableParallel({
    "original": RunnablePassthrough(),
    "upper": RunnableLambda(lambda s: s.upper()),
})
print(chain.invoke("langchain"))
