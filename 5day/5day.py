import psutil
cpu=psutil.cpu_freq()
print(cpu)

cpu_core=psutil.cpu_count(logical=False)
print(cpu_core)

memory=psutil.virtual_memory()
print(memory)

disk=psutil.disk_partitions()
print(disk)

net=psutil.net_io_counters()
print(net)

cpu_current_ghz=round(cpu.current/1000,2)
print(f"cpu 속도: {cpu_current_ghz}GHz")

print(f"코어: {cpu_core}개")

memory_total=round(memory.total/1024**3)
print(f"메모리: {memory_total}GB")

for p in disk:
    print(p.mountpoint,p.fstype,end='')
    du=psutil.disk_usage(p.mountpoint)
    disk_total=round(du.total/1024**3)
    print(f"디스크 크기: {disk_total}GB")

sent=round(net.bytes_sent/1024**2,1)
recv=round(net.bytes_recv/1024**2,1)
print(f"보내기: {sent}MB 받기: {recv}MB")