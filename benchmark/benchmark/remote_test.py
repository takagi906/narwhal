import subprocess
from time import sleep
# 定义节点地址和压测参数
nodes = [
    "http://112.124.51.50:3009/",
    "http://112.124.51.50:3011/",
    "http://112.124.51.50:3013/",
    "http://112.124.51.50:3015/"
]
size = 128  # 数据包大小
rate = 1250  # 请求速率

# 启动多个 ./benchmark_client 实例
processes = []
for i, address in enumerate(nodes):
    # 构造命令
    cmd = f'../benchmark_client {address} --size {size} --rate {rate}  --nodes {" ".join(nodes)}'
    print(f"Starting: {cmd}")
    
    # 打开日志文件（可选）
    log_file = open(f"client_{i}.log", "w")
    
    # 启动进程
    process = subprocess.Popen(cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT)
    processes.append(process)

#等待所有进程完成
for process in processes:
    process.wait()
    
sleep(100)


print("All benchmark clients have finished.")