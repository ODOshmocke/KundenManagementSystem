import time
import datetime
from .emails import send_mails

def checking_emails():
    time.sleep(1)
    from .models import UserInformation
    from backend.models import Changes

    all_changes = Changes.objects.filter().all()
    all_users = UserInformation.objects.filter().all()

    if len(all_changes) != 0:

        for user in all_users:

            for key, send in user.gesendet.items():

                if send == False:
                    print(key)


                    obj = Changes.objects.get(id=key)

                    print(obj.email_text)


'''
        for information in all_changes:

            date = user.erstellt + datetime.timedelta(days=information.email_zeit)

            if date.date() == datetime.datetime.now().date():
                print(user)
                send_mails(user)
'''



