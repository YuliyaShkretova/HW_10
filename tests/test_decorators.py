import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def allure_decorators(func):
    @allure.tag("Decorators")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "YuliyaShkretova")
    @allure.feature("Tasks in repository")
    @allure.story("Task is visible")
    @allure.link("https://github.com", name="HW_10")
    @allure.title("Allure Decorators Test")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@allure.step("Open main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Find reposit {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Go to reposit {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Open Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Check issue number {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()


@allure_decorators
def test_decorator_steps():
    open_main_page()
    search_for_repository("YuliyaShkretova/HW_10")
    go_to_repository("YuliyaShkretova/HW_10")
    open_issue_tab()
    should_see_issue_with_number("#1")
