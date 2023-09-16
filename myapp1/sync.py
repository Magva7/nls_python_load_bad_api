import schedule
import time
from threading import Thread
from myapp1.views import synchronize_data

def run_sync_task():
    synchronize_data()

def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

# запуск раз в час
schedule.every(1).hour.do(run_sync_task)

scheduler = Thread(target=scheduler_thread)
scheduler.start()
