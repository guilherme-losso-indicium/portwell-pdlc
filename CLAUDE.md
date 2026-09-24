# Portwell PDLC harness

@skills/constitution/SKILL.md

The constitution above is always in context. Read it before any other file. Then:

- `states/` is the contract: `schema.yaml` for the common header, `types.yaml` for item types,
  `statuses.yaml` for the statuses, and one `definition.yaml` plus one `template.yaml` per stage.
- `skills/` holds the procedures, one per course stage. All of them run under the constitution.
- `lifecycle/` holds one YAML artifact per item per stage. Skills write there. People sign there.
- `lifecycle.md` is the course worksheet. `traces/worked-case.md` is the record of one run.
- `track.yaml` names the track repository. It is read and never written.
