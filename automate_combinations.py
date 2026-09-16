"""Query Palworld.gg breeding combinations using Playwright"""
from playwright.sync_api import Page, sync_playwright
from tqdm import tqdm

BASE_URL = 'https://palworld.gg/breeding-calculator'

def select_pal(page: Page, pal_name: str, index: int) -> None:
    """Select a Pal in the specified calculator slot."""

    page.locator(".calculator .pal").nth(index).click()

    search_input = page.get_by_placeholder("Search for Pal")
    search_input.fill(pal_name)

    page.locator(".pal .container").get_by_text(
        pal_name, exact=True
    ).first.click()

def get_breeding_combinations(pals: list[str]) -> dict[str, list[str]]:
    """Return breeding combinations for input pals"""

    combinations: dict[str, list[str]] = {}

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

        remaining_pals = list(pals)

        while len(remaining_pals) > 1:
            pal1 = remaining_pals.pop(0)

            select_pal(page, pal1, index=0)

            for pal2 in tqdm(remaining_pals, desc=f"Breeding with {pal1}"):

                is_katress_wixen = {pal1, pal2} == {"Katress", "Wixen"}
                if is_katress_wixen:
                    katress_wixen_pair = f"{pal1} + {pal2}"
                    combinations.setdefault("Katress Ignis", []).append(katress_wixen_pair)
                    combinations.setdefault("Wixen Noct", []).append(katress_wixen_pair)

                if (pal1 == "Katress" and pal2 == "Wixen") or (pal1 == "Wixen" and pal2 == "Katress"):
                    if "Katress Ignis" not in combinations:
                        combinations["Katress Ignis"] = []
                    if "Wixen Noct" not in combinations:
                        combinations["Wixen Noct"] = []
                    combinations["Katress Ignis"].append(f"{pal1} + {pal2}")
                    combinations["Wixen Noct"].append(f"{pal1} + {pal2}")
                    break

                select_pal(page, pal2, index=1)

                result = page.locator(".calculator .pal.result")
                result.wait_for(state='visible')
                text = result.text_content()

                if text is None:
                    raise RuntimeError("Breeding result does not exist (has no text).")

                combinations.setdefault(text, []).append(
                    f"{pal1.strip()} + {pal2.strip()}"
                )

        browser.close()
    return combinations
