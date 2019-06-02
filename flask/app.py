from flask import Flask,request
from flask_cors import CORS
from query import insert
import json, re
import alchemy as db

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['post'])

def easy():
    param = request.get_json()
    print(param)
    print(type(param))
    print(type(param['input']))
    result = {
        'status': '',
        'data': []
    }

    if param['type'] == 1:

        easy_pattern_A = re.compile(r'^[a-zA-Z]+$')
        easy_pattern_B = re.compile(r'^\*[a-zA-Z]+$')
        easy_pattern_C = re.compile(r'^[a-zA-Z]+\*[a-zA-Z]+$')
        easy_pattern_D = re.compile(r'^[a-zA-Z]+\*$')

        if param == '' or param is None:
            result['status'] = "输入格式有误，请重新输入"

        elif re.match(easy_pattern_A, param['input']) or re.match(easy_pattern_B, param['input']) or re.match(easy_pattern_C, param['input']) or re.match(easy_pattern_D, param['input']):
            result = insert(p=param, r=result)

        else:
            result['status'] = "输入格式有误，请重新输入"

    elif param['type'] == 2:
        pattern = param['input']
        # unsup_pattern_A = re.compile(r'\*\?')
        # unsup_pattern_B = re.compile(r'\+\?')
        #
        # if re.match(pattern, unsup_pattern_A) or re.match(pattern, unsup_pattern_B):
        #     pattern = pattern.replace('*?','{0,}').replace('+?','+')

        try:

            obj = db.db_session.query(db.Words).filter(db.Words.word.op('regexp')(pattern)).all()

            if len(obj) == 0:
                result['status'] = '未查询到匹配该正则词汇'
            else:
                result['status'] = 'Succeed'
                for x in obj:
                    word = {
                        'word': x.word,
                        'unit': x.unit,
                        'translation': x.translation.split("  &&  ")[:-1]
                    }
                    result['data'].append(word)

        except Exception as e:
            print(e)
            result['status'] = '查询失败'

    else:
        result['status'] = "输入格式有误，请重新输入"

    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8002)
