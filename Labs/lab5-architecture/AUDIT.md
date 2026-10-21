# AUDIT: Lab 5 - розбіжності spec <-> артефакт + коміти-виправлення

Формат: критерій spec -> знайдено -> виправив -> коміт.

## 1. Наближення нотації замість UML component-нотації (третій прецедент)

**Критерій spec:** відсутній — додано «діаграма в UML component-нотації — канонічний source PlantUML («component»-стереотипи, provided lollipop / required socket, межа як елемент)».
**Знайдено:** драфт `component.mmd` — Mermaid `graph TD`: прямокутники без component-стереотипу, `subgraph System` як групування, інтерфейси — текстові мітки ребер. Та сама помилка, за яку Lab 2 відхилили і Lab 4 драфт переписувався.
**Виправив:** `component.puml` — `[Component]`-стереотипи, `rectangle "VideoHub System"`, `() Interface` provided/required, `.mmd` видалено.
**Коміт spec+модель:** `371efc9`

## 2. Інтерфейси як мітки ребер — provided/required не читається

**Критерій spec:** «provided/required-інтерфейси визначені» — списком є, але на діаграмі роль «хто надає / хто потребує» з ребра не читалась.
**Знайдено:** `APIGateway -->|IAuth| AuthService` — мітка є, семантики provided/required немає; інтерфейси-громади (ISearchIndex, INotify) частково неузгоджені зі spec.
**Виправив:** `() "IName"` — провайдер `Component - () I` (lollipop), споживач `Component ..> () I` (socket); spec-списки інтерфейсів синхронізовані з діаграмою (додано ISearchIndex, INotify у provided).
**Коміт spec+модель:** `371efc9`

## 3. Зовнішні системи всередині межі на першому рендері

**Критерій spec:** «межа системи чітка; зовнішні інтеграції поза нею».
**Знайдено:** на першому рендері .puml Google OAuth і Email/SMS Gateway візуально опинилися ВСЕРЕДИНІ `rectangle "VideoHub System"` — межа намальована, але зовнішні виглядали внутрішніми.
**Виправив:** `package "External Systems"` — явна група зовнішніх; ребра до них перетинають межу (коректна семантика «система потребує зовнішнє»); прибрано зайві `: requires`-мітки для читабельності.
**Коміт модель+рендер:** `282bf83`

## 4. Untraced-елемент Email/SMS Gateway

**Критерій spec:** відсутній — додано «Email/SMS Gateway — задокументоване доменне розширення (ADR-005)».
**Знайдено:** AI-драфт додав Email/SMS Gateway без сліду в REQ1-11/UC/lifelines/activity — «правдоподібне дорисування».
**Виправив:** не видалено, а задокументовано — найближчий слід REQ6 «notify channel owner» + fork `Notify subscribers` (Lab 4): сповіщення існує, канал не визначений. ADR-005 фіксує зовнішній канал як розширення, позначене «поза REQ».
**Коміт spec+модель:** `371efc9`

## 5. Матриці трасування не було — покриття недоведене

**Критерій spec:** відсутній — додано «кожен компонент і залежність має слід у Lab 1–4; жоден UC без компонента».
**Знайдено:** драфт містив правильний набір компонентів, але покриття було неявним — без матриці критерій task «кожен компонент/залежність трасується» не доведений.
**Виправив:** матриця трасування нижче — доказ повного покриття.
**Коміт:** цей коміт (AUDIT.md).

---

## Матриця трасування UC / вимоги / моделі -> компоненти

| Елемент ланцюга | Компонент(и) | Слід |
|---|---|---|
| UC1 Register | Auth Service | реєстрація, створення User |
| UC2 Login | Auth Service + Google OAuth | REQ2 |
| UC3 Upload Video | API Gateway -> Video Service -> DAL -> DB | upload, dedup, create |
| UC4 Watch Video | Frontend + API Gateway + Video Service | playback |
| UC5 Comment | Comment Service | REQ8/REQ9 |
| UC6 Like Video | Video Service (like — операція відео) | REQ5 |
| UC7 Subscribe | Video Service (підписка на канал) + Notification Service (повідомити власника) | REQ6 |
| UC8 Search | Search Service | ISearch, REQ7 |
| UC9 Authenticate | Auth Service | IAuth, include-UC |
| REQ6 notify owner | Notification Service -> Email/SMS Gateway | ADR-005 |
| REQ11 invalid format | API Gateway (валідація -> 400) | Lab 3/4 parity |
| ER: User/Video/Comment/Like/Subscription | Data Access Layer + PostgreSQL | Lab 1 |
| Sequence: VideoController | API Gateway (вхідна точка контролера) | Lab 3 |
| Sequence: AuthService | Auth Service | Lab 3 |
| Sequence: VideoService | Video Service | Lab 3 |
| Sequence: Database | DAL + PostgreSQL | Lab 3 |
| Activity: validateToken/validateInput | Auth Service / API Gateway | Lab 4 |
| Activity: findByAuthorAndUrl + createVideo | Video Service + DAL | Lab 4 |
| Activity: fork Notify | Notification Service | Lab 4 + REQ6 |
| Activity: fork Index | Search Service | Lab 4 + UC8 |

**Підсумок:** усі 9 UC, REQ1–11, 4 lifelines, кроки activity — покриті; усі 9 внутрішніх і 2 зовнішні компоненти — трасуються.
