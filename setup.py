from pathlib import Path
from typing import List

from setuptools import find_packages, setup


HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return install requirements from the first matching requirements file."""
    candidates = [Path(file_path), Path("requirments.txt")]
    requirements_path = next((path for path in candidates if path.exists()), None)

    if requirements_path is None:
        return []

    with requirements_path.open() as file_obj:
        requirements = [line.strip() for line in file_obj if line.strip()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="UNI0908",
    version="0.1",
    author="Bhupendra Kumar",
    author_email="bs1050046@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
