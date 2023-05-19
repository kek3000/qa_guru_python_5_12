import allure
from selene import have
import os


@allure.title("Successful fill form")
def test_form(browser_start):
    browser = browser_start

    with allure.step('Открываем главную страницу'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('Заполняем данные студента'):
        browser.element('#firstName').type('Nikita')
        browser.element('#lastName').type('Alekseev')
        browser.element('#userEmail').type('test@test.ru')
        browser.element('#gender-radio-1').double_click()
        browser.element('#userNumber').type('79999999999')
        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="6"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="1991"]').click()
        browser.element('div[aria-label="Choose Thursday, July 18th, 1991"]').click()
        browser.element('#subjectsInput').type('Computer Science').press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()
        browser.element('#uploadPicture').send_keys(os.getcwd() + "/image.jpg")
        browser.element('#currentAddress').type('Russia, Reutov')
        browser.element('#state').click()
        browser.element('#react-select-3-input').set_value('Haryana').press_tab()
        browser.element('#city').click()
        browser.element('#react-select-4-input').set_value('Panipat').press_tab()

    with allure.step('Отправляем форму регистрации'):
        browser.element('#submit').press_enter()

    with allure.step('Проверяем заполненные данные'):
        browser.all('tbody tr').should(have.exact_texts(
            'Student Name Nikita Alekseev', 'Student Email test@test.ru', 'Gender Male', 'Mobile 7999999999',
            'Date of Birth 18 July,1991', 'Subjects Computer Science', 'Hobbies Sports, Music',
            'Picture image.jpg', 'Address Russia, Reutov', 'State and City Haryana Panipat'))

    print('\nФорма полностью заполнена, отправлена и проверена. Тест пройден успешно.')
