"""
Phi-Network-Monitor: أداة مراقبة الشبكة لمشروع Phi-Chain
تقوم هذه الأداة بمراقبة حالة العقد (Nodes)، سرعة إنتاج الكتل، وحالة الإجماع، بالإضافة إلى تتبع الكتل والمعاملات.
"""

import time
import json
import random
from datetime import datetime

class PhiNetworkMonitor:
    def __init__(self, nodes_count=7):
        self.nodes_count = nodes_count
        self.start_time = datetime.now()
        self.blocks_produced = 0
        self.latest_block_height = 1000 # محاكاة بدء من ارتفاع معين

    def get_network_status(self):
        """محاكاة الحصول على حالة الشبكة"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "uptime": str(datetime.now() - self.start_time),
            "active_nodes": random.randint(self.nodes_count - 1, self.nodes_count),
            "total_nodes": self.nodes_count,
            "avg_block_time": f"{random.uniform(1.5, 1.7):.2f}s",
            "consensus_health": "Optimal (Φ-Coherent)"
        }
        return status

    def get_latest_block(self):
        """محاكاة الحصول على بيانات آخر كتلة"""
        self.latest_block_height += 1
        self.blocks_produced += 1
        tx_count = random.randint(5, 50)
        block_data = {
            "height": self.latest_block_height,
            "hash": f"0x{random.getrandbits(256):064x}"[:10] + "...",
            "transactions": tx_count,
            "miner": f"Node-{random.randint(1, self.nodes_count)}",
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        return block_data

    def get_pending_transactions(self):
        """محاكاة الحصول على عدد المعاملات المعلقة"""
        return random.randint(0, 150)

    def run_monitor(self, duration_seconds=10):
        print(f"🚀 بدء مراقبة شبكة Phi-Chain (المدة: {duration_seconds} ثوانٍ)...")
        print("-" * 70)
        print(f"{'الوقت':<10} | {'العقد النشطة':<12} | {'زمن الكتلة':<10} | {'الكتلة #':<8} | {'معاملات':<8} | {'معاملات معلقة':<15}")
        print("-" * 70)
        
        elapsed = 0
        while elapsed < duration_seconds:
            status = self.get_network_status()
            block = self.get_latest_block()
            pending_tx = self.get_pending_transactions()

            print(f"{datetime.now().strftime('%H:%M:%S'):<10} | "
                  f"{status['active_nodes']}/{status['total_nodes']:<10} | "
                  f"{status['avg_block_time']:<10} | "
                  f"{block['height']:<8} | "
                  f"{block['transactions']:<8} | "
                  f"{pending_tx:<15}")
            
            time.sleep(2)
            elapsed += 2
            
        print("-" * 70)
        print(f"✅ انتهت جلسة المراقبة. تم إنتاج {self.blocks_produced} كتلة جديدة.")

if __name__ == "__main__":
    nodes_count = 7 # القيمة الافتراضية لـ F_4 في فيبوناتشي
    monitor = PhiNetworkMonitor(nodes_count)
    monitor.run_monitor(duration_seconds=10)
