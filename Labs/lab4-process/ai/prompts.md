# AI prompts: Lab 4 — Process (Activity), AI-assisted track

## Контекст на вході

Ця лаба зроблена AI-шляхом (рішення після Lab 1–3: складніші завдання — через явний цикл «AI-драфт -> AI-аудит -> фікс-коміти»). На вхід моделі передано:

- `task.md` — умова (activity АБО state machine; >=1 розгалуження; >=1 паралельна гілка; аудит повноти переходів/досяжності/умов; звірка з UC Lab 2 і Sequence Lab 3; топ-3 розбіжності; DEFENSE);
- `spec.md` — намір, кроки, ролі, критерії;
- драфт `model/activity.mmd` — Mermaid flowchart, згенерований AI;
- `Labs/lab3-sequence/model/sequence.mmd` — гілки 401/400/409 і `findByAuthorAndUrl` для звірки;
- `Labs/lab2-usecases/usecases.md` — main/alt flows UC3;
- контекст-урок: Lab 2 відхилено за не-UML нотацію («діаграма говно кругле») — нотація оцінюється окремо від змісту.

Промпти нижче — англійською (робоча мова для моделі), результати — українською для захисту. Формат кожного промпту: **role + context + task + constraints + output contract**.

---

## P1 — checklist extraction

> **Role:** You are a strict requirements engineer.
> **Input:** the full text of `task.md` (Lab 4).
> **Task:** Extract every requirement into a numbered checklist. One requirement per item. For each item state where it must be verified (spec / diagram / audit / defense). Flag requirements that set a quantitative minimum (e.g. ">=1 branch", ">=1 parallel branch") and requirements that are cross-artifact checks (consistency vs UC, vs Sequence).
> **Constraints:** Do not add requirements that are not in the text. Do not merge two requirements into one item. If a requirement is ambiguous, quote the ambiguous phrase verbatim.
> **Output:** markdown table: # | requirement | verify-in | type (quantitative / structural / cross-check).

Відповідь AI: 9 пунктів — одна декларативна форма; start/end; дії+потоки; >=1 if/else; >=1 fork/join; swimlanes «за потреби»; повнота+досяжність+коректність умов; звірка UC+Sequence; топ-3 розбіжності + DEFENSE.

## P2 — audit the draft against the checklist

> **Role:** You are an adversarial reviewer. Your job is to FAIL this draft, not to approve it.
> **Input:** the checklist from P1, the draft `model/activity.mmd` (Mermaid flowchart), `spec.md`.
> **Task:** Run every checklist item against the draft. Verdicts: PASS / FAIL / RISK, each with a quoted line number as evidence. Then do a second pass — consistency vs `Labs/lab3-sequence/model/sequence.mmd`: the sequence has error branches 401/400/409 and an explicit `findByAuthorAndUrl` step. List every divergence with the quoted draft line.
> **Constraints:** A PASS without a cited line does not count. If a diagram element has no trace in spec, mark it "untraced element" — do not assume intent.
> **Output:** two tables — checklist verdicts; sequence-divergences.

Відповідь AI: FAIL — (а) лише 401 і 400; гілки 409 і dedup-кроку немає взагалі — пряма розбіжність з sequence (критерій «узгодженість з Lab 3»); (б) `{{fork}}`/`{{join}}` — шестикутники flowchart, не UML synchronization-бари; (в) swimlanes відсутні — ролі є в spec, невидимі на діаграмі; (г) Notify/Index без сліду в UC3 flows / sequence / REQ — untraced elements; (д) `title: ... v3` — версія у заголовку.

## P3 — critical evaluation of the notation choice

> **Role:** You are reviewing my own earlier decision. Be sceptical of it.
> **Context:** Lab 2 was rejected by the instructor for a non-UML diagram ("кругле говно") — a Mermaid graph instead of a use-case diagram; it was fixed by moving to PlantUML. The Lab 4 task allows either "Mermaid flowchart OR PlantUML activity".
> **Task:** Evaluate whether Mermaid flowchart repeats the Lab 2 mistake — an approximation of a notation instead of the notation itself. Compare item by item: partitions/swimlanes, fork/join as synchronization bars, decision nodes, start/end symbols, flow semantics. Conclusion must be argued by notation, not by GitHub-render convenience.
> **Constraints:** "The task allows both" is not an argument — it only means both parse. Consider the precedent set by the instructor's review.
> **Output:** comparison table + verdict + what must change in ADR-004.

Відповідь AI: повторює помилку. У flowchart немає partitions, fork/join — прості вузли, рішення — граф-ромби без семантики activity. Рішення: PlantUML `activity.puml` канонічний; ADR-004 переглянути (superseded для Mermaid — сценарій ADR-002 у Lab 2).

## P4 — implement spec+model in one commit

