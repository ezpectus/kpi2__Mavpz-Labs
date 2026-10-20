# AI prompts: Lab 5 — Architecture (Component), AI-assisted track

## Контекст на вході

Lab 5 зроблена AI-шляхом (рішення після Lab 1–3, продовжено в Lab 4): модель архітектури має інтегрувати весь ланцюг моделей, тому процес — «AI-драфт -> окремий AI-рев'юер -> фікс-коміти». Дві моделі на різні ролі:

- **SWE-2 Max** — генерація драфту і реалізація фіксів (spec/model/renders/документи);
- **GLM 5.3 Max** — adversarial-рев'ю: чек-листи, звірка з ланцюгом моделей, спроба зламати аргументи.

Рознесення генератора і рев'юера по різних моделях свідоме: одна модель погано бачить власні діри.

На вхід передано:

- `task.md` — компоненти (UI, API/Backend, сервіси, Data Access, БД), provided/required-інтерфейси, залежності, чітка межа системи, зовнішні інтеграції; аудит: кожен компонент/залежність трасується до попередніх моделей (дані/вимоги/взаємодія/процес); топ-3 розбіжності; DEFENSE «як модель інтегрує ланцюг»;
- `spec.md` — таблиці компонентів і інтерфейсів;
- драфт `model/component.mmd` — Mermaid `graph TD` (згенерував SWE-2 Max);
- ланцюг для звірки: `Labs/lab1-er/model/er.mmd`, `Labs/lab2-usecases/` (UC1–UC9, REQ1–11), `Labs/lab3-sequence/model/sequence.mmd`, `Labs/lab4-process/model/activity.puml`;
- прецеденти: Lab 2 відхилена за не-UML нотацію; Lab 4 драфт flowchart замінено PlantUML — «task дозволяє обидва» ≠ «обидва прийнятні».

Формат промпту: **model + role + context + task + constraints + output contract**.

---

## P1 — checklist extraction (GLM 5.3 Max, review role)

> **Model:** GLM 5.3 Max · **Role:** strict requirements engineer · **Temp:** low (deterministic extraction)
> **Input:** full text of `task.md` (Lab 5).
> **Task:** Extract every requirement into a numbered checklist with verify-location (spec / diagram / audit / defense). Flag quantitative minimums and the full-chain consistency requirement — name the four upstream models explicitly (ER Lab 1, UC Lab 2, Sequence Lab 3, Activity Lab 4) so the check can reference them by file.
> **Constraints:** no invented requirements; quote ambiguous phrases verbatim; keep "every component/dependency traced" as one atomic item — it is the core criterion.
> **Output:** markdown table: # | requirement | verify-in | type (quantitative / structural / cross-check).

Відповідь GLM: 9 пунктів — модулі UI/API/сервіси/DAL/БД; provided/required-інтерфейси; залежності; чітка межа; зовнішні інтеграції; одна компонентна діаграма + рендер; трасування кожного елемента до lab1–4; топ-3 розбіжності; DEFENSE про інтеграцію ланцюга.

## P2 — audit draft + full-chain trace (GLM 5.3 Max, adversarial)

> **Model:** GLM 5.3 Max · **Role:** adversarial reviewer — your job is to FAIL the draft, not approve it
> **Input:** P1 checklist, draft `component.mmd`, and the four upstream sources (paths above).
> **Task:** (a) Run every checklist item: PASS/FAIL/RISK + quoted line as evidence. (b) Build a traceability matrix: every component and every edge -> which REQ/UC/lifeline/process-step it realizes. Elements without a trace = "untraced element". UC/REQ without a component = "coverage hole".
> **Constraints:** A PASS without a cited line does not count. Do not assume intent for untraced elements. Check that `subgraph` actually renders as a boundary, not just a group label.
> **Output:** verdict table + traceability matrix + untraced elements + coverage holes.

Відповідь GLM: FAIL — (а) `graph TD` не UML component-нотація: немає «component»-стереотипів, provided/required (lollipop/socket), портів — інтерфейси лише мітки ребер; (б) `subgraph System` — групування, не елемент-межа; (в) `Email/SMS Gateway` — без сліду в REQ1-11/UC/lifelines/activity — untraced element; (г) матриці трасування немає — стрілки є, але зв'язок з UC не доведений; (д) `title: v3`; (е) Frontend→GW стрілка без інтерфейсу серед решти інтерфейсних ребер — неузгоджено.

## P3 — notation critical evaluation (GLM 5.3 Max, sceptical review)

> **Model:** GLM 5.3 Max · **Role:** reviewer of my own earlier decision — be sceptical
> **Context:** Lab 2 rejected for non-UML diagram ("кругле говно"); Lab 4 draft flowchart replaced by PlantUML activity. ADR-005 argues for Mermaid "because GitHub renders it".
> **Task:** Does `graph TD` + `subgraph` repeat the approximation-instead-of-notation mistake a third time? Compare element-by-element: component stereotype, provided/required interfaces (ball/socket), ports, assembly connectors, boundary as a first-class element, external systems placement.
> **Constraints:** "the task allows both" is not an argument; weigh the instructor's established standard from his reviews.
> **Output:** comparison table + verdict + ADR-005 decision (supersede or amend).

