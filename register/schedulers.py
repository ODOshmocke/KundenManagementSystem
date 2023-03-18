from .functions import checking_emails
from apscheduler.schedulers import background


def start_checking_emails():
    scheduler = background.BackgroundScheduler()
    scheduler.add_job(checking_emails, 'interval', seconds=5)
    scheduler.start()
