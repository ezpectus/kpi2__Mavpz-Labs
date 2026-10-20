# ADR-005: Component-діаграма на PlantUML + Email/SMS Gateway як задокументоване розширення

## Статус

Accepted (переглянуто після AI-аудиту; попередня редакція обирала Mermaid graph — superseded у частині інструмента)

## Контекст

Для Lab 5 треба component diagram з інтерфейсами, залежностями, межею системи. Варіанти інструмента: Mermaid graph (рендериться в GitHub, але без component-нотації) vs PlantUML component (повна UML-нотація). Окреме питання — `Email/SMS Gateway`, який не трасується до жодного REQ/UC.

## Рішення

### 1. Інструмент: PlantUML component (не Mermaid graph)

AI-аудит і прецеденти Lab 2 (діаграма відхилена за не-UML нотацію) і Lab 4 (flowchart -> PlantUML) показали: `graph TD` — лише наближення:

- немає «component»-стереотипів — лише прямокутники;
- інтерфейси — текстові мітки ребер, напрямок provided/required не читається;
- `subgraph` — групування, не межа як first-class елемент;
- немає provided lollipop / required socket-нотації.

Канонічний source — `model/component.puml`; `.mmd` видалено (один джерело правди).

### 2. Email/SMS Gateway: лишено з документацією (не видалено)

AI-аудит позначив його untraced-елементом: жоден REQ/UC/lifeline/activity-крок не згадує email/SMS. Рішення — не видаляти, а задокументувати:

- найближчий слід у вимогах — REQ6 «notify channel owner» і fork `Notify subscribers` у Lab 4: сповіщення існує, канал не визначений;
- зовнішній шлюз — реалістична канал-абстракція для YouTube-домену (in-app зараз, email/SMS — зростання);
- явно позначено «розширення поза REQ» — чесно, а не приховано;
- бонус: критерій task «зовнішні інтеграції» покрито повніше (OAuth + Email).

## Наслідки

- Плюс: повна UML-нотація, видимі provided/required, межа як елемент, трасування доведене матрицею
- Мінус: PlantUML не рендериться нативно в GitHub — прийнятно, рендер у `renders/component.png`
- Матриця UC→компонент у AUDIT.md — доказ покриття ланцюга lab1–4
