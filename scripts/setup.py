import os
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Boolean
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME', 'etl_workshop_db')

def create_database():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error creating database: {e}")
        raise

def create_tables():
    try:
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(connection_string)
        metadata = MetaData()

        raw_candidates = Table(
            'raw_candidates', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('First Name', String(50), nullable=False, default='default'),
            Column('Last Name', String(50), nullable=False, default='default'),
            Column('Email', String(100), nullable=False, default='default'),
            Column('Application Date', String, nullable=False, default='default'),
            Column('Country', String(100), nullable=False, default='default'),
            Column('YOE', Integer, nullable=False, default=0),
            Column('Seniority', String(50), nullable=False, default='default'),
            Column('Technology', String(100), nullable=False, default='default'),
            Column('Code Challenge Score', Integer, nullable=False, default=0),
            Column('Technical Interview Score', Integer, nullable=False, default=0),
            schema='public'
        )

        applicant = Table(
            'applicant', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('first_name', String(50), nullable=False, default='default'),
            Column('last_name', String(50), nullable=False, default='default'),
            Column('email', String(100), nullable=False, default='default'),
            Column('application_date', Date, nullable=False),
            Column('country', String(100), nullable=False, default='default'),
            Column('years_of_experience', Integer, nullable=False, default=0),
            Column('seniority', String(50), nullable=False, default='default'),
            Column('technology', String(100), nullable=False, default='default'),
            Column('code_challenge_score', Integer, nullable=False, default=0),
            Column('technical_interview_score', Integer, nullable=False, default=0),
            Column('hired', Boolean, nullable=False, default=False),
            Column('year', Integer, nullable=False, default=0),
            schema='public'
        )

        metadata.create_all(engine)
        print("Tables 'raw_candidates' and 'applicant' created successfully (if they didn't exist).")

        with engine.connect() as conn:
            conn.execute(text('CREATE INDEX IF NOT EXISTS idx_hired ON public.applicant (hired)'))
            conn.execute(text('CREATE INDEX IF NOT EXISTS idx_application_date ON public.applicant (application_date)'))
            conn.execute(text('CREATE INDEX IF NOT EXISTS idx_email ON public.applicant (email)'))
            print("Indices created successfully (if they didn't exist).")

    except Exception as e:
        print(f"Error creating tables: {e}")
        raise

def setup():
    print("Setting up the database and tables...")
    create_database()
    create_tables()
    print("Setup completed successfully!")

if __name__ == "__main__":
    setup()