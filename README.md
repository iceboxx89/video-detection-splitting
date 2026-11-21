# Video Detection Splitting

## Task

Using the source video in `resources/source_video_small.mp4`, analyse the video and use an off-the-shelf face detection model to split it into multiple shorter videos, such that each split video contains the face of a character from the source video.

## Requirements

### Input

- The source video is `resources/source_video_small.mp4`.
- The solution must read the input video from this path (or accept it as a command-line argument with this as the default).

### Functional requirements

1. **Analyse the video** – detect faces in the frames of the source video.
2. **Use an off-the-shelf face detection model** – use a pre-trained, publicly available face detector (for example OpenCV's Haar cascade or DNN face detector, MediaPipe Face Detection, or RetinaFace). Do not train a custom model.
3. **Identify characters** – group detected faces so that each distinct character is recognised across the video. Each character's appearances must be assigned to that character.
4. **Split the video** – produce one output video per character (or per continuous segment) such that every split video contains the face of that character.
5. **Only relevant footage** – each split video should contain the character's face in the frames it includes; frames without that character's face should not be the main content of the split.
6. **Full face crop** – each output video must be cropped to the character's face, not the full frame. The crop must be the *full* face: the whole face region (forehead to chin, including the ears where visible) must be inside the frame, never cut off. Add a margin around the detected face box so no part of the face is clipped by detector jitter, and keep the crop stable across frames so the face does not jump around in the output.
7. **Save outputs** – write the split videos to an `output/` directory, with a clear, descriptive file name per character or segment (for example `character_1_segment_01.mp4`).

### Technical requirements

- Language: Python (the project targets Python `3.15`, see `.python-version` and `pyproject.toml`).
- Dependency management: use `uv`. Add any additional dependencies with `uv add`, so they are recorded in `pyproject.toml` and `uv.lock`.
- The existing dependency `opencv-python` may be used for video I/O and frame processing.
- The program must be runnable from the command line, e.g. `uv run video-detection-splitting`, and the `main` entry point in `src/video_detection_splitting/__init__.py` should be updated accordingly.
- Code should be clean, readable and structured into modules/functions rather than a single long script.

### Deliverables

- Working source code in `src/video_detection_splitting/`.
- The generated split videos in `output/` (or instructions to regenerate them).
- An updated `README.md` that explains:
  - how to install dependencies (`uv sync`);
  - how to run the program;
  - which face detection model was used and why;
  - any assumptions, limitations, or known failure cases (e.g. missed faces, profile views, misidentified characters).

### Evaluation criteria

- Correctness: each split video genuinely contains the face of the character it is associated with.
- Use of an off-the-shelf face detection model, applied sensibly.
- Quality and reproducibility of the code and the run instructions.
- Clear handling of edge cases and honest documentation of limitations.
