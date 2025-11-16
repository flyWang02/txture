import platform


def detect_os() -> str:
    name = platform.system()
    if name == "Darwin":
        return "mac"
    if name == "Windows":
        return "windows"
    if name == "Linux":
        return "linux"
    return "other"


def backend_candidates(os_name: str) -> list[str]:
    if os_name == "mac":
        return ["avfoundation", "cv2"]
    if os_name == "windows":
        return ["dshow", "cv2"]
    if os_name == "linux":
        return ["v4l2", "cv2"]
    return ["cv2"]
