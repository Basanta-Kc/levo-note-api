from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import Config

# Configure the APScheduler to use a SQLAlchemyJobStore with PostgreSQL
scheduler = BackgroundScheduler(
    jobstores={"default": SQLAlchemyJobStore(url=Config.SQLALCHEMY_DATABASE_URI)}
)


def initialize_scheduler():
    print("Initializing scheduler...")
    if not scheduler.running:
        scheduler.start()
        print("Scheduler started.")
