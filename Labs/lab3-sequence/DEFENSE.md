# DEFENSE: Lab 3 - Sequence Diagram

## 1. Намір і критерії

Описати динаміку UC3 (Upload Video) з Завдання 2 як sequence-діаграму. Актор + 4 компоненти (VideoController, AuthService, VideoService, Database), alt/else гілки помилок (401, 400, 409), return-повідомлення, реалістичні назви викликів. Критерії зафіксовані в spec.md комітом `faabc11`.

## 2. Топ-3 розбіжності -> коміти

- Один учасник "Server" + немає return-повідомлень — проти spec "основні компоненти/об'єкти" і "return-повідомлення". Розбив на VideoController/AuthService/VideoService/Database, додав -->> для всіх викликів. Коміт: `5395f87`
- Немає гілок помилок (тільки happy path) — проти spec "альтернативні/умовні гілки" і "401, 400, 409". Додав alt-гілки. Коміт: `2efea96`
- opt для термінальних помилок (потік продовжувався до 201 після 400/409) + userId замість authorId у createVideo — проти spec "гілки помилок завершують сценарій" і ER-назви. Замінив на вкладені alt/else, єдиний validateToken, `authorId = userId`. Коміт: `9c345cb`

## 3. Ключове рішення (ADR)

Mermaid sequenceDiagram замість PlantUML. На відміну від use case діаграми (Lab 2) де Mermaid — компроміс, для sequence вона повністю підтримує UML-нотацію: actor, participant, ->>, -->>, alt/else, opt, loop. Рендериться нативно в GitHub; PlantUML — ні. Деталі: `adr/adr-003-sequence-notation.md`

## 4. Перевірка — узгодженість із попередніми моделями

**З Lab 1 (ER):** Database створює Video entity — атрибути виклику createVideo збігаються з полями Video (title, description, url, authorId). authorId = userId з AuthService — показано як `authorId = userId`.

**З Lab 2 (UC):** UC3 деталізований крок-в-крок; include UC9 (Authenticate) реалізований як AuthService.validateToken(). Помилкові гілки відповідають alternative flows UC3.

Додатково: для 409 в spec зафіксовано бізнес-правило дедуплікації (authorId, url) — в ER унікального обмеження на Video.url немає, тому це правило рівня застосунку, а не БД-констрейнт.
