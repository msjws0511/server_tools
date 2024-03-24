import psutil

def get_sys_info():
    virtual_memory = psutil.virtual_memory()

    total_memory = virtual_memory.total // (1024*1024)

    disk_usage = psutil.disk_usage('/')

    total_disk_space = disk_usage.total // (1024*1024*1024)
    free_disk_space = disk_usage.free // (1024*1024*1024)
    free_disk_percent = disk_usage.percent

    res={'memory':total_memory,'total_disk_space':total_disk_space,'free_disk_space':free_disk_space,'free_disk_percent':free_disk_percent}
    return res