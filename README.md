# KPI2-MAVPZ Labs

Лабораторні роботи з дисципліни "Компоненти програмної інженерії. Частина 2. Моделювання та аналіз вимог до програмного забезпечення".

Студент: Степаненко Денис, група IM-051
Спеціальність: 121 "Інженерія програмного забезпечення"
Викладач: Нечай Дмитро Олександрович

Рік: 2026, осінній семестр

Домен усіх завдань: **VideoHub** - платформа для відео, реальний проєкт: [github.com/ezpectus/VideoHub](https://github.com/ezpectus/VideoHub)

---

## Завдання

| # | Завдання | Тип моделі | Дедлайн | Статус | PR |
|---|----------|-----------|---------|--------|-----|
| 1 | ER-модель | Модель даних | 10 жовтня 2026 | Прийнято | [#2](https://github.com/ezpectus/kpi2__Mavpz-Labs/pull/2) |
| 2 | Use Cases | Вимоги | 24 жовтня 2026 | На рев'ю (перероблено за відгуком) | [#3](https://github.com/ezpectus/kpi2__Mavpz-Labs/pull/3) |
| 3 | Sequence | Взаємодія | 21 листопада 2026 | Прийнято з правками | [#1](https://github.com/ezpectus/kpi2__Mavpz-Labs/pull/1) |
| 4 | Process | Процес | 5 грудня 2026 | На рев'ю | [#4](https://github.com/ezpectus/kpi2__Mavpz-Labs/pull/4) |
| 5 | Architecture | Архітектура | 19 грудня 2026 | На рев'ю | [#5](https://github.com/ezpectus/kpi2__Mavpz-Labs/pull/5) |
| - | МКР | Контрольна | Наприкінці семестру | - | - |

Ланцюг моделей: **дані (ER) → вимоги (UC) → взаємодія (Sequence) → процес (Activity) → архітектура (Component)** — одна система VideoHub в п'яти ракурсах, кожна лаба трасується до попередніх.

---

## Гілки

Кожна лаба — окрема гілка + PR. Гілки змерджені каскадом (кожна містить повний ланцюг попередніх), бази PR — попередня лаба, тому диф кожного PR містить лише свою папку:

`lab1-er` → `lab2-usecases` → `lab3-sequence` → `lab4-process` → `lab5-architecture`

---

## Структура репозиторію

```
KPI2-MAVPZ Labs/
├── README.md
├── RULES.md                       - правила курсу
└── Labs/
    ├── lab1-er/                   - Завдання 1: ER-модель (Mermaid erDiagram)
    ├── lab2-usecases/             - Завдання 2: Use Cases (PlantUML usecase)
    ├── lab3-sequence/             - Завдання 3: Sequence (Mermaid sequenceDiagram)
    ├── lab4-process/              - Завдання 4: Activity (PlantUML activity)
    └── lab5-architecture/         - Завдання 5: Component (PlantUML component)
```

Кожна лабораторна містить:

- `task.md` - умова від викладача + посилання на проєкт-джерело
- `README.md` - опис домену
- `spec.md` - намір, сутності/кроки, критерії прийняття (<=1 стор.)
- `model/` - канонічний source діаграми (.mmd або .puml) + editable (.drawio)
- `renders/` - рендер діаграми (PNG)
- `AUDIT.md` - розбіжності spec <-> артефакт у форматі «критерій -> коміт-виправлення»
- `adr/` - Architecture Decision Records (MADR)
- `DEFENSE.md` - точка входу для рев'ю (1 стор.)
- `ai/` - слід AI-ітерації для лаб по AI-шляху (3-5): prompts, audit, workflow
