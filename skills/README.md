# skills

Nine procedures, one per course stage, plus the constitution that all of them run under. They are
prose, not code. None of them needs a tool, a hook or a permission in Module 1.

## How a skill is invoked

Every skill takes two parameters: `item`, the stable ID, and `stage`, one of the eight folders under
`lifecycle/`. The skill reads `states/<stage>/definition.yaml` first. That file's `skills_sequence`
says which skills run in that stage and in what order. A skill that is not in the sequence for a
stage does nothing there and says so.

| Stage | Sequence |
| :- | :- |
| 01-backlog | intake, context, route, approve, handoff |
| 02-discovery | intake, context, route, act, verify, approve, handoff |
| 03-ready-for-development | intake, handoff |
| 04-in-development | intake, verify, handoff |
| 05-review | intake, context, route, act, verify, approve, handoff |
| 06-release | intake, act, verify, handoff |
| 07-monitoring | intake, context, observe, verify, approve, handoff, recover |
| 08-done | intake, handoff |

`recover` is invoked from any stage when a status changes, by whichever skill hit the failure path.

## What every skill has

Purpose. Parameters. Entry conditions. Reads. Prohibited context. Writes, by artifact and section.
Never writes. Procedure, numbered. Evidence produced. Proposed transition. Stop and escalation
conditions. Human judgment boundary. This is the contract in `constitution/SKILL.md`.

## Two rules that hold everywhere

A skill may produce evidence and propose the next state. It never records an approval that did not
happen. The `signature` block of every gate is written only by a person.

A skill that reaches a stop condition writes why in the artifact, names the person who must
answer, and ends. It does not continue on an assumption.
