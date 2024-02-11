from datetime import datetime

def convert(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()