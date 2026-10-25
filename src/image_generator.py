import requests
import urllib.parse

def generate_cartoon_image(prompt, output_path):
    # This locks in the look of Candy and Titu
    character_base = "A cute 2D cartoon illustration for kids. Candy is a 4-year-old girl with a red bow and yellow dress. Titu is a 2-year-old boy with a blue t-shirt and brown shorts. "
    full_prompt = character_base + prompt + ", children's book style, vibrant colors, flat vector art, simple background."
    
    encoded_prompt = urllib.parse.quote(full_prompt)
    # seed=42 keeps the characters looking exactly the same every time
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed=42&width=1920&height=1080&nologo=true"
    
    print(f"Generating image for: {prompt}")
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Image saved: {output_path}")
            return True
    except Exception as e:
        print(f"❌ Error: {e}")
    return False
