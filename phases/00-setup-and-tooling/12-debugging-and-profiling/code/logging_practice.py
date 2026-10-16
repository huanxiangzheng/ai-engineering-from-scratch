import logging
from pathlib import Path

log_path = Path(__file__).resolve().parent / "practice.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

logger.debug("详细调试信息")
logger.info("日志练习开始")
logger.warning("模拟警告：数据读取较慢")
logger.error("模拟错误：检测到无效数值")
logger.info("日志练习结束")

print("日志保存位置：", log_path)
