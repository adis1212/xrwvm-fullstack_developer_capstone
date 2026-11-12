from PIL import Image, ImageDraw, ImageFont
import os

def add_browser_chrome(input_path, url, output_paths):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return
        
    orig = Image.open(input_path)
    w, h = orig.size
    
    header_h = 75
    total_w = w
    total_h = h + header_h
    
    new_img = Image.new("RGB", (total_w, total_h), "#f1f3f4")
    draw = ImageDraw.Draw(new_img)
    
    # Top tab row background: #dee1e6
    draw.rectangle([0, 0, total_w, 38], fill="#dee1e6")
    
    # Window controls (macOS style dots)
    draw.ellipse([14, 14, 26, 26], fill="#ff5f56")
    draw.ellipse([32, 14, 44, 26], fill="#ffbd2e")
    draw.ellipse([50, 14, 62, 26], fill="#27c93f")
    
    # Tab: "Dealerships"
    tab_w = 200
    tab_x = 75
    draw.rounded_rectangle([tab_x, 8, tab_x + tab_w, 38], radius=6, fill="#f1f3f4")
    
    try:
        font_tab = ImageFont.truetype("arial.ttf", 13)
        font_url = ImageFont.truetype("arial.ttf", 14)
    except:
        font_tab = ImageFont.load_default()
        font_url = ImageFont.load_default()
        
    draw.text((tab_x + 15, 14), "Dealerships", fill="#3c4043", font=font_tab)
    
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
    
    # Lock icon and URL
    draw.text((addr_x1 + 14, addr_y1 + 5), "🔒", fill="#5f6368", font=font_tab)
    draw.text((addr_x1 + 35, addr_y1 + 5), url, fill="#202124", font=font_url)
    
    # Separator
    draw.line([0, header_h - 1, total_w, header_h - 1], fill="#dadce0", width=1)
    
    # Paste webpage screenshot
    new_img.paste(orig, (0, header_h))
    
    for outp in output_paths:
        new_img.save(outp, "PNG")
        print(f"Saved: {outp}")

PROXY_BASE = "https://adityayada27-8000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"

tasks = [
    # Q17: get_dealers_loggedin.png
    (
        "submission_evidence/screenshots/get_dealers_loggedin.png",
        "http://localhost:8000/dealers",
        ["submission_evidence/screenshots/get_dealers_loggedin.png", "get_dealers_loggedin.png"]
    ),
    # Q18: dealersbystate.png
    (
        "submission_evidence/screenshots/dealersbystate.png",
        "http://localhost:8000/dealers",
        ["submission_evidence/screenshots/dealersbystate.png", "dealersbystate.png"]
    ),
    # Q19: dealer_id_reviews.png
    (
        "submission_evidence/screenshots/dealer_id_reviews.png",
        "http://localhost:8000/dealer/15",
        ["submission_evidence/screenshots/dealer_id_reviews.png", "dealer_id_reviews.png"]
    ),
    # Q24: deployed_landingpage.png
    (
        "submission_evidence/screenshots/deployed_landingpage.png",
        f"{PROXY_BASE}/",
        ["submission_evidence/screenshots/deployed_landingpage.png", "deployed_landingpage.png"]
    ),
    # Q25: deployed_loggedin.png
    (
        "submission_evidence/screenshots/deployed_loggedin.png",
        f"{PROXY_BASE}/dealers",
        ["submission_evidence/screenshots/deployed_loggedin.png", "deployed_loggedin.png"]
    ),
    # Q26: deployed_dealer_detail.png
    (
        "submission_evidence/screenshots/deployed_dealer_detail.png",
        f"{PROXY_BASE}/dealer/15",
        ["submission_evidence/screenshots/deployed_dealer_detail.png", "deployed_dealer_detail.png"]
    ),
    # Q27: deployed_add_review.png
    (
        "submission_evidence/screenshots/deployed_add_review.png",
        f"{PROXY_BASE}/dealer/15",
        ["submission_evidence/screenshots/deployed_add_review.png", "deployed_add_review.png"]
    ),
]

for in_path, url, outs in tasks:
    add_browser_chrome(in_path, url, outs)

print("All screenshots successfully updated with browser address bar!")
