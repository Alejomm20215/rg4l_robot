# rg4l_robot

## Robot project developed with:
- **Python (uv-managed)** for UI/interface + vision + calculations
- **Arduino C++** for low-level control

I'll be developing this with my coworker, Tusk; we expect the project to take a long time, so we're currently on the planning stage of the project


## Prereqs
- **Python 3.12+**
- **uv** installed (Astral)
- Arduino IDE **or** PlatformIO (optional, for `arduino/`)

## Quickstart (Python)
Create a virtual env and install deps:

```bash
uv sync
```

Run the CLI:

```bash
uv run rg4l --help
uv run rg4l status
```

Run tests:

```bash
uv run pytest
```

Lint/format:

```bash
uv run ruff check .
uv run ruff format .
```

## Repo layout
- `src/rg4l_robot/`: Python package (vision/comms/math)
- `tests/`: unit tests
- `arduino/`: Arduino C++ sketch + protocol docs
- `docs/`: additional documentation

## Next decisions (you tell me)
- Camera: **USB webcam**, **Raspberry Pi Camera**, or something else?
- Host computer: **Windows laptop**, **Raspberry Pi**, **Jetson**, etc.?
- Arduino link: **Serial over USB**, **BLE**, **Wi‑Fi**, CAN?


