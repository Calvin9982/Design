from pyhanlp import  *
class Untils:

    ## 判断语句中的查询类型
    def JudgeType(text):
        symptom_qwds = ['症状', '表征', '现象', '症候', '表现',"引起","会引起","会"]
        easyget_qwds = ['易感人群', '容易感染', '易发人群', '什么人', '哪些人', '感染', '染上', '得上']
        lasttime_qwds = ['周期', '多久', '多长时间', '多少时间', '几天', '几年', '多少天', '多少小时', '几个小时', '多少年']
        check_qwds = ['检查', '检查项目', '查出', '检查', '测出', '试出']
        if text in symptom_qwds:
            return "symptom_qwds"
        elif text in easyget_qwds:
            return "easyget_qwds"
        elif text in lasttime_qwds:
            return "lasttime_qwds"
        elif text in check_qwds:
            return "check_qwds"
        else:
            return ""

    ## 根据语句类型和疾病名，产生对应的SQL语句
    def GetSql(disease,type):
        if("easyget_qwds" == type):
            sql="MATCH (m:Disease) where m.name = '{0}' return m.name, m.easy_get".format(disease)

        elif("lasttime_qwds" == type):
            sql="MATCH (m:Disease) where m.name = '{0}' return m.name, m.cure_lasttime".format(disease)

        elif("check_qwds" == type):
            sql="MATCH (m:Disease)-[r:need_check]->(n:Check) where m.name = '{0}' return m.name, r.name, n.name".format(disease)

        elif("symptom_qwds" == type):
            sql="MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{0}' return m.name, r.name, n.name".format(disease)

        return sql

    def SplitWords(texts):
        res=dict()
        text=HanLP.segment(texts)
        print(text)
        for t in text:
            word=str(t.word)
            nature=str(t.nature)
            res[nature]=word
        return  res

    def PrintRes(res,isRight,symptom):
        if(isRight):
          print("该帖子不属于谣言~ ")
        else:
          print("该帖子属于谣言~  "+"原因是：在"+res[1]["m.name"]+"这种疾病中,不包含有 "+symptom+" 这种症状")

        print(res[1]["m.name"]+"这种疾病，在通常情况下可能有以下症状：",end="")

        i=0
        for r in res:
          if i==0:
           print(r["n.name"],end="")
          else:
           print("、"+r["n.name"], end="")
          i=1


if __name__ == '__main__':
     # graph = Graph("http://localhost:7474", username="neo4j", password='985211')
     # sqls=Untils.GetSql("哮喘","symptom_qwds")
     #
     # ress = graph.run(sqls).data()
     # print(ress)
     # words = Untils.SplitWord("哮喘会引起结膜充血")
     # for word in words:
     #    print(word)
     text = "哮喘的症状有睡眠呼吸暂停"
     res=Untils.SplitWords(text)


