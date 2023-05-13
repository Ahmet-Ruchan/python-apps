import time
from plyer import notification

if __name__ == "__main__":

    notification.notify(
        title="Hey Whatsapp Dude!",
        message="This is basic notification app using with python",

        timeout=10,
    )

    time.sleep(5)
