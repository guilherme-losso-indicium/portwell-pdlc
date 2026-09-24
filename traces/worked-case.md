# Worked lifecycle case

Run on 2026-09-24 in Claude Code, by hand, following the skills in `skills/` under the constitution.
Every value written into the artifacts came from a document in `portwell-product`, which was not
modified. Where the run needed a fact nobody recorded, it wrote `unknown` and named who could
supply it. Where it needed a decision, it stopped.

## Case

| Field | Value |
| :- | :- |
| Work item | OPPORTUNITY-04, expand the help portal rollout |
| Type | feature, proposed by route, not confirmed |
| Intended outcome | A signed G2 decision on whether to widen the pilot, with evidence that is current and sourced, every required consent given or recorded as missing, and a review date |
| Starting state | In flight since 2026-06-18 with no lifecycle. Tracker status Open. No G1 record. Decision deadline 2026-08-31 passed |
| Final state | 02-discovery, status escalated. Open episodes: escalated on POLICY-03 with no target, blocked on the passed G2 deadline, correction-required on failed verification. G2 unsigned. Handoff refused |
| Artifacts produced | `lifecycle/01-backlog/OPPORTUNITY-04.yaml`, `lifecycle/02-discovery/OPPORTUNITY-04.yaml`, `board.md` |

## Trace

| # | Skill invoked | Stage | Context read | Evidence produced | Proposed state | Result | Human intervention |
| -: | :- | :- | :- | :- | :- | :- | :- |
| 1 | intake | 01-backlog | Brief 2026-06-18, tracker row, four stakeholder requests, Ana Fialho interview | `01-backlog` artifact: header, `opportunity` with origin Gabriela Rocha, date unknown, deadline 2026-08-31 from REQUEST-A01, five unknowns | open | Created. Entry condition "requester can be named" met through the interview, not through any request document | Asked Ana Fialho for the origin date and to ratify the entry. Unanswered |
| 2 | context | 01-backlog | The four requests | `attached_requests`, four entries with verbatim asks | open | Done | None |
| 3 | route | 01-backlog | Brief, tracker | `type_hypothesis: feature` | open | Done | None |
| 4 | approve | 01-backlog | Artifact | G1 pack. Consents none. Recommendation null | open | **Stopped at the signature.** No record that anyone decided to investigate this opportunity | Ana Fialho asked to sign G1 or state that it was never decided. Unanswered |
| 5 | handoff | 01-backlog | G1 block | None | none | **Refused.** `gate.signature.person` is null | None. This is a refusal, not a question |
| 6 | intake | 02-discovery | Legacy onboarding rule in `skills/intake/SKILL.md`. Brief, tracker | `02-discovery` artifact: header, `entry_ticket` with G1 unknown and G2 deadline 2026-08-31, status_log line 1 "legacy entry" | open | Created under the legacy onboarding rule. The item is in discovery in fact: the brief, the design and the experiment exist | Operator decision, recorded below |
| 7 | context | 02-discovery | 22 documents, listed in `sources` | 27 manifest facts. Validity pass: F2 to F5 invalidated by INCIDENT-01, F8 invalidated by the author's statement, F9 unknown. 8 positions, two not on record. 8 contradictions. 12 unknowns | open | Done. Contradictions 1, 2, 6 and 8 depend on G2 | Asked Ana Fialho for the registered thresholds. Asked Rui Bastos for a capacity number. Asked Kofi Adjei for a written estimate. Asked Gabriela Rocha for the 112 minute source. Unanswered |
| 8 | route | 02-discovery | `types.yaml`, Policies.docx, manifest, headcount | `route_note`: type feature, four policies triggered, seven deterministic checks, signatories for G2 and G3, two waves | open | Done. Account count 28 exceeds 25, 40 exceeds 25. Enabled count cannot be counted. POLICY-03 wording mismatch recorded as contradiction 6, not decided | None |
| 9 | act | 02-discovery | Manifest, route note, DECISION-0031 for form | `decision_draft` with rationale citing manifest IDs, five constraints, review date unknown. `experiment_registration` not applicable | open | Done. The draft does not cite the experiment as a clean pass | None |
| 10 | verify | 02-discovery | Definition checks 1 to 7, artifact sections | `verification`: 5 pass, 1 cannot verify, 1 fail. Outcome failed. Seven `controls_missing` | correction-required | **Failed.** Check 3: registered thresholds unknown. Check 4: POLICY-10 in the evidence chain after supersession | None |
| 11 | recover | 02-discovery | statuses.yaml, tracker, interview 2026-08-12, REQUEST-T01, REQUEST-A01 | status_log lines 2 to 5: blocked on POLICY-03 since 2026-07-11, three asks with unknown dates, limit reached on the record of 2026-08-12; escalated since 2026-08-12, target not named; blocked on the passed G2 deadline since 2026-09-01; correction-required since 2026-09-24 | escalated | **Stopped.** No escalation target exists in the process. Header status set to escalated per the precedence added to `statuses.yaml` | Ana Fialho asked to name an escalation target. Unanswered |
| 12 | approve | 02-discovery | Route note, positions, verification | G2 pack. Consents: Rui Bastos objected 2026-08-08, Tomas Silva objected for LATAM 2026-08-11, Kofi Adjei not on record. Six items under `missing_for_more_discovery`. Recommendation null | open | **Stopped at the signature.** Build not available while verification is failed. Deadline passed | Ana Fialho asked to choose among reject, more-discovery, defer. Unanswered |
| 13 | handoff | 02-discovery | G2 block | Board row updated | none | **Refused.** `gate.signature.person` is null | None |

## Failure, refusal, or ambiguity

The run stopped four times. None of the stops was staged. Each is what the records force.

