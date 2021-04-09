import datetime


def get_local_time():
    return datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
