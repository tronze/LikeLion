import string

from random import choice

from django.utils import timezone

def custom_path(instance, filename):
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    date = timezone.localdate()
    return '%s/%s/%s/%s.%s' % (date.year, date.month, date.day, pid, extension)

