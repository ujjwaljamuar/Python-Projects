from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
account_sid = 'AccountSid'
auth_token = 'AuthToken'
client = Client(account_sid, auth_token)


def send():
    message = client.messages.create(
        from_='whatsapp:8809945696',
        body='LOl',
        to='whatsapp:7903718939'
    )


sched = BlockingScheduler()
sched.add_job(send, 'interval', seconds=5)
sched.start()