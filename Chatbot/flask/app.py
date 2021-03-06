
import random
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return '어서와'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지'

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020,1,1)
    result = new_year - today
    return f'<h1>더 성숙해지기까지 {result.days}일 남았습니다!</h1>'

# 인사하는 페이지
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'반갑습니다, {name}님! :)'
    return render_template('greeting.html',html_name=name)

# 세제곱 결과를 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    #return f'{number}의 세제곱의 값은 {number**3}입니다.'
    result = number ** 3
    return render_template('cube.html',number=number,result=result)

# 점심 메뉴를 골라주는 페이지
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈수육정식','고추잡채덮밥','돼지불백','샐러드','히레카츠']
    order = random.sample(menu,people)
    return str(order)


@app.route('/movie')
def movie():
    movies = ['나이브스 아웃','조커','엔드게임']
    return render_template('movie.html',movie_list=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html',age=age)

# naver 검색
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력받을 페이지를 ㄴ
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name=request.args.get('name')
    # 데이터 리스트
    first_options=['잘생김','못생김','존잘','존못','쏘쏘']
    second_options=['친절함','싹수','애교','잘난척']
    third_options=['돈복','코딩력','물욕','식욕']
    # 각 데이터 리스트별로 요소를 하나씩 무작위로 뽑음

    # sample 사용한 경우(list 형태로 들어옴)
     #tmp = random.sample(first_options,1)
     #print(tmp,type(tmp,tmp[0]))

    #choice 사용한 경우 (str형태로 들어옴)
    first = random.choice(first_options) 
    second = random.choice(second_options) 
    third = random.choice(third_options) 
 
    return render_template('godmademe.html',name=name,first=first,second=second,third=third)

# app.py 가장 하단에 위치
# 1. 앞으로 flask run으로 서버를 켜는 게 아니라, python app.py로 서버를 실행한다.
# 2. 내용이 바뀌어도 서버를 켰다 껐다 안해도 된다.
if __name__ == '__main__':
    app.run(debug=True)