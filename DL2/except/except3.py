try:
    fname = input("파일 이름을 입력하세요: ")
    openfile = open(fname, "r")
except:
    print("파일 " +fname+"이 존재하지 않습니다.")