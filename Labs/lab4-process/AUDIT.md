# AUDIT: Lab 4 - розбіжності spec <-> артефакт + коміти-виправлення

Формат: критерій spec -> знайдено -> виправив -> коміт. AI-аудит (ai/audit.md) і цей файл доповнюють один одного: там — помилки драфту, тут — зв'язка з критеріями spec і комітами.

## 1. Відсутня гілка 409 і dedup-перевірка (знайдено AI-звіркою з Lab 3)

**Критерій spec:** «узгодженість з Sequence (Lab 3)» існував, але не конкретизував «які саме елементи звіряються». Уточнено до «гілки помилок і dedup-крок ідентичні Sequence Lab 3 (401/400/409, findByAuthorAndUrl)».
**Знайдено:** у драфті `activity.mmd` потік ішов `{Title not empty?} --Yes--> Create Video in DB` — одразу створення без перевірки дублікату. У sequence.mmd (Lab 3) є явний крок `findByAuthorAndUrl(authorId = userId, url)` і гілка 409 за ADR-003. Activity і Sequence моделюють один процес — логіка має збігатися.
**Виправив:** action `findByAuthorAndUrl(authorId = userId, url)` + decision `duplicate found?` -> `Return 409 Conflict` -> `stop`; кроки 6-7 у spec.
**Коміт spec+модель:** `0630d3a` — lab4: spec+model - PlantUML activity + 409/dedup parity with sequence + swimlanes + fork/join

## 2. Наближення нотації замість UML activity-нотації (знайдено AI-аудитом, прецедент Lab 2)

**Критерій spec:** відсутній — додано «діаграма в UML activity-нотації — канонічний source PlantUML: start/stop, ромби-рішення, справжні fork/join-бари, partitions».
**Знайдено:** драфт на Mermaid `flowchart TD`: `{{fork}}`/`{{join}}` — шестикутники-ноди, не synchronization-бари; partitions/swimlanes у flowchart не існує; рішення — звичайні ромби графа. Та сама помилка, за яку Lab 2 була відхилена («діаграма не в UML-нотації»).
**Виправив:** канонічний source переписано на PlantUML `activity.puml` (`partition User`/`VideoHub System`, `if/then/else`, `fork/fork again/end fork`, `start/stop`); `activity.mmd` видалено — один канонічний source.
**Коміт spec+модель:** `0630d3a` (той самий — spec, .puml, видалення .mmd, ADR-004 в одному коміті)

## 3. Swimlanes задекларовані в spec, але відсутні на діаграмі

**Критерій spec:** «ролі (swimlanes) за потреби» — ролі User/System були в spec текстом, але на flowchart-рендері їх не видно.
**Знайдено:** усі дії у драфті — однакові прямокутники; не видно, які кроки робить User, а які System. Розбіжність spec («Ролі») <-> артефакт.
**Виправив:** `partition User` (open form, fill, submit) і `partition VideoHub System` (валідації, dedup, create, fork, відповідь) у .puml; ролі у spec перейменовано на «Ролі (swimlanes)» з точною назвою lane.
**Коміт spec+модель:** `0630d3a`

## 4. Post-creation кроки без трасування (Notify/Index)

**Критерій spec:** відсутній — додано «post-creation кроки (Notify/Index) задокументовані як доменне розширення».
**Знайдено:** `Notify subscribers` і `Index video for search` не зустрічаються ні в UC3 flows (`usecases.md`), ні в sequence, ні в REQ1-11 — AI-драфт «дорисував» правдоподібні кроки без джерела.
**Виправив:** не видалено, а задокументовано — ADR-004 фіксує post-creation fork як доменне розширення: sequence моделює синхронний request-response, асинхронні post-commit кроки поза його scope; водночас fork дає обов'язкову >=1 паралельну гілку змістовно.
**Коміт spec+модель:** `0630d3a` (ADR-004 у тому ж коміті)

## Дрібне, згорнуто

- `title: ... Activity v3` у драфті — версія у заголовку артефакту; прибрано при переписуванні на .puml.
- Draft-рендер `activity.png` (flowchart) замінено рендером з .puml у коміті `75e8a74`.

## Перевірено без змін (повнота/досяжність — окремий прохід аудиту)

- **Досяжність:** кожен вузол досяжний зі start; кожен вузол досягає якогось end — недосяжних дій і «висячих» гілок немає.
- **Повнота переходів:** кожен decision має рівно два підписані виходи (yes/no); після join жоден потік не йде поверх (201 лише після обох паралельних гілок).
- **Коректність умов:** умови — перевірювані предикати (token valid? / input valid? / duplicate found?), не дії.
- **Термінальність:** 401/400/409 завершуються `stop` — аналог `break` у sequence Lab 3.
