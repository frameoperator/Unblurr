cat > deblur.py << 'ENDOFFILE'
import cv2
import numpy as np
from pathlib import Path
import sys

def sharpen_unsharp_mask(image, sigma=1.5, strength=1.5):
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)
    return cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)

def enhance_details(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    enhanced = cv2.merge([l, a, b])
    return cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

input_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('googlemaps')
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

for ext in ['.jpg', '.jpeg', '.png', '.bmp']:
    for img_file in input_dir.glob(f'*{ext}'):
        print(f"Verarbeite: {img_file.name}")
        img = cv2.imread(str(img_file))
        if img is not None:
            result = sharpen_unsharp_mask(img)
            result = enhance_details(result)
            output_path = output_dir / f"{img_file.stem}_entblurred{img_file.suffix}"
            cv2.imwrite(str(output_path), result)
            print(f"Fertig: {output_path.name}")
ENDOFFILE
