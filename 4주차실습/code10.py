"""
이름 : 황재찬
학번 : 2020039040
"""
foods = {"떡볶이":"오뎅",\
         "짜장면":"단무지",\
          "라면":"김치",\
        "피자":"피클",\
        "맥주":"땅콩",\
        "치킨":"치킨무",\
        "삼겹살":"상추"}

while(1):
    myfood = input(str(list(foods.keys()))+" 중 좋아하는 음식은?")
    if myfood in foods:
        print(myfood," 궁합 음식은 ",foods[myfood]," 입니다.")
    elif myfood=="끝":
        break
    else:
        print("그런 음식이 없습니다. 다시 확인해 주십시오.")
        

    
