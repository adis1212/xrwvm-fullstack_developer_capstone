from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://127.0.0.1:8000/admin/login/')
    page.fill('input[name="username"]', 'root')
    page.fill('input[name="password"]', 'RootAdmin123!')
    page.click('input[type="submit"]')
    page.wait_for_timeout(2000)
    print('Header HTML:\n', page.locator('#user-tools').inner_html())
    
    # In Django 5, the form in #user-tools submits a POST to /admin/logout/
    # Click the logout button inside the logout form
    page.locator('form[action*="logout"] button').click()
    page.wait_for_timeout(2000)
    print('Current page title:', page.title())
    print('Current URL:', page.url)
    print('Content text:\n', page.locator('#content').inner_text())
    page.screenshot(path='submission_evidence/screenshots/admin_logout.png')
    page.screenshot(path='admin_logout.png')
    browser.close()
