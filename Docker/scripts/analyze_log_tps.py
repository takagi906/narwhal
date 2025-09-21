import os
import shutil

# 在Docker目录下运行 python3 ./scripts/analyze_log_tps.py

# 创建 logs 文件夹
from logs import LogParser
class LocalBench:
    def run(self):
        os.makedirs('logs', exist_ok=True)

        # 源文件路径
        src_files = [
            'validators/validator-0/logs/worker-0-0.log',
            'validators/validator-0/logs/primary-0.log',
            'validators/validator-1/logs/worker-1-0.log',
            'validators/validator-1/logs/primary-1.log',
            'validators/validator-2/logs/worker-2-0.log',
            'validators/validator-2/logs/primary-2.log',
            'validators/validator-3/logs/worker-3-0.log',
            'validators/validator-3/logs/primary-3.log',
        ]

        # 复制文件到 logs 文件夹
        for src in src_files:
            if os.path.exists(src):
                shutil.copy(src, 'logs')
            else:
                print(f'文件不存在: {src}')
        return LogParser.process('logs')

