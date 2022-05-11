def nationCompare(xlabel, ylabel):
    '''산점도 그래프와 선 그래프를 통해 두 값의 국가별 평균 수치 비교'''
    print("국가별 %s vs %s" %(xlabel,ylabel))
    # 산점도 그래프 그리기
    df= cd.makesameDf(datadict[xlabel], datadict[ylabel],xlabel,ylabel)
    graphs.plotScatter(xlabel,ylabel,df,"국가별")

    same_country = cd.findSame(datadict[xlabel], datadict[ylabel])
    lists = cd.makesameList(datadict[xlabel], datadict[ylabel])
    
    # 선 그래프 그리기
    graphs.plotLine(same_country,same_country,lists,["국가별",xlabel,ylabel])  

# 전처리 파일이 있는 경우에만 실행 가능
try:
    import graphs
    import compareData as cd
    import pandas as pd
    
    edu_cost = pd.read_csv("./교육단계별_연간_학생1인당_공교육비_전처리.csv", encoding = 'utf-8')
    student_score = pd.read_csv("./학업_성취도_전처리.csv",encoding='utf-8')
    patent_enroll = pd.read_csv("./주요국_특허_등록_전처리.csv",encoding='utf-8')
    patent_receipt = pd.read_csv("./주요국_특허_출원_전처리.csv",encoding='utf-8')
    RD_researcher = pd.read_csv("./100만명당_RD_연구개발자_전처리.csv", encoding = 'utf-8')
    total_researcher = pd.read_csv("./총연구원_수_전처리.csv", encoding = 'utf-8')

    # 국가를 index로 변경
    edu_cost.set_index("국가별", inplace = True)
    student_score.set_index("국가별", inplace = True)
    patent_enroll.set_index("국가별", inplace = True)
    patent_receipt.set_index("국가별", inplace = True)
    RD_researcher.set_index("국가별", inplace = True)
    total_researcher.set_index("국가별", inplace = True)

    datadict = {"공교육비":edu_cost,"학업 성취도":student_score,"특허 출원수": patent_receipt, "특허 등록수": patent_enroll, "RD 연구원수": RD_researcher, "총 연구원수": total_researcher}

    # 비교할 데이터 두 가지 고르고 그래프 그리기 (오류 4번까지 가능)
    trying = 0
    conti = '네'
    while conti=='네':
        trying = 0 # 오류 횟수 초기화
        print("비교 가능한 데이터 목록:",list(datadict.keys()))

        terminated= False
        while not terminated:
            try:
                val1 = input("비교할 데이터를 선택하세요 (첫 번째): ")
                if val1 not in list(datadict.keys()):
                    raise ValueError()
                terminated = True

            except ValueError:
                trying += 1
                print("비교 가능한 데이터가 아닙니다.")
                if trying >= 4:
                    print("시도 가능 횟수를 초과하여 분석을 종료합니다.")
                    terminated = True

        terminated2 = False            
        while not terminated2 and trying<4:
            try:
                val2 = input("비교할 데이터를 선택하세요 (두 번째): ")
                if val2 not in list(datadict.keys()) or val2 == val1:
                    raise ValueError()
                terminated2 = True
        
            except ValueError:
                trying += 1
                print("비교 가능한 데이터가 아닙니다.")
                if trying >= 4:
                    print("시도 가능 횟수를 초과하여 분석을 종료합니다.")
                    terminated2 = True

        if trying<4:    
            nationCompare(val1,val2)
        
        print()
        conti = input("계속 진행하시겠습니까? ('네' 입력시 계속): ")
        print()
        
except FileNotFoundError:
    print("전처리 파일을 찾을 수 없습니다. 전처리 프로그램을 실행 후 다시 실행하십시오")

except ModuleNotFoundError:
    print("프로그램 실행을 위한 모듈이 설치되어있지 않습니다. 필요한 라이브러리를 설치하고 다시 실행하십시오")
    

  


    





    



