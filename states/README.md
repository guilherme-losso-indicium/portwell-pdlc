# states

The contract of the lifecycle. Declarative. It changes when the process changes, not when an item
moves.

| File | Holds |
| :- | :- |
| `schema.yaml` | The header every artifact under `lifecycle/` starts with, and the signature block |
| `types.yaml` | The item types and what each gate requires of each type |
| `statuses.yaml` | The seven statuses, with entry, evidence, exit, owner, transitions and failure path |
| `<stage>/definition.yaml` | The six fields of the stage, its skill sequence, its verify checks, its gate |
| `<stage>/template.yaml` | The skeleton a skill instantiates as `lifecycle/<stage>/<ITEM-ID>.yaml` |

The operating rules that apply to every skill are in `skills/constitution/SKILL.md`, loaded through
the root `CLAUDE.md`.
