from playwright.sync_api import sync_playwright

def test_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        

        # page.goto("http://127.0.0.1:5500/wwwroot")
        page.goto("http://127.0.0.1:5500", wait_until="networkidle")

        
        
        assert "Vivre aux Lilas - Accueil" in page.title()
        
        # Vérifier la visibilité de certains éléments clés
        assert page.locator("h2:has-text('Actualités Récentes')").is_visible()
        assert page.locator("h2:has-text('Contact & Événements à venir')").is_visible()
        
        browser.close()

def test_menu_links():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        
        # page.goto("http://127.0.0.1:5500/wwwroot")
        page.goto("http://127.0.0.1:5500", wait_until="networkidle")

        
        
        links = page.locator("nav ul li a")
        assert links.nth(0).get_attribute("href") == "index.html"
        assert links.nth(1).get_attribute("href") == "actualites.html"
        assert links.nth(2).get_attribute("href") == "membres.html"
        
        browser.close()
