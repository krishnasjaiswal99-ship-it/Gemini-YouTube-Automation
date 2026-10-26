import shutil
import os

def generate_cartoon_image(prompt, output_path):
    assets_dir = "assets"
    # Sort the images by number (1.jpg, 2.jpg, etc.)
    image_files = sorted([f for f in os.listdir(assets_dir) if f.endswith(('.jpg', '.png', '.jpeg'))], key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    
    if not image_files:
        print("❌ No images found in assets folder!")
        return False
        
    try:
        # Extract slide number from the path (e.g., temp_cartoon_1.jpg -> 1)
        slide_num = int(str(output_path).split('_')[-1].split('.')[0])
        # Pick an image from your folder
        selected_image = image_files[(slide_num - 1) % len(image_files)]
        source_path = os.path.join(assets_dir, selected_image)
        
        shutil.copy(source_path, output_path)
        print(f"✅ Using local image {selected_image} for: {prompt}")
        return True
    except Exception as e:
        print(f"❌ Error selecting local image: {e}")
        return False
