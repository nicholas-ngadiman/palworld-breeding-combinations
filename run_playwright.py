"""Use Playwright to query Palworld.gg"""
import time
from playwright.sync_api import sync_playwright

BASE_URL = 'https://palworld.gg/breeding-calculator'

def get_combinations(pals: list[str]):
    """Query combinations from Palworld.gg"""
    combinations: dict[str, list[str]] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)

        while len(pals) > 1:
            pal1 = pals.pop(0)
            print(pal1)
            page.locator(".calculator .pal").first.click()
            time.sleep(0.2)

            page.fill("input[id='search-mini']", pal1)
            time.sleep(0.2)

            page.get_by_text(f"{pal1} ", exact=True).first.click()
            time.sleep(0.2)

            for pal2 in pals:
                page.locator(".calculator .pal").nth(1).click()
                time.sleep(0.2)

                page.fill("input[id='search-mini']", pal2)
                time.sleep(0.2)

                page.get_by_text(f"{pal2} ", exact=True).first.click()
                time.sleep(0.2)

                selector = page.query_selector(".calculator .pal.result")
                time.sleep(0.2)

                if selector is None:
                    raise RuntimeError(f"Element not found {selector}")

                child = selector.text_content()
                if child is None:
                    raise RuntimeError(f"Text not found in element for {pal1} + {pal2}: {selector}")

                if child not in combinations:
                    combinations[child] = []
                combinations[child].append(f"{pal1} + {pal2}")
        return combinations