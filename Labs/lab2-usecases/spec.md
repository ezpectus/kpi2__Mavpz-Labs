# Spec: Lab 2 - Use Cases VideoHub (draft)

## Намiр

Описати вимоги до VideoHub у структурованому вигляді: EARS-вимоги, user stories, Gherkin-сценарії та use-case-діаграма. Трасування вимог до сценаріїв - багато-до-багатьох. Узгодженість з ER-моделлю (Lab 1).

## Актори

- **Guest** (людина) - незареєстрований відвідувач, може переглядати і шукати відео
- **User** (людина) - зареєстрований користувач, може все що Guest + завантажувати, коментувати, лайкати, підписуватись
- **Google OAuth** (зовнішня система) - сервіс автентифікації

## Головні цілі

1. Реєстрація та вхід (email + Google OAuth)
2. Завантаження відео
3. Перегляд відео
4. Коментування
5. Лайк
6. Підписка на канал
7. Пошук відео

## Use Cases

- UC1: Register - реєстрація нового користувача
- UC2: Login - вхід (email або Google OAuth)
- UC3: Upload Video - завантаження відео
- UC4: Watch Video - перегляд відео
- UC5: Comment - коментування відео
- UC6: Like Video - лайк
- UC7: Subscribe - підписка на канал
- UC8: Search Videos - пошук

## EARS-вимоги (неповний список, доповню в комітах)

- REQ1: WHEN user submits registration form, system SHALL create account with email and password
- REQ2: WHEN user selects Google login, system SHALL redirect to Google OAuth and create account on success
- REQ3: WHILE user is authenticated, system SHALL allow video upload with title and URL
- REQ4: WHEN guest opens video page, system SHALL display video and comments
- REQ5: WHEN user clicks like, system SHALL record like and prevent duplicate likes
- REQ6: WHEN user subscribes to channel, system SHALL create subscription record
- REQ7: WHILE guest searches, system SHALL return matching videos by title

## Критерії прийняття

- [ ] >= 2 типи акторів (людина + зовнішня система)
- [ ] EARS-вимоги однозначні й тестовані
- [ ] User stories в форматі "As a ... I want ... so that ..."
- [ ] Gherkin-сценарії (Given/When/Then)
- [ ] Use Case діаграма з include/extend та узагальненням
- [ ] Матриця трасування багато-до-багатьох
- [ ] >= 1 непокрита вимога з поясненням
- [ ] Узгодженість з ER-моделлю (Lab 1)
