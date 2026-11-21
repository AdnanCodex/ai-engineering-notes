from langchain_core.runnables import RunnableLambda, RunnableParallel

parallel = RunnableParallel({
    "upper": RunnableLambda(lambda s: s.upper()),
    "length": RunnableLambda(len),
})
print(parallel.invoke("langchain"))
