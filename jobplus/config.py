class BaseConfig(object):
	""" base BaseConfig """
	SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
	""" DevelopmentConfig """
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/devjobplus?charset=utf8'

class ProductionConfig(BaseConfig):
	""" ProductionConfig """
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

configs = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}

