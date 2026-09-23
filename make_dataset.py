import base64
import json
import os

types = ["basophil", "eosinophil", "lymphocyte", "monocyte", "neutrophil"]
data = {}

for t in types:
    if os.path.exists(t):
        data[t] = []
        for f in os.listdir(t):
            ext = f.rsplit(".", 1)[-1].lower()
            if ext in ["jpg", "jpeg", "png", "bmp"]:
                file_path = os.path.join(t, f)
                with open(file_path, "rb") as img_file:
                    b64_str = base64.b64encode(img_file.read()).decode("utf-8")
                    mime = "jpeg" if ext in ["jpg", "jpeg"] else ext
                    data[t].append(f"data:image/{mime};base64,{b64_str}")

with open("dataset.js", "w") as out:
    out.write(f"window.DATASET = {json.dumps(data)};")

print("dataset.js successfully built with embedded Base64 images!")