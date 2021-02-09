import untils
from py2neo import Graph
from pyhanlp import *

## 启动命令：neo4j.bat console

s=input()
res=untils.Untils.SplitWords(s)
words=HanLP.segment(s)
querytypes=""
for word in words:
    types=untils.Untils.JudgeType(word.word)
    if types!="":
        querytypes=types

sql=untils.Untils.GetSql(res["disease"],querytypes)
graph = Graph("http://localhost:7474", username="neo4j", password='985211')

isRight=False

queryRes = graph.run(sql).data()

print(res["symptom"])
for r in queryRes:
    if res["symptom"]==r["n.name"] :
        isRight=True

untils.Untils.PrintRes(queryRes,isRight,res["symptom"])
