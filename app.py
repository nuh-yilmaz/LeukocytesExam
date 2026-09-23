import os
import sys
import webview


def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.abspath(".")


if __name__ == "__main__":
    base_dir = get_base_path()
    index_path = os.path.join(base_dir, "index.html")

    window = webview.create_window(
        "Leukocyte Exam", index_path, width=500, height=750, resizable=True
    )
    webview.start()