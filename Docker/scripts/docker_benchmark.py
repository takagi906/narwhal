import subprocess
from time import sleep
# 定义节点地址和压测参数
nodes = [
    "http://worker_0:4001/",
    "http://worker_1:4001/",
    "http://worker_2:4001/",
    "http://worker_3:4001/"
]
size = 512  # 数据包大小
rate = 280000  # 请求速率

# 启动多个 ./benchmark_client 实例
processes = []
rates = [0.9, 0.03, 0.03, 0.03]
for i, address in enumerate(nodes):
    # 构造命令
    rate_i = int(rate * rates[i])
    cmd = f'./benchmark_client {address} --size {size} --rate {rate_i}  --nodes {" ".join(nodes)}'
    print(f"Starting: {cmd}")
    
    # 打开日志文件（可选）
    log_file = open(f"logs/client-{i}.log", "w")
    
    # 启动进程
    process = subprocess.Popen(cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT)
    processes.append(process)

#等待所有进程完成
for process in processes:
    process.wait()


print("All benchmark clients have finished.")