**What happened, 1. The item entered without a gate.** OPPORTUNITY-04 has no G1 record and never
had one. Intake could not satisfy the entry condition of discovery. Instead of fabricating a
triage decision or refusing to look at an item that is in fact in flight, the run applied the
legacy onboarding rule: create both artifacts, leave G1 unsigned, let the read-only skills run,
and refuse any movement until Ana Fialho ratifies the entry. The board therefore shows the item in
two columns. The process never recorded the step between "somebody asked" and "we are
investigating", and the board shows that.

**What happened, 2. The evidence contradicts itself on the fact G2 depends on.** The experiment
document says "Both criteria met." Its author said on 2026-08-12 that "It beat one measure and
missed the other" and that the threshold "was adjusted". The registered thresholds are not
recorded anywhere. Context recorded both versions. Verify could not perform check 3 and failed.
Approve wrote in the pack that the option build is not available. Nobody in the run resolved the
contradiction, because Article 2 forbids it and only Ana Fialho can.

**What happened, 3. A blocked episode had nowhere to go.** The POLICY-03 sign-off has been
pending since 2026-07-11. The record shows three asks by 2026-08-12. Recover applied the limit and
opened an escalated episode. The escalation target is `not named`, because the process has none.
Ana Fialho, 2026-08-12: "the person I would escalate to is the person waiting." The run stopped
and asked her to name one. `headcount.xlsx` shows she reports to Ines Duarte, and the run did not
pick that person, because a skill does not choose an escalation target.

**What happened, 4. Handoff refused twice.** With G1 and G2 unsigned, handoff refused to move the
item out of either stage. This is the one place where a skill refuses rather than asks.

**Why the lifecycle did not advance.** No person signed anything during the run. The group cannot
sign for Ana Fialho, Rui Bastos, Tomas Silva or Kofi Adjei, and the constitution forbids a skill
from doing it. Every signature block in both artifacts is null. That is the correct end state for
a run over records in which the decision has not been taken.

**Recovery or escalation.** Open in the artifacts: three unanswered questions to Ana Fialho
(ratify entry, re-establish the thresholds, name an escalation target), one to Rui Bastos
(capacity number), one to Kofi Adjei (written estimate), one to Gabriela Rocha (Nordkai baseline
source). `missing_for_more_discovery` lists what a G2 outcome of more-discovery would require.

## Stages not reached

The item did not leave discovery. For the lifecycle to be visible end to end, this is what each
later stage would have required of it, from the stage definitions. None of it was executed.

| Stage | Would require | State of that requirement in the record |
| :- | :- | :- |
| 03-ready-for-development | A signed G2 and an engineering estimate in writing | G2 unsigned. DECISION-0028 cites only "Verbal confirmation from engineering" |
| 04-in-development | Per-account enablement, per-area threshold, routing on account commitments, as the design proposes | Checklist row 5: "In the design, not built" |
| 05-review | Every checklist row Yes with an evidence link, rollback plan that exists, current policies | Rows 1, 2, 8 Yes with no evidence. Row 4 cites a file that does not exist. Row 6 checks POLICY-10 |
| G3 | Ana Fialho decides. Consents: Rui Bastos, Tomas Silva per region, Kofi Adjei, Gabriela Rocha. Account count against 25 | Rui objected. Tomas objected for LATAM. Kofi and Gabriela not on record. 28 exceeds 25 |
| 06-release | Wave 1 EU and NA enabled and confirmed by engineering | Whether 28 accounts are enabled today is not recorded |
| 07-monitoring | Measures with source and version against criteria frozen before release. Incidents linked | Registered criteria unknown. "Review load per engineer" has source "Not measured". Two incidents, no follow-up owner |
| G4 | Verdict against registered criteria | Cannot verify while F9 is unknown |
| 08-done | G4 outcome done and every remaining measure owned by an item | Not reachable |

## Decisions taken during the run

Two gaps in the design showed up only when the skills met the records. Both were closed by
editing the contract, and both are recorded here so a reviewer can disagree.

1. **Legacy onboarding rule**, added to `skills/intake/SKILL.md`. An item in flight when the
   harness is adopted enters the stage the record places it in, with every missing gate recorded
   as unknown. Read-only skills may run. Handoff may not, and no gate may be signed, until the
   owner ratifies the entry. Without this rule the run would have ended at step 1 with nothing to
   show. With it, nothing was approved and everything was recorded.
2. **Status precedence**, added to `states/statuses.yaml`. An artifact with an escalated
   episode, a blocked episode and a correction open at once needs one header status. The order
   is escalated, blocked, correction-required, open.

## Limitations and next improvement

- The run was performed by hand. Nothing checked that the artifacts match the templates or that
  the status log is consistent with the header. A schema check on `lifecycle/*.yaml` against
  `states/schema.yaml` is the first Module 2 tool.
- The parent pilot has no item. Its monitoring, which is where the incidents belong, could not
  be recorded as an artifact. The incidents entered this item only through the validity pass.
  Issuing an ID for the pilot is a question for the product repository's identifier range, which
  `docs/identifiers.md` should hold and the fixture does not ship.
- The dates of the three asks on BLOCKER-01 are unknown. The record says "three" and gives no
  dates. The limit was applied on the date of the record that states the count.
- The recomputed medians in F11 are the harness's arithmetic over the six rows of the results
  workbook. They match the document and are marked as not a source.
- Seven controls were performed by reading and are listed under `controls_missing`. The next
  improvement is to make one of them executable in Module 3: a consent cannot be recorded as
  given without a dated written response from that person. It would have caught checklist row 2.
- The `lifecycle.md` worksheet still has its to-be tables to fill from `states/`. That is
  deliverable 1 and is pending.
