import untils
import jieba
from py2neo import Graph

## 启动命令：neo4j.bat console

# graph = Graph("http://localhost:7474", username="neo4j", password='985211')
# sql = "MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{0}' return m.name, r.name, n.name".format("苍耳中毒")
# ress = graph.run(sql).data()
# print(ress)
#

# graph = Graph("http://localhost:7474", username="neo4j", password='985211')


s="哮喘会引起结膜充血"
words=untils.Untils.SplitWord(s)
texts=[]
for word in words:

    texts.append(word)
    res=untils.Untils.JudgeType(word)
    if res!="":
        querytypes=res    ## 查询类型

print(querytypes)
print(texts)

#
# ill=dict() ## 疾病名
# texts=[]
#
# for i in range(len):
#     if(lac_result[1][i]=="n"):
#         texts.append(lac_result[0][i])
#     res=untils.Untils.JudgeType(lac_result[0][i])
#     if res!="":
#         querytypes=res    ## 查询类型
#
# ill=untils.Untils.JudgeIll(texts)
# print(ill)
# sql=untils.Untils.GetSql(ill["disease"],querytypes)
# ress = graph.run(sql).data()
# isRight=False
#
# for l in ress :
#    print(l["n.name"])
#    if l["n.name"]==ill["symptom"] :
#        isRight=True
#
# print(isRight)
