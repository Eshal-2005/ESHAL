import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import OLD
elif bit=='32bit':
    import OLD32