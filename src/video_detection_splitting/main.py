### solution here..
from pathlib import Path


# Read the video
def read_video(path: str): ...


# Analyse faces
def detect_faces(): ...


# Create 1 video for each face
def create_video(output_path: Path) -> str: ...
