import os
import time
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = os.path.abspath("submission_evidence/screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        print("1. Capturing admin_login.png...")
        page.goto("http://localhost:8000/admin/login/?next=/admin/")
        page.wait_for_selector("#id_username")
        page.fill("#id_username", "root")
        page.fill("#id_password", "RootAdmin123!")
        page.click("input[type=submit]")
        page.wait_for_selector("#user-tools")
        time.sleep(1)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "admin_login.png"))

        print("2. Capturing admin_logout.png...")
        page.goto("http://localhost:8000/admin/logout/")
        time.sleep(1)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "admin_logout.png"))

        print("3. Capturing get_dealers.png (logged out)...")
        # Clear storage
        context.clear_cookies()
        page.goto("http://localhost:8000/dealers/")
        page.wait_for_selector("table.table tr")
        time.sleep(2)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "get_dealers.png"))

        print("4. Capturing get_dealers_loggedin.png...")
        # Set session storage for logged-in user
        page.evaluate("""() => {
            sessionStorage.setItem('username', 'testuser');
            sessionStorage.setItem('firstname', 'Test');
            sessionStorage.setItem('lastname', 'User');
        }""")
        page.reload()
        page.wait_for_selector("table.table tr")
        time.sleep(2)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "get_dealers_loggedin.png"))

        print("5. Capturing dealersbystate.png (Kansas)...")
        page.select_option("select#state", "Kansas")
        time.sleep(2)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "dealersbystate.png"))

        print("6. Capturing dealer_id_reviews.png (Dealer 15)...")
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".reviews_panel")
        time.sleep(2)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "dealer_id_reviews.png"))

        print("7. Capturing dealership_review_submission.png...")
        page.goto("http://localhost:8000/postreview/15")
        page.wait_for_selector("#review")
        time.sleep(2)
        page.fill("#review", "Excellent dealership experience, very friendly staff and smooth delivery process.")
        # Purchase date input
        date_input = page.locator('input[type="date"]')
        date_input.fill("2023-05-15")
        # Car make & model select
        page.select_option("select#cars", label="Toyota Camry")
        # Car year input
        year_input = page.locator('input[type="int"], input[max="2023"]')
        year_input.fill("2023")
        time.sleep(1)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "dealership_review_submission.png"))

        print("8. Posting review and capturing added_review.png...")
        page.click("button.postreview")
        time.sleep(3)
        # Verify review is posted and visible on dealer 15 page
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".reviews_panel")
        time.sleep(2)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "added_review.png"))

        browser.close()
        print("All local screenshots captured successfully!")

if __name__ == "__main__":
    run()
