# import allure
# from allure_commons.types import Severity
# from selene.support import by
# from selene.support.conditions import be
# from selene.support.shared import browser
# from selene.support.shared.jquery_style import s
#
#
# def test_dynamic_labels():
#     allure.dynamic.tag("web")
#     allure.dynamic.severity(Severity.BLOCKER)
#     allure.dynamic.feature("Tasks in repository")
#     allure.dynamic.story("Task is not visible")
#     allure.dynamic.link("https://github.com", name="HW_10")
#     pass
#
#
# @allure.tag("gitHub")
# @allure.severity(Severity.CRITICAL)
# @allure.label("owner", "YuliyaShkretova")
# @allure.feature("Tasks in repository")
# @allure.story("Task is visible")
# @allure.link("https://github.com", name="HW_10")
# def test_decorator_steps_issue():
#    pass
