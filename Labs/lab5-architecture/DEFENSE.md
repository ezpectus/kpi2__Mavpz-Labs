# DEFENSE: Lab 5 - Архітектура (Component)

## 1. Намір і критерії

Змоделював архітектуру VideoHub компонентною діаграмою UML (PlantUML): модулі (Frontend, API Gateway, Auth/Video/Comment/Search/Notification Services, Data Access Layer, PostgreSQL), provided/required-інтерфейси (lollipop/socket), залежності, межа системи `rectangle`, зовнішні інтеграції (Google OAuth, Email/SMS Gateway). Критерії в spec.md + ключовий: кожен компонент і залежність трасується до ланцюга Lab 1–4 (матриця в AUDIT.md).

Лаба зроблена AI-шляхом з двома моделями: SWE-2 Max (драфт/реалізація) + GLM 5.3 Max (adversarial-рев'ю). Слід: `ai/prompts.md`, `ai/audit.md`, `ai/lab5_workflow.md`.

## 2. Топ-3 розбіжності (spec <-> артефакт) + коміт-виправлення

- **Наближення нотації втретє** — `graph TD` без component-стереотипів, lollipop-інтерфейсів і first-class межі. Прецедент Lab 2/4 — умова дозволяє Mermaid, але нотація оцінюється окремо. Критерій додано: «канонічний source PlantUML». Коміт spec+модель: `371efc9`
- **Інтерфейси як мітки ребер + зовнішні всередині межі** — provided/required читались тільки текстом spec; на першому рендері Google/Email візуально всередині межі. Виправлено: `() Interface` lollipop/socket + `package "External Systems"`. Коміти: `371efc9`, `282bf83`
- **Untraced Email/SMS Gateway + відсутня матриця покриття** — AI «дорисував» шлюз без сліду в REQ/UC; покриття ланцюга було неявним. Виправлено: Email/SMS задокументовано в ADR-005 (канал для REQ6 + Notify з Lab 4); матриця UC/REQ/lifeline/activity -> компонент у AUDIT.md — 9/9 UC покриті. Коміти: `371efc9`, поточний (AUDIT)

Повний список — AUDIT.md (5 розбіжностей + матриця).

## 3. Ключове рішення (ADR)

**ADR-005** — два рішення: (а) PlantUML component замість Mermaid graph (повна нотація: стереотипи, provided/required, межа-елемент); (б) Email/SMS Gateway лишено як задокументоване доменне розширення — канал сповіщень для REQ6 і fork Notify (Lab 4); явно позначено «поза REQ». Архітектура сервіс-орієнтована: кожен доменний UC-скопіювальний кластер — окремий сервіс, спільний доступ до даних через єдиний Data Access Layer (DIP-сумісно: сервіси залежать від IDataAccess, не від PostgreSQL напряму).

## 4. Як модель інтегрує весь ланцюг (перевірка)

- **Lab 1 (ER):** 5 сутностей — власник DAL + PostgreSQL; `authorId = userId` реалізується через IDataAccess.
- **Lab 2 (UC):** матриця UC->компонент у AUDIT.md; UC9 Authenticate -> Auth Service (include реалізований як IAuth); Google OAuth — зовнішній актор -> зовнішня система.
- **Lab 3 (Sequence):** lifelines -> компоненти: VideoController -> API Gateway, AuthService -> Auth Service, VideoService -> Video Service, Database -> DAL + PostgreSQL. findByAuthorAndUrl живе у Video Service через IDataAccess.
- **Lab 4 (Activity):** validateToken -> Auth Service; validateInput -> API Gateway; dedup+create -> Video Service + DAL; fork Notify -> Notification Service; fork Index -> Search Service (ISearchIndex).

## 5. Здача

Посилання на GitHub PR: (див. submit/defense.txt) + цей заповнений DEFENSE.