> **Role:** You are implementing an approved fix, not redesigning.
> **Task:** In ONE commit update spec.md and the model together: (a) spec — add criteria "diagram in UML activity notation, canonical source PlantUML: start/stop, decision diamonds, real fork/join bars, partitions" and "error branches and dedup step identical to Lab 3 sequence (401/400/409, findByAuthorAndUrl)"; insert the dedup-check step between input validation and record creation; rename roles to swimlanes User / VideoHub System; mark criteria [x]. (b) model — rewrite as `activity.puml`: `partition User` (open form, fill, submit), `partition VideoHub System` (validateToken -> decision -> 401 -> stop; validateInput -> 400 -> stop; findByAuthorAndUrl(authorId = userId, url) -> duplicate? -> 409 -> stop; createVideo -> fork [Notify subscribers | Index video for search] -> join -> 201 -> stop). (c) delete `activity.mmd` — one canonical source only.
> **Constraints:** every spec criterion must map to a visible diagram element; every diagram step must map to a spec step or an ADR-documented extension. Commit message: "lab4: spec+model - ..." (spec and model change together, as in Lab 3).
> **Output:** the full .puml source + the spec diff.

Результат: коміт `0630d3a` — spec.md + `activity.puml` + видалений `.mmd` + оновлений ADR-004 в одному коміті.

## P5 — render and cross-format sync

> **Role:** Build engineer for diagram artifacts.
> **Task:** Regenerate `renders/activity.png` from `activity.puml` via the PlantUML public server (send a User-Agent header — the bare request returns 403, as seen in Lab 2). Rewrite `activity.drawio` semantically identical: same actions in the same lanes, rhombus decisions, fork/join bars, labeled yes/no exits.
> **Self-verification before done:** (1) no flow reaches an end node bypassing the join bar; (2) every decision has exactly two labeled exits; (3) error labels 401/400/409 are character-identical to `sequence.mmd`; (4) PNG visually shows lanes, diamonds, and thick fork/join bars.
> **Output:** PNG bytes + drawio XML + a verification checklist result per item.

Результат: `75e8a74` — PNG перегенеровано (видно lanes, ромби, fork/join-бари), drawio синхронний, валідний XML.

## P6 — write AUDIT.md in the review format

> **Role:** You are writing the audit the instructor will read.
> **Format:** for each discrepancy — which spec criterion was missing/imprecise -> what was found (quote the draft) -> what was fixed -> commit. Do not invent commit hashes; write "цей коміт" for the current change.
> **Content:** 4 findings — missing 409/dedup (consistency vs Lab 3); flowchart instead of activity notation; swimlanes declared in spec but not drawn; Notify/Index untraced -> ADR-004. Add a "verified unchanged" section: reachability of every node, exactly two labeled exits per decision, terminal stops.
> **Constraint:** the tone is factual — this is evidence, not marketing.

Результат: `710a732` — AUDIT.md з 4 findings + секція «Перевірено без змін».

## P7 — write DEFENSE.md + cross-model verification

> **Role:** You are preparing my oral defense script.
> **Format:** the instructor's template — intent+criteria, top-3 discrepancies + fix commits, key decision (ADR), verification of consistency with previous models.
> **Required consistency content:** (a) 401/400/409 branches and the dedup step are identical to Lab 3 — sequence shows WHO calls whom in time, activity shows the FLOW of the same logic; (b) fork/join is a documented domain extension — sequence models synchronous request-response, Notify/Index are asynchronous post-commit steps (ADR-004); (c) lane User = the UC3 actor, Validate auth token = include UC9; (d) `break` in sequence = `stop` in activity.
> **Constraint:** if any claim cannot be traced to a file, flag it — do not write untraceable claims.

Результат: `710a732` — DEFENSE.md за шаблоном, 4 пункти звірки (Lab 1/2/3).

## P8 — final self-check run (the AI-check simulation)

> **Role:** You are the instructor's automated checker. Assume nothing is done until proven.
> **Input:** the P1 checklist + the final state of `Labs/lab4-process/` (spec.md, model/activity.puml, renders/, AUDIT.md, DEFENSE.md, adr/, ai/, git log).
> **Task:** Run every checklist item. Verdicts PASS / FAIL with file:line evidence — including "task says ONE declarative form": confirm there is exactly one canonical diagram source and that drawio/PNG are renders of it, not a second notation. Check commit dates are plausible and spec+model changed in the same commits.
> **Output:** the full verdict table; list only the FAILs at the end, or state "no open findings".

Результат прогону (фінальний стан): усі 9 пунктів PASS — докази зафіксовані в `ai/audit.md` (секція «Фінальний прогон»). FAILів немає.

## P9 — workflow document

> **Task:** Write `ai/lab4_workflow.md` from the template of `lab3_workflow.md`: spec -> AI draft -> AI audit -> fix commits -> renders -> AUDIT/DEFENSE -> post-review readiness. State honestly which findings the AI-check caught and which a human would likely miss. State the stop conditions (checklist all-PASS; every diagram step traced or ADR-documented; one canonical source).

Результат: `710a732` — `ai/lab4_workflow.md`.
