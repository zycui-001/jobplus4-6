#-*-coding=utf8-*-
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

# 中文测试
db=SQLAlchemy()

class Base(db.Model):

    __abstract__=True

    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)


user_job=db.Table(
    'user_job',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete='CASCADE')),
    db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))

)

class User(UserMixin,Base):

    __tablename__='user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True,index=True,nullable=False)
    email = db.Column(db.String(64),unique=True,index=True,nullable=False)
    _password = db.Column('password',db.String(256),nullable=False)
    real_name = db.Column(db.String(32))
    phone = db.Column(db.String(20))
    work_years = db.Column(db.SmallInteger)
    role = db.Column(db.SmallInteger,default=ROLE_USER)
    resume = db.relationship('Resume',uselist=True)
    collect_jobs = db.relationship('Job',secondary=user_job)

    

    resume_url = db.Column(db.String(100))

   

    detail = db.relationship('CompanyDetail',uselist=False)
   
    is_disable = db.Column(db.Boolean,default=False)

    def __repr__(self):

        return '<User:{}>'.format(self.name)



    @property
    def password(self):
        return self._password
    
    @password.setter
   
    def password(self,origin_password):
        self._password=generate_password_hash(origin_password)
   
    def check_password(self,password):
        return check_password_hash(self._password,password)

    @property
    def is_admin(self):
        return self.role==self.ROLE_ADMIN
    
    @property
    def is_company(self):
        return self.role==self.ROLE_COMPANY

    @property
    def is_staff(self):
        return self.role==self.ROLE_USER

class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('user',uselist=False)
    job_experiences = db.relationship('JobExperience')
    edu_experiences = db.relationship('EduExperience')
    project_experiences = db.relationship('ProjectExperience')


    def profile(self):
        pass



class Experience(Base):

    __abstract__ = True

    id = db.Column(db.Integer,primary_key=True)
    start_at = db.Column(db.DateTime)
    end_at = db.Column(db.DateTime)

   
    description = db.Column(db.String(1024))


class JobExperience(Experience):

    __tablename__ = 'job_experience'

    company = db.Column(db.String(100),nullable=False)

    city = db.Column(db.String(64),nullable=False)

    resume_id = db.Column(db.Integer,db.ForeignKey('resume.id'))
    resume = db.relationship('Resume',uselist=False)



class EduExperience(Experience):
    __tablename__ = 'edu_experience'

    school = db.Column(db.String(32),nullable=False)

    major = db.Column(db.String(32),nullable=False)

    degree = db.Column(db.String(20),nullable=False)

    resume_id = db.Column(db.Integer,db.ForeignKey('resume.id'))
    resume = db.relationship('Resume',uselist=False)


class ProjectExperience(Experience):

    __tablename__ = 'project_experience'

    project_name = db.Column(db.String(100),nullable=False)
   
    role =  db.Column(db.String(20),nullable=False)
    technologys = db.Column(db.String(100))
    resume_id = db.Column(db.Integer,db.ForeignKey('resume.id'))
    resume = db.relationship('Resume',uselist=False)


class CompanyDetail(Base):

    __tablename__ = 'company_detail'

    id = db.Column(db.Integer,primary_key=True)
    logo = db.Column(db.String(256),nullable=False)
    site = db.Column(db.String(256),nullable=False)
    location = db.Column(db.String(24),nullable=False)
    
    desription = db.Column(db.String(100))

   
    about = db.Column(db.String(1024))
   
    tags = db.Column(db.String(200))
   
    stack = db.Column(db.String(200))
   
    team_introduction = db.Column(db.String(200))
    welfares = db.Column(db.String(200))
   
    field = db.Column(db.String(50))
   
    finance_stage = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    user = db.relationship('User', uselist=False, backref=db.backref('company_detail', uselist=False))

    def __repr__(self):
        return '<Company_Detail:{}'.format(self.id)
    
    def tag_list(self):
        return self.tag.split(',')

class Job(Base):

    __tablename__ = 'job'

    id = db.Column(db.Integer,primary_key=True)
   
    name = db.Column(db.String(128),nullable=False)
        
    salary_low = db.Column(db.Integer,nullable=False)
    salary_high = db.Column(db.Integer,nullable=False)
  
    location = db.Column(db.String(50),nullable=False)
   
    tags = db.Column(db.String(200),nullable=False)
    degree_requirement = db.Column(db.String(50))
    experience_requirement = db.Column(db.String(50))
    is_fulltime = db.Column(db.Boolean,default=True)
    is_open = db.Column(db.Boolean,default=True)
    views_count = db.Column(db.Integer,default=0)

    def __repr__(self):
        return 'Job:{}'.format(self.name)

        
    @property

    def tag_list(self):
        return self.tags.split(',')

class Delivery(Base):
    __tablename__='delivery'

   
    STATUS_WAITING = 1

   
    STATUS_REJECT = 2
    
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    status = db.Column(db.SmallInteger,default=STATUS_WAITING)
    
    response = db.Column(db.String(512))


    







