#coding:utf-8
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker,relationship

#设置一系列的基本参数
Base = declarative_base()
DB_CONNECT_STR = "mysql+pymysql://root:@localhost:3306/English?charset=utf8"
engine = create_engine(DB_CONNECT_STR,encoding="utf8",convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


class Words(Base):
    __tablename__ = 'words'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer,primary_key=True,autoincrement=True)
    word = Column(String(255),nullable=False)
    unit = Column(String(255),nullable=False)
    translation = Column(String(255),nullable=True)


#创建全部表的主函数
def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
