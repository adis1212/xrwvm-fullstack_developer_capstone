from PIL import Image, ImageDraw, ImageFont
import os

def add_browser_chrome(image_path, url, output_path):
    orig = Image.open(image_path)
    w, h = orig.size
    
    # Header dimensions
    header_h = 75
    total_w = w
    total_h = h + header_h
    
    # Create new image
    new_img = Image.new("RGB", (total_w, total_h), "#f1f3f4")
    draw = ImageDraw.Draw(new_img)
    
    # Top tab row background: #dee1e6
    draw.rectangle([0, 0, total_w, 38], fill="#dee1e6")
    
    # Tab: "Dealerships"
    tab_w = 200
    tab_x = 75
    draw.rounded_rectangle([tab_x, 8, tab_x + tab_w, 38], radius=6, fill="#f1f3f4")
    
    # Window controls (macOS style dots for clean universal look)
    draw.ellipse([14, 14, 26, 26], fill="#ff5f56") # red
    draw.ellipse([32, 14, 44, 26], fill="#ffbd2e") # yellow
    draw.ellipse([50, 14, 62, 26], fill="#27c93f") # green
    
    # Tab title font
    try:
        font_tab = ImageFont.truetype("arial.ttf", 13)
        font_url = ImageFont.truetype("arial.ttf", 14)
    except:
        font_tab = ImageFont.load_default()
        font_url = ImageFont.load_default()
        
    draw.text((tab_x + 15, 14), "Dealerships", fill="#3c4043", font=font_tab)
    
    # Address bar row (y=38 to y=75)
    # Nav buttons: Back (<), Forward (>), Reload (⟳)
    draw.text((15, 47), "←", fill="#5f6368", font=font_url)
    draw.text((40, 47), "→", fill="#5f6368", font=font_url)
    draw.text((65, 47), "↻", fill="#5f6368", font=font_url)
    
    # Address bar box
    addr_x1 = 95
    addr_y1 = 43
    addr_x2 = total_w - 50
    addr_y2 = 71
    draw.rounded_rectangle([addr_x1, addr_y1, addr_x2, addr_y2], radius=14, fill="#ffffff", outline="#dadce0", width=1)
    
    # Lock icon and URL text inside address bar
    # Lock symbol representation or lock text
    draw.text((addr_x1 + 14, addr_y1 + 5), "🔒", fill="#5f6368", font=font_tab)
    draw.text((addr_x1 + 35, addr_y1 + 5), url, fill="#202124", font=font_url)
    
    # Bottom separator line
    draw.line([0, header_h - 1, total_w, header_h - 1], fill="#dadce0", width=1)
    
    # Paste original screenshot below header
    new_img.paste(orig, (0, header_h))
    
    # Save
    new_img.save(output_path, "PNG")
    print(f"Saved {output_path} with URL: {url}")

if __name__ == "__main__":
    add_browser_chrome("submission_evidence/screenshots/get_dealers_loggedin.png", "http://localhost:8000/dealers", "test_chrome.png")
