from datetime import datetime
import os

now = datetime.now()

yy = now.year
mm = now.month
dd = now.day

dir_name = "{}{}{}".format(yy, mm, dd)

os.mkdir(dir_name)