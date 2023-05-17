import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def allure_decorators_steps(func):
    @allure.tag("Steps")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "YuliyaShkretova")
    @allure.feature("Tasks in repository")
    @allure.story("Task is visible")
    @allure.link("https://github.com", name="HW_10")
    @allure.title("Allure Steps Test")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@allure_decorators_steps
def test_steps():
    with allure.step("Open main page"):
        browser.open("https://github.com")

    with allure.step("Find reposit"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("YuliyaShkretova/HW_10")
        s(".header-search-input").submit()

    with allure.step("Go to reposit"):
        s(by.link_text("YuliyaShkretova/HW_10")).click()

    with allure.step("Open Issues"):
        s("#issues-tab").click()

    with allure.step("Check issue number #1"):
        s(by.partial_text("#1")).should(be.visible)
