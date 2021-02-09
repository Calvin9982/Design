from py2neo import Graph
import jieba
class Untils:

    ## 判断词语中属于疾病里的什么东西
    def JudgeIll(texts):
        type= dict()
        check_list = []
        deny_list=[]
        department_list=[]
        drug_list=[]
        food_list=[]
        producer_list=[]
        symptom_list=[]
        disease_list=[]

        file = open("dict/check.txt", encoding="utf-8").readlines()
        for f in file:
            check_list.append(f.strip("\n"))

        file = open("dict/deny.txt", encoding="utf-8").readlines()
        for f in file:
            deny_list.append(f.strip("\n"))

        file = open("dict/department.txt", encoding="utf-8").readlines()
        for f in file:
            department_list.append(f.strip("\n"))

        file = open("dict/disease.txt", encoding="utf-8").readlines()
        for f in file:
            disease_list.append(f.strip("\n"))

        file = open("dict/drug.txt", encoding="utf-8").readlines()
        for f in file:
            drug_list.append(f.strip("\n"))

        file = open("dict/food.txt", encoding="utf-8").readlines()
        for f in file:
            food_list.append(f.strip("\n"))

        file = open("dict/producer.txt", encoding="utf-8").readlines()
        for f in file:
            producer_list.append(f.strip("\n"))

        file = open("dict/symptom.txt", encoding="utf-8").readlines()
        for f in file:
            symptom_list.append(f.strip("\n"))

        for text in texts:
            if text in check_list:
                type["check"]=text
            if text in deny_list:
                type["deny"]=text
            if text in department_list:
                type["department"] = text
            if text in disease_list:
                type["disease"] = text
            if text in drug_list:
                type["drug"]=text
            if text in food_list:
                type["food"] = text
            if text in producer_list:
                type["producer"] = text
            if text in symptom_list:
                type["symptom"] = text
        return type

    ## 判断语句中的查询类型
    def JudgeType(text):
        symptom_qwds = ['症状', '表征', '现象', '症候', '表现',"引起","会引起"]
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

    ## 进行分词
    def SplitWord(text):
        jieba.load_userdict("dict/check.txt")
        jieba.load_userdict("dict/deny.txt")
        jieba.load_userdict("dict/department.txt")
        jieba.load_userdict("dict/disease.txt")
        jieba.load_userdict("dict/drug.txt")
        jieba.load_userdict("dict/food.txt")
        jieba.load_userdict("dict/producer.txt")
        jieba.load_userdict("dict/symptom.txt")
        res=jieba.cut(text)
        return res



if __name__ == '__main__':
     # graph = Graph("http://localhost:7474", username="neo4j", password='985211')
     # sqls=Untils.GetSql("哮喘","symptom_qwds")
     #
     # ress = graph.run(sqls).data()
     # print(ress)
     words = Untils.SplitWord("哮喘会引起结膜充血")
     for word in words:
        print(word)

