from dotenv import load_dotenv

load_dotenv()  # loads OPENAI_API_KEY from the .env file in the repo root

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel

classify = PromptTemplate.from_template(
    "Classify the sentiment of this feedback as 'positive' or 'negative'. One word only.\n{feedback}"
) | model | parser
positive = PromptTemplate.from_template("Write a thank-you reply to: {feedback}") | model | parser
negative = PromptTemplate.from_template("Write an apologetic reply to: {feedback}") | model | parser

branch = RunnableBranch(
    (lambda x: "positive" in x["sentiment"].lower(), positive),
    (lambda x: "negative" in x["sentiment"].lower(), negative),
    RunnableLambda(lambda x: "Could not determine sentiment"),
)
chain = RunnableParallel({"sentiment": classify, "feedback": lambda x: x["feedback"]}) | branch
print(chain.invoke({"feedback": "The delivery was late and the box was damaged."}))
