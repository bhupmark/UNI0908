import logging
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


logging.basicConfig(
    filename=str(LOG_FILE),
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


logger = logging.getLogger("srcLogger")
