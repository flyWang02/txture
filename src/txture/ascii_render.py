import cv2
import numpy as np


def frame_to_ascii(
    frame_bgr,
    lut: list[str],
    cols: int,
    char_aspect: float = 2.0,
    colorize: bool = False,
) -> list[str]:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    rows = max(1, int(cols * h / w / char_aspect))

    small_gray = cv2.resize(gray, (cols, rows), interpolation=cv2.INTER_AREA)

    mapped = np.vectorize(lambda v: lut[int(v)])(small_gray)

    lines = ["".join(row) for row in mapped]

    if not colorize:
        return lines, None

    small_bgr = cv2.resize(
        frame_bgr, (cols, rows), interpolation=cv2.INTER_AREA
    )
    small_rgb = cv2.cvtColor(small_bgr, cv2.COLOR_BGR2RGB)
    color = small_rgb.tolist()

    return lines, color
