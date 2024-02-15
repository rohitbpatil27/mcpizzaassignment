import pytest
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    yield
    # Capture screenshot at the end of each test
    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = screenshot_dir / f"{request.cls.driver.title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    request.cls.driver.save_screenshot(str(screenshot_path))
    request.cls.driver.quit()  # Quit the driver after all tests in the class have finished

def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True
    config.option.html_report_title = "McPizza Assignment Report"  # Set HTML report title

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    try:
        outcome = yield
        rep = outcome.get_result()

        if rep.when == "call":
            if rep.failed:
                # Capture screenshot on failure
                screenshot_dir = Path("screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                screenshot_path = screenshot_dir / f"{item.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                item.cls.driver.save_screenshot(str(screenshot_path))
                pytest_html = item.config.pluginmanager.get_plugin("html")
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path, name="Screenshot"))
                rep.extra = extra
    except Exception as e:
        print("Error in pytest_runtest_makereport:", e)
