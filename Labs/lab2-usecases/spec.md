# Spec: Lab 2 - Use Cases VideoHub

## Намiр

Описати вимоги до VideoHub у структурованому вигляді: EARS-вимоги, user stories, Gherkin-сценарії та use-case-діаграма. Трасування вимог до сценаріїв - багато-до-багатьох. Узгодженість з ER-моделлю (Lab 1).

## Актори

- **Guest** (людина) - незареєстрований відвідувач: реєструється (UC1), логіниться (UC2), переглядає (UC4), шукає (UC8)
- **User** (людина) - зареєстрований користувач, спеціалізація Guest: успадковує UC4/UC8 + власні UC3, UC5, UC6, UC7 (завантажувати, коментувати, лайкати, підписуватись)
- **Google OAuth** (зовнішня система) - сервіс автентифікації, пов'язаний з UC9

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
- UC9: Authenticate - перевірка автентифікації (включається в UC2/3/5/6/7)

## EARS-вимоги (неповний список, доповню в комітах)

- REQ1: WHEN user submits registration form, system SHALL create account with email and password
- REQ2: WHEN user selects Google login, system SHALL redirect to Google OAuth and create account on success
- REQ3: WHILE user is authenticated, system SHALL allow video upload with title and URL
- REQ4: WHEN guest opens video page, system SHALL display video and comments
- REQ5: WHEN user clicks like, system SHALL record like and prevent duplicate likes
- REQ6: WHEN user subscribes to channel, system SHALL create subscription record
- REQ7: WHILE guest searches, system SHALL return matching videos by title

## Критерії прийняття

- [x] >= 2 типи акторів (людина + зовнішня система)
- [x] EARS-вимоги однозначні й тестовані
- [x] User stories в форматі "As a ... I want ... so that ..."
- [x] Gherkin-сценарії (Given/When/Then)
- [x] Use Case діаграма з include/extend та узагальненням
- [x] Діаграма в UML use-case нотації: еліпси UC, актори-фігури, рамка системи (boundary). Канонічний source - PlantUML `model/usecase.puml` (Mermaid не має UC-нотації); `.drawio` синхронний семантично
- [x] Узагальнення у напрямку дитина -> батько: User --|> Guest (User є різновидом Guest з додатковими правами), ідентично в .puml і .drawio
- [x] UC асоційовані з актором, який їх реально виконує: реєструється/логіниться Guest (ще не User); upload/comment/like/subscribe - User
- [x] Вимоги розбиті на функціональні (EARS, REQ1-11) і нефункціональні (NFR) у requirements.md
- [x] Кожен UC має покроковий сценарій: основний потік + альтернативні потоки у usecases.md
- [x] Матриця трасування багато-до-багатьох
- [x] >= 1 непокрита вимога з поясненням
- [x] Узгодженість з ER-моделлю (Lab 1)
