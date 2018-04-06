import datetime

time_before_truncating = datetime.datetime.now()  # remove 6 characters from this string
time = str(time_before_truncating)[None:-7]
print time
