import sys
import shutil
import argparse
from pathlib import Path
import cv2
from txture.loaders import load_lut
from txture.ascii_render import frame_to_ascii

BASE = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image", help="input image path")
    ap.add_argument(
        "--lut",
        default=str(
            BASE
            / "data"
            / "metrics"
            / "ascii_punctuation_only__DejaVuSansMono-Bold_16.json"
        ),
    )
    ap.add_argument("--cols", type=int, default=0, help="if 0 auto-detect")
    ap.add_argument("--aspect", type=float, default=2.0)
    ap.add_argument("--color", action="store_true")
    args = ap.parse_args()

    img_path = Path(args.image)

    if not img_path.exists():
        print(f"[error] not found: {img_path}")
        sys.exit(1)

    lut = load_lut(Path(args.lut))

    bgr = cv2.imread(str(img_path))
    if bgr is None:
        print(f"[error] failed to read: {img_path}")
        sys.exit(1)

    if args.cols > 0:
        cols = args.cols
    else:
        cols = max(20, shutil.get_terminal_size((80, 24)).columns - 2)

    lines, colors = frame_to_ascii(
        bgr, lut, cols=cols, char_aspect=args.aspect, colorize=args.color
    )

    sys.stdout.write("\x1b[2J")
    sys.stdout.write("\x1b[H")
    if args.color and colors is not None:
        out_lines = []
        for y, line in enumerate(lines):
            segs = []
            for x, ch in enumerate(line):
                r, g, b = colors[y][x]
                segs.append(f"\x1b[38;2;{r};{g};{b}m{ch}")
            out_lines.append("".join(segs) + "\x1b[0m")
        sys.stdout.write("\n".join(out_lines) + "\n")
    else:
        for line in lines:
            sys.stdout.write(line + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
