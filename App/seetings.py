
def get_db_uri(dbinfo):
    ENGING = dbinfo.get('ENGING') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'root'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    DB = dbinfo.get('DB') or 'db'
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGING,DRIVER,USER,PASSWORD,HOST,PORT,DB)





class Config():
    DEBUG = False
    TESTING = False

    SECRET_KEY='JKLKLKLIOIJJFDANNKCJIEOIEOEWFW'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    DATABASE={
        'ENGING':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'rock1204',
        'HOST':'localhost',
        'PORT':'3306',
        'DB':'Python1803FlaskAXF'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)



envs={
    'develop':DevelopConfig
}