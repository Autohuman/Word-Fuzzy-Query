import alchemy as db

def insert(p, r):
    try:
        pattern = '^' + p['input'].replace('*', '[a-zA-Z]{0,}') + '$'
        print(pattern)
        obj = db.db_session.query(db.Words).filter(db.Words.word.op('regexp')(pattern)).all()

        if len(obj) == 0:
            r['status'] = '未查询到该格式词汇'
        elif len(obj) == 1:
            r['status'] = 'Succeed'
            word = {
                'word': obj[0].word,
                'unit': obj[0].unit,
                'translation': obj[0].translation.split("  &&  ")[:-1]
            }
            r['data'].append(word)
        else:
            r['status'] = 'Succeed'
            for x in obj:
                word = {
                    'word': x.word,
                    'unit': x.unit,
                    'translation': x.translation.split("  &&  ")[:-1]
                }
                r['data'].append(word)

    except Exception as e:
        print(e)
        r['status'] = '查询失败'

    return r
