from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, Integer
from sqlalchemy.orm import sessionmaker

class Database:

    user = 'postgres'
    password = '12345678'
    host = 'database-1.cbixtilkjhc6.ap-northeast-1.rds.amazonaws.com'
    port = 5432
    dbname = 'db_test'
    session = None

    def __init__(self):

        try:
            # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE

            self.db = create_engine(
                url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
                    self.user, self.password, self.host, self.port,
                    self.dbname))
            print(
                f"Connection to the {self.host} for user {self.user} created successfully."
            )

            #setup schema of table
            self.meta = MetaData(self.db)
            self.salary_db = Table('salary_db', self.meta, 
                               Column('job_title', String),
                               Column('company_name', String),
                               Column('monthly_salary', Integer),
                               Column('location', String),
                               Column('salary_id', Integer))
            self.skills_db = Table('skills_db', self.meta,
                                     Column('job_title', String),
                                     Column('skill', String))

            Session = sessionmaker(bind=self.db)
            self.session = Session()

        except Exception as ex:
            print(
                "Connection could not be made due to the following error: \n", ex)

    def GetMatchingJobTitle(self):
        result = []
        select_statement = '''select distinct job_title from skills_db as s natural join salary_db order by job_title asc'''
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result
    
    def GetJobWithTitle(self, job):
        result = []
        select_statement = '''select * from salary_db where job_title = '{0}' order by monthly_salary asc'''.format(job)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result
    
    def GetJobWithCompany(self, company):
        result = []
        select_statement = '''select * from salary_db where company_name = '{0}' order by monthly_salary asc'''.format(company)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result

    def GetJobWithSalary(self, salary):
        result = []
        select_statement = '''select * from salary_db where monthly_salary = {0} order by monthly_salary asc'''.format(salary)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result

    def GetJobWithLocation(self, locale):
        result = []
        select_statement = '''select * from salary_db where location = '{0}' order by monthly_salary asc'''.format(locale)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result

    def GetJobWithOneMatchingSkill(self, skill):
        result = []
        select_statement = '''select distinct job_title from skills_db where skill = '{0}' order by job_title asc'''.format(skill)
        #print(select_statement)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result
    
    def GetJobWithMultipleSkills(self, json):
        params = "("
        skills = []
        result = []
        for key, val in json.items():
            #print('val: ', val)
            skills.append(val)
        for index, words in enumerate(skills):
            if index != len(skills) - 1:
                params = params + "'{0}', ".format(words)
            else:
                params = params + "'{0}')".format(words)
        select_statement = '''select * from (select distinct job_title from skills_db where skill in {0}) as j natural join salary_db order by monthly_salary desc limit 10'''.format(params)
        temp = self.db.execute(select_statement).fetchall()
        for row in temp:
            result.append(dict(row))
        return result

    def GetJobWithMultipleSkillsProMax(self, json):
        skills_params = "("
        location_params = "("
        skills = []
        location = []
        salary = []
        result = []
        point = 0
        locations = {"2" : "New Delhi", "3" : "Bangalore", "4" : "pune", "5" : "Chennai" , "6" : "Kolkata", "7" : "Mumbai", "8" : "Hyperabad", "9" : "Madhya Pradesh", "10" : "Kerala", "11" : "Jaipur"}
        
        if json != None : 
            for key, value in json.items():
                if point <= 1:
                    salary.append(value)
                elif 1 < point <= 11:
                    if value == "true":
                        location.append(locations["{0}".format(point)])
                elif point > 11:
                    skills.append(value)
                point += 1

            for index, words in enumerate(location):
                if index != len(location) - 1:
                    location_params = location_params + "'{0}', ".format(words)
                else:
                    location_params = location_params + "'{0}')".format(words)

            for index, words in enumerate(skills):
                if index != len(skills) - 1:
                    skills_params = skills_params + "'{0}', ".format(words)
                else:
                    skills_params = skills_params + "'{0}')".format(words)
            
            select_statement = '''select * from (select distinct job_title from skills_db where skill in {0}) as j natural join salary_db where location in {1} and monthly_salary >= {2} and monthly_salary <= {3} order by monthly_salary asc'''.format(skills_params, location_params, salary[0], salary[1])
            temp = self.db.execute(select_statement).fetchall()
            for row in temp:
                result.append(dict(row))
        return result

