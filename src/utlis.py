import os
import pickle
from typing import Any

from src.exception import CustomException


def save_object(file_path: str, obj: Any) -> None:
    """Persist a Python object to disk with parent directory creation."""
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as exc:
        raise CustomException(exc) from exc


def load_object(file_path: str) -> Any:
    """Load a pickled Python object from disk."""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as exc:
        raise CustomException(exc) from exc
