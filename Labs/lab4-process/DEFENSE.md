# DEFENSE: Lab 4 - Процес (Activity)

## 1. Намір і критерії

Описав бізнес-процес UC3 (Upload Video) однією декларативною формою — UML activity-діаграмою на PlantUML: start/stop, дії, ромби-рішення, fork/join-бари, swimlanes (User / VideoHub System). Критерії в spec.md: >=1 розгалуження, >=1 паралельна гілка, повнота переходів, узгодженість з UC (Lab 2) і Sequence (Lab 3).

Лаба зроблена AI-шляхом: AI написав драфт, AI-аудит за чек-листом task.md знайшов 4 розбіжності, кожна закрита фікс-комітом. Слід: `ai/prompts.md`, `ai/audit.md`, `ai/lab4_workflow.md`.

## 2. Топ-3 розбіжності (spec <-> артефакт) + коміт-виправлення

- **Відсутня гілка 409 і dedup-перевірка** — у драфті `title not empty? -> Create Video in DB`, а в sequence Lab 3 є `findByAuthorAndUrl` + 409 за ADR-003. Activity і sequence — один процес, логіка має бути ідентичною. Критерій «узгодженість з Lab 3» уточнено до конкретних елементів (401/400/409 + dedup-крок). Коміт spec+модель: `0630d3a`
- **Наближення нотації замість нотації** — Mermaid flowchart: `{{fork}}`/`{{join}}` шестикутниками, без partitions і ромбів-рішень як елементів нотації. Та сама помилка, за яку Lab 2 відхилили («не UML-нотація»). Критерію не було — додано «канонічний source PlantUML». Коміт spec+модель: `0630d3a` (.mmd видалено, .puml створено)
- **Swimlanes у spec, але не на діаграмі + незадокументовані кроки** — ролі User/System існували тільки текстом; Notify/Index не трасувалися до жодного UC/REQ. Виправлено: `partition User`/`VideoHub System` у діаграмі; Notify/Index задокументовано в ADR-004 як доменне розширення (асинхронні post-commit кроки поза синхронним scope sequence). Коміт spec+модель: `0630d3a`

Повний список — AUDIT.md (4 розбіжності + дрібне).

## 3. Ключове рішення (ADR)

**ADR-004** — три пов'язані рішення: (а) activity, не машина станів (UC3 — процес з чітким початком/кінцем; state machine — для життєвого циклу Video); (б) PlantUML, не Mermaid flowchart (повна activity-нотація: partitions, fork/join-бари, ромби — прецедент Lab 2); (в) Notify/Index лишено як задокументоване доменне розширення — реалістично для YouTube-домену і дає змістовну паралельну гілку.

## 4. Перевірка узгодженості з попередніми моделями

**З Lab 3 (Sequence):** той самий процес, інший ракурс — sequence показує ХТО кого викликає в часі, activity показує ПОТІК робіт. Гілки помилок ідентичні: 401 (invalid token), 400 (invalid input), 409 (duplicate за `findByAuthorAndUrl`). Різниця свідома: sequence — синхронний request-response, тому Notify/Index там відсутні (асинхронні post-commit кроки — ADR-004); термінальний `break` у sequence відповідає `stop` у activity.

**З Lab 2 (UC):** деталізує UC3; lane `User` = актор UC3; `Validate auth token` відповідає include UC9 Authenticate (реалізований у Lab 3 як AuthService.validateToken).

**З Lab 1 (ER):** `authorId = userId` у dedup-кроці — місток до Video.authorId; UNIQUE на url в ER немає — тому dedup є кроком процесу, а не констрейнтом БД.

## 5. Здача

Посилання на GitHub PR: (див. submit/defense.txt) + цей заповнений DEFENSE.
