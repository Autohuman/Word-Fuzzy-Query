import re
import alchemy as db

file = open('vocabulary.txt', 'r')

pattern_unit = re.compile(r'^#.*')
pattern_space = re.compile(r'\s')
pattern_word = re.compile(r'[a-z]*')
word_unit = "Unknown"

for line in file.readlines():

    if re.match(pattern_unit, line):
        word_unit = line.replace('#','')
        print(word_unit)

    elif re.match(pattern_space, line):
        pass

    elif re.match(pattern_word, line):
        new_word = db.Words(
            word = line.strip(),
            unit = word_unit
        )
        try:
            db.db_session.add(new_word)
        except Exception as e:
            print(e)
    else:
        print(line)
        print("错误错误错误")

try:
    db.db_session.commit()
    db.db_session.close()
    print("Add Vocabulary succeed")
except Exception as e:
    print(e)