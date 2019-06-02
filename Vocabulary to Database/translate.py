import requests
from lxml import etree
import alchemy as db

words_num = db.db_session.query(db.Words).count()

for x in range(1, words_num+1):

    try:
        obj = db.db_session.query(db.Words).get(x)

        page = requests.get('http://www.youdao.com/w/' + obj.word + '/#keyfrom=dict2.top')
        selector = etree.HTML(page.content)
        means = etree.HTML(page.content).xpath('//*[@id="phrsListTab"]/div[@class="trans-container"]/ul/li/text()')
        summary = ''
        for mean in means:
            summary = summary + mean + '  &&  '

        obj.translation = summary
    except:
        print("One Word Failed")
        pass

db.db_session.commit()
db.db_session.close()