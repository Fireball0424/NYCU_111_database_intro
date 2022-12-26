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
                "Connection could not be made due to the following error: \n",
                ex)

    def GetMatchingJobTitle(self):
        select_statement = '''select distinct job_title from skills_db as s natural join salary_db order by job_title asc'''
        result = self.db.execute(select_statement).fetchall()
        return result
    
    def GetJobWithTitle(self, job):
        select_statement = '''select * from salary_db where job_title = '{0}' order by monthly_salary asc'''.format(job)
        result = self.db.execute(select_statement).fetchall()
        return result
    
    def GetJobWithCompany(self, company):
        select_statement = '''select * from salary_db where company_name = '{0}' order by monthly_salary asc'''.format(company)
        result = self.db.execute(select_statement).fetchall()
        return result

    def GetJobWithSalary(self, salary):
        select_statement = '''select * from salary_db where monthly_salary = {0} order by monthly_salary asc'''.format(salary)
        result = self.db.execute(select_statement).fetchall()
        return result

    def GetJobWithLocation(self, locale):
        select_statement = '''select * from salary_db where location = '{0}' order by monthly_salary asc'''.format(locale)
        result = self.db.execute(select_statement).fetchall()
        return result


        

database = Database()
temp = database.GetJobWithCompany('Wibmo')
print(temp)