Відповідь GLM: третє повторення тієї ж помилки. PlantUML має `[Component]`, `() Interface` (provided lollipop / required socket), `package`/`rectangle` boundary. ADR-005 — superseded в частині інструмента (Mermaid->PlantUML), рішення про зміст моделі лишається.

## P4 — implement spec+model in one commit (SWE-2 Max, implementer)

> **Model:** SWE-2 Max · **Role:** implementer of an approved fix, not a redesigner
> **Task:** ONE commit: (a) spec — add criteria "UML component notation, canonical PlantUML: «component» stereotypes, provided/required interfaces, boundary as drawn element" + "every component and dependency traced to Lab 1–4 via a coverage matrix"; (b) `component.puml`: `rectangle "VideoHub System"` boundary; components Frontend(Next.js), API Gateway(Express), Auth/Video/Comment/Search/Notification Services, DataAccessLayer(Prisma), Database(PostgreSQL) inside; Google OAuth and Email/SMS Gateway outside; provided/required lollipops — GW requires IAuth/IVideoOps/ICommentOps/ISearch; VideoService requires INotify/ISearchIndex; services require IDataAccess provided by DAL; AuthService requires IGoogleOAuth; NotificationService requires IEmailGateway; actor User -> Frontend. (c) resolve EmailGateway: keep ONLY with ADR-documented trace (notification channel for REQ6/lab4-fork), else delete. (d) delete component.mmd — one canonical source.
> **Constraints:** every component traced to UC/REQ/lifeline/process or removed; every edge has an interface or a documented reason; commit "lab5: spec+model - ..." (spec and model together).
> **Output:** full .puml + spec diff + coverage matrix rows to embed into AUDIT.

Результат: коміт spec+model — PlantUML component (boundary, lollipop-інтерфейси), EmailGateway лишено з ADR-005-розширенням (канал сповіщень для REQ6 + fork Notify з Lab 4), `.mmd` видалено.

## P5 — render + drawio sync + self-verify (SWE-2 Max, build role)

> **Model:** SWE-2 Max · **Role:** build engineer for diagram artifacts
> **Task:** Regenerate `renders/component.png` from `component.puml` via PlantUML server (User-Agent — bare request 403s). Rewrite `component.drawio` semantically identical: boundary rectangle, component shapes, lollipop provided / socket required, externals outside.
> **Self-verification:** every required interface has exactly one provider inside the boundary; nothing crosses the boundary except OAuth and Email edges; every UC1–UC9 maps to >=1 component; no dangling edges.
> **Output:** PNG + drawio XML + per-item verification result.

## P6 — AUDIT in review format (SWE-2 Max, writer)

> **Task:** AUDIT.md, format «criterion -> found (quote) -> fixed -> commit» ("цей коміт" if pending). Findings: notation (graph TD not component); boundary as subgraph-approximation; interfaces as edge-labels not provided/required; EmailGateway untraced -> resolved via ADR-005; missing traceability matrix -> added as coverage table. Embed the UC->component matrix as proof of coverage.

## P7 — DEFENSE + chain-integration section (SWE-2 Max)

> **Task:** DEFENSE.md by instructor template + the required "how the model integrates the whole chain": ER entities -> owning components; UC1–UC9 -> components; sequence lifelines (VideoController/AuthService/VideoService/Database) -> components; activity steps (validate/dedup/create/fork) -> component responsibilities. Every claim must trace to a file — flag untraceable ones.

## P8 — final self-check run (GLM 5.3 Max, instructor's-checker simulation)

> **Model:** GLM 5.3 Max · **Role:** the instructor's automated checker — assume nothing is done until proven
> **Input:** P1 checklist + final repo state (spec, component.puml, renders/, AUDIT, DEFENSE, adr/, ai/, git log).
> **Task:** Verify every item with file:line evidence. Specifically: exactly one canonical source; boundary drawn as an element; provided/required as notation (not edge text); coverage matrix complete — no component without trace, no UC1–UC9 without component.
> **Output:** full verdict table; FAILs only at the end, or "no open findings".

Результат прогону: усі 9 пунктів PASS, докази — секція «Фінальний прогон» у `ai/audit.md`.

## P9 — workflow document (SWE-2 Max)

> **Task:** `ai/lab5_workflow.md` from the lab4 template, adapted: spec -> AI draft -> adversarial AI review (separate model) -> fix commits -> renders -> AUDIT/DEFENSE -> post-review readiness. State honestly which findings which model caught, and why generator/reviewer were split across models.
