# Spec: Lab 4 - Activity Diagram VideoHub

## Намір

Описати бізнес-процес UC3 (Upload Video) однією декларативною формою — activity-діаграмою. Початок/кінець, дії, потоки керування, розгалуження (if/else), паралельні гілки (fork/join), ролі. Узгодженість з UC (Lab 2) та Sequence (Lab 3).

## Обраний процес

UC3: Upload Video (з Lab 2, деталізований в Lab 3 sequence)

Ракурс відрізняється від Lab 3: sequence показує взаємодію компонентів у часі (хто кого викликає), activity — потік робіт процесу (кроки, рішення, паралельність, ролі).

## Кроки процесу

1. Start: User відкриває форму завантаження
2. Дія (User): заповнити title, description, url
3. Дія (User): натиснути Submit
4. Рішення (System): токен валідний?
   - Ні -> повернути 401 -> End
   - Так -> продовжити
5. Рішення (System): ввід валідний (title, формат)?
   - Ні -> повернути 400 -> End
   - Так -> продовжити
6. Дія (System): findByAuthorAndUrl(authorId = userId, url) — dedup-перевірка (бізнес-правило, як у Lab 3)
7. Рішення (System): дублікат знайдено?
   - Так -> повернути 409 -> End
   - Ні -> продовжити
8. Дія (System): створити запис Video в БД
9. Паралельні гілки (fork):
   - Гілка A: надіслати сповіщення підписникам
   - Гілка B: індексувати відео для пошуку
10. Join: обидві гілки завершені
11. Дія (System): повернути 201 + videoId
12. End

## Ролі (swimlanes)

- **User** — відкриває форму, заповнює, надсилає
- **VideoHub System** — перевіряє токен і ввід, dedup-перевірка, створює Video, сповіщає, індексує, відповідає

## Розгалуження

- if token valid (else 401)
- if input valid (else 400)
- if duplicate found (else 409 — ідентично Lab 3)

## Паралельні гілки

- fork: notify subscribers || index video
- join: обидві завершені до відповіді 201

## Критерії прийняття

- [x] Діаграма деталізує UC з Завдання 2
- [x] Є початок і кінець
- [x] Є >= 1 розгалуження (if/else) — три рішення: 401, 400, 409
- [x] Є >= 1 паралельна гілка (fork/join) — Notify || Index
- [x] Повнота переходів: немає недосяжних станів і «дір» у потоці; термінальні помилки завершують процес (stop)
- [x] Ролі (swimlanes): partition User / VideoHub System
- [x] Діаграма в UML activity-нотації — канонічний source PlantUML `model/activity.puml` (start/stop, ромби-рішення, справжні fork/join-бари, partitions); Mermaid flowchart не має partitions і fork-барів (прецедент Lab 2)
- [x] Гілки помилок і dedup-крок ідентичні Sequence Lab 3 (401/400/409, findByAuthorAndUrl)
- [x] Post-creation кроки (Notify/Index) задокументовані як доменне розширення — ADR-004
- [x] Узгодженість з UC (Lab 2) і Sequence (Lab 3)
- [x] Аудит: топ-3 розбіжності spec <-> артефакт з комітами-виправленнями
