from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.minute, now.second, now.hour, now.minute, now.second)
