from langchain_core.runnables import RunnableBranch, RunnableLambda

branch = RunnableBranch(
    (lambda x: x > 100, RunnableLambda(lambda x: "big")),
    (lambda x: x > 10, RunnableLambda(lambda x: "medium")),
    RunnableLambda(lambda x: "small"),
)
print([branch.invoke(n) for n in (5, 50, 500)])
