import shutil

total, used, free = shutil.disk_usage("/")

print("Total Space: %.2f GB" % (total / (1024**3)))

print("Used Space : %.2f GB" % (used / (1024**3)))

print("Free Space : %.2f GB" % (free / (1024**3)))
