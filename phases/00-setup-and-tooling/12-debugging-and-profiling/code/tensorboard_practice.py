from datetime import datetime
from pathlib import Path

from torch.utils.tensorboard.writer import SummaryWriter


def main() -> None:
    log_root = Path(__file__).resolve().parent / "runs"
    log_dir = log_root / datetime.now().strftime("%Y%m%d_%H%M%S")
    log_root.mkdir(parents=True, exist_ok=True)

    writer = SummaryWriter(log_dir=str(log_dir))
    try:
        for step in range(1, 101):
            train_loss = 1.0 / step
            val_loss = 1.0 / step + max(0, step - 40) * 0.005

            writer.add_scalars(
                "loss",
                {"train": train_loss, "validation": val_loss},
                step,
            )
    finally:
        writer.close()

    print(f"记录完成，保存位置：{log_dir}")


if __name__ == "__main__":
    main()
