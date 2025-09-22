import os
from data.models.image_classifier import classify_xray

# --- Hardcoded test image path ---
# Adjust this to match an image you already have in your project
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# IMG_PATH = os.path.join(BASE_DIR, "images", "person2_bacteria_4.jpeg")
# IMG_PATH = "C:/Users/Admin/Downloads/Medi/data/images/person2_bacteria_4.jpeg"
IMG_PATH = "C:/Users/Admin/Downloads/Medi/data/images/IM-0129-0001.jpeg"



def main():
    if not os.path.exists(IMG_PATH):
        print(f"❌ Image not found: {IMG_PATH}")
        return

    print(f"🔍 Testing image classification on: {IMG_PATH}")
    result = classify_xray(IMG_PATH)
    print("✅ Classification Result:")
    print(result)

if __name__ == "__main__":
    main()
