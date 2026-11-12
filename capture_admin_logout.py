from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('http://127.0.0.1:8000/admin/login/', timeout=15000)
    page.fill('input[name="username"]', 'root')
    page.fill('input[name="password"]', 'RootAdmin123!')
    page.click('input[type="submit"]')
    page.wait_for_timeout(2000)
    print('Logged in, URL:', page.url)
    
    # Click Log out button/link in admin header
    logout_link = page.locator('a[href*="logout"]').first
    if logout_link.is_visible():
        logout_link.click()
    else:
        page.goto('http://127.0.0.1:8000/admin/logout/')
        
    page.wait_for_timeout(2000)
    print('After logout, URL:', page.url)
    page.screenshot(path='submission_evidence/screenshots/admin_logout.png')
    page.screenshot(path='admin_logout.png')
    browser.close()
print('Proper admin logout captured!')
