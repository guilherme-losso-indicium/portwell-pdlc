# Lifecycle worksheet

## Selected work item

| Field | Value |
| :- | :- |
| Track | PDLC, Product Development Lifecycle |
| Process | A product decision is made |
| Work item | OPPORTUNITY-04, expand the help portal pilot rollout (target 40 accounts) |
| Intended outcome | A recorded decision on whether, and how far, the pilot widens beyond its current scope, taken on evidence that is current and sourced, with every required sign-off either given or recorded as missing, and a stated condition for looking at it again |
| Current owner | Ana Fialho, VP Product (tracker owner for OPPORTUNITY-04 and LAUNCH-01) |

Why this item: it is the only item in the tracker that touches every other record in the repository
(the experiment, both incidents, the only pilot decision, all four stakeholder requests, the
blocker, the readiness checklist and the adoption measures). It is also still open, so the trace
ends in a real unresolved state rather than a tidy one.

## Sources consulted

All read from `portwell-product-main`, which was not modified. Age is the date the artifact itself
states. Where it states none, the age is unknown.

| Artifact | Path | Author | Dated | Revised |
| :- | :- | :- | :- | :- |
| How product decisions get made here | docs/How we work today.docx | Ana Fialho | 2025-11-04 | never |
| Policies | docs/Policies.docx | Ana Fialho | unknown | last reviewed 2026-06-02 |
| Dependencies | docs/Dependencies.docx | Ana Fialho | 2026-05-14 | unknown |
| Interview, how decisions happen | docs/interviews/2026-08-12 Ana Fialho, how decisions happen.docx | Mei Tan (interviewer) | 2026-08-12 | n/a |
| Interview, what the pilot showed | docs/interviews/2026-08-19 Rui Bastos, what the pilot showed.docx | Mei Tan (interviewer) | 2026-08-19 | n/a |
| INCIDENT-01 | docs/incidents/INCIDENT-01 superseded refund window.docx | on-call engineer, name not recorded | written 2026-07-14 | unknown |
| INCIDENT-02 | docs/incidents/INCIDENT-02 retry advice stopped a feed.docx | solution consultant, name not recorded | written 2026-07-29 | unknown |
| Pilot incidents, product view | docs/incidents/Pilot incidents, product view.docx | Ana Fialho | 2026-08-04 | unknown |
| Product tracker | data/product-tracker.xlsx | Ana Fialho | unknown | "updated when someone remembers" |
| OPPORTUNITY-04 brief | data/discovery/OPPORTUNITY-04-expand-the-portal-pilot.docx | Ana Fialho | 2026-06-18 | 2026-06-18 |
| Expansion design | data/discovery/portal-expansion-design.docx | Ana Fialho, Kofi Adjei | 2026-07-09 | unknown, status Draft |
| Stakeholder requests (4) | data/discovery/stakeholder-requests/ | Rocha, Bastos, Silva, Fialho | 2026-08-05 to 2026-08-13 | n/a |
| EXPERIMENT-02 design and result | data/experiments/EXPERIMENT-02-design-and-result.docx | Ana Fialho | registered 2026-05-28 | last edited 2026-07-21 |
| EXPERIMENT-02 results | data/experiments/EXPERIMENT-02-results.xlsx | Ana Fialho | compiled 2026-07-18 | unknown |
| DECISION-0028 | data/decisions/DECISION-0028-pilot-scope-change.docx | Ana Fialho | decided 2026-08-07 | unknown |
| Launch readiness checklist | data/launch/launch-readiness-checklist.xlsx | Ana Fialho | unknown | last updated 2026-08-26 |
| Adoption measures | data/launch/adoption-measures-draft.xlsx | Ana Fialho | unknown | status draft, not agreed |
| Headcount | data/people/headcount.xlsx | unknown | unknown | unknown |

## Current process

The trace of OPPORTUNITY-04 as it actually happened, in date order. "Evidence" is what the record
shows the step rested on, not what it should have rested on. Nothing below is inferred to fill a
gap. Gaps are written as unknown.

| Step | Actor | System or artifact | Input | Output | Decision | Evidence | Problem or unknown |
| -: | :- | :- | :- | :- | :- | :- | :- |
| 1 | Gabriela Rocha, then Ana Fialho | Conversation, no artifact | Two upcoming renewals (Ana interview) | The question "can we widen the pilot" | None. A question now exists and "does not go away" | Ana's recollection on 2026-08-12 | Date unknown. No record of the request before the brief. The only source is the interview |
| 2 | Ana Fialho | EXPERIMENT-02 design | Unknown what prompted it | Registered experiment: six accounts, six weeks, two success criteria | Thresholds set before running | Design document, registered 2026-05-28 | The thresholds visible today (first response p50 under 75 min, self-service at or above 35%) are the adjusted ones (see step 8). The originally registered values are not recorded anywhere |
| 3 | Ana Fialho | OPPORTUNITY-04 brief | Pilot figures "from analytics", a market estimate | Brief recommending a launch readiness assessment for 40 accounts | Proceed to readiness assessment | 71% suggested, 58% sent without edit, first response 22 min against a 94 min baseline, self-service 58% | Figures carry no date, query or measure version (the Dependencies doc says this is normal). They disagree with EXPERIMENT-02 (72 min, 36.9%). Whether they measure different populations is unknown. The brief says 12 accounts for six weeks, while the experiment used six accounts from 2026-06-01. Never revised after 2026-06-18 |
| 4 | Ana Fialho, Kofi Adjei | Expansion design (Draft) | OPPORTUNITY-04 | Proposed per-account enablement, per-area thresholds, routing on account commitments | None. Circulated 2026-07-09, no comments received | The design itself | States support has not given a review capacity number. States knowledge base quality is assumed and untested. Says billing routes to a human for Business and Enterprise, while INCIDENT-01 is a billing answer sent without a human. The INCIDENT-01 account tier is not recorded, so whether this is a contradiction is unresolved |
| 5 | Tomas Silva (blocking), Ana Fialho (asking) | Tracker row BLOCKER-01 | POLICY-03, LATAM accounts in scope | Open blocker | Sign-off withheld for LATAM accounts only | Tracker opened 2026-07-11. Checklist row 3 "open since 2026-07-11" | Tracker owner field is empty. "Asked three times" on 2026-08-12 and still three on 2026-08-22. No escalation path exists (how-we-work doc, and Ana: the person she would escalate to is the person waiting) |
| 6 | On-call engineer and solution consultant, both unnamed | INCIDENT-01, INCIDENT-02 | Pilot suggestions sent without human review | Two write-ups | Both closed in retrospective without a control and without a follow-up owner | Incident documents written 2026-07-14 and 2026-07-29 | INCIDENT-01 is a POLICY-01 case (billing answer), and POLICY-01 is enforced by nothing. The date INCIDENT-02 occurred is not stated. Who changed the superseded article's status, and when, is not recorded. OPPORTUNITY-04 was not revised after either |
| 7 | Ana Fialho | EXPERIMENT-02 results workbook | Six weeks of pilot data, 2026-06-01 to 2026-07-15 | Per-account figures, "Met" against both criteria | Both criteria met | Workbook compiled 2026-07-18 | The workbook's Median row is empty. Recomputing from the six rows gives 72 min and 36.9%, which matches the design document. Which analytics measure version produced the figures is unknown |
| 8 | Ana Fialho, others unnamed | Discussion, then an edit to the EXPERIMENT-02 document | A result that, per Ana, "beat one measure and missed the other" | Threshold "adjusted". Document last edited 2026-07-21 reads "Both criteria met" and "supports widening" | A threshold was changed after the result was known | None recorded. Mei Tan asked where it would be recorded. Ana: "Nowhere. That is your answer." | CONTRADICTION. The document says both criteria were met against pre-set thresholds. Its author says one was missed and the threshold then moved. Which threshold changed, from what value, and who agreed are all unknown. Unresolved |
| 9 | Ana Fialho | Pilot incidents, product view | Both incident write-ups | A statement of what the incidents mean for expansion | None. "Nobody has been asked to decide" whether either incident blocks expansion | Document dated 2026-08-04 | The decision was named and then assigned to nobody |
| 10 | Gabriela Rocha | Request REQUEST-G01 | Nordkai result | Request to quote pilot numbers in renewals | None recorded | Received 2026-08-05 | Nordkai 51 min matches the experiment workbook. The 112 min baseline she quotes appears in no artifact. The brief's 94 min baseline covers a different population. Tracker has no "last touched" date |
| 11 | Ana Fialho (sole approver) | DECISION-0028 | 16 account manager requests, OPPORTUNITY-04, verbal engineering confirmation | Pilot widened from 12 to 28 accounts | Treated as a "scope change to the existing pilot rather than a launch" | OPPORTUNITY-04 (stale since step 6) and a verbal statement. Decided 2026-08-07 | POLICY-08 requires a documented launch-readiness decision above 25 accounts. 28 exceeds it, and the readiness assessment (LAUNCH-01) was not opened until 2026-08-19. Nothing checked. No record that Rui Bastos or Tomas Silva agreed, although Ana names both as required. Whether any of the 16 accounts is LATAM is unknown. Does not reference either incident. Says "no change to the review process". Whether 28 accounts are actually enabled today is not recorded in this repository |
| 12 | Rui Bastos | Request REQUEST-R01 | Review queue load on six engineers | Written request: do not widen until the review share falls | None recorded | Received 2026-08-08, the day after DECISION-0028 | Rui says he raised this in three earlier meetings. Their dates and any minutes are not recorded. Tracker note: "Not reflected in the brief" |
| 13 | Tomas Silva | Request REQUEST-T01 | POLICY-03 | Written statement of the same blocker as step 5 | Sign-off withheld for LATAM. EU and NA unaffected | Received 2026-08-11 | Duplicates BLOCKER-01 in the tracker, so the two rows can drift apart |
| 14 | Ana Fialho, Mei Tan | Interview | n/a | Account of how decisions happen | n/a | Interview 2026-08-12 | Ana says the decision records folder has four records. The repository holds two. Unresolved which is true. The interviewer's follow-ups (brief owner, original threshold, asking Tomas directly) have no recorded outcome |
| 15 | Ana Fialho | Request REQUEST-A01 | Engineering planning needs | Deadline: decide by end of August | None | Received 2026-08-13. Tracker "last touched" for OPPORTUNITY-04 is also 2026-08-13 | The deadline passed with no decision and no recorded decision to defer. Tracker marks it "Now overdue" |
| 16 | Rui Bastos, Mei Tan | Interview | n/a | "I object to expanding before the review queue is solved" | n/a | Interview 2026-08-19 | The measure that would change his mind (share of suggestions needing a human) is not measured. Whether Sofia Marques (Analytics) was asked is not recorded |
| 17 | Ana Fialho | Tracker rows LAUNCH-01, ADOPT-01 | POLICY-08, OPPORTUNITY-04 | Readiness assessment opened 2026-08-19. Adoption measures task opened 2026-08-20 | None | Tracker | LAUNCH-01 opened twelve days after the scope had already passed 25 accounts. Adoption measures are "draft, not agreed", and the one support asked for has "Not measured" as its source |
| 18 | Ana Fialho (owner), row owners as listed | Launch readiness checklist | Row owners' beliefs | Six rows Yes, three rows No | Not ready, since "ready when every row reads Yes" | Checklist last updated 2026-08-26 | Row 1 (answer quality) is Yes with no evidence, while the brief lists it as unproven and the design says it is untested. Row 2 (review capacity, owner Rui Bastos) is Yes with no evidence, contradicting Rui's request and interview. Who ticked it is unknown. Row 4 cites "assist-expansion-design.docx", which does not exist, and the design that does exist has no rollback section. Row 6 checks against POLICY-10, superseded by POLICY-11 on 2026-07-01. Row 7 says the "pre-registered threshold" was met, which step 8 contradicts. Row 8 is Yes with no evidence |
| 19 | Nobody recorded | n/a | n/a | n/a | No expansion decision, and no decision to defer or reject | The latest dated record is the checklist, 2026-08-26 | As of 2026-09-24 OPPORTUNITY-04 is "Open", REQUEST-A01 is overdue, BLOCKER-01 has no owner, and neither incident has a follow-up owner. What happened after 2026-08-26 is unknown |

## Where the current process lost information

This is the red state for Module 1: the points in the trace where a fact the decision depends on
stopped being carried forward.

1. **The evidence went stale and nothing noticed.** OPPORTUNITY-04 was written before both
   incidents, was never revised, and was still cited as evidence for DECISION-0028 on 2026-08-07.
   No artifact carries a review date, so nothing marks it as stale.
2. **A threshold moved after the result, and the record kept only the new value.** EXPERIMENT-02
   reads as a clean pass. Its author says it was not. The original threshold cannot be recovered
   from the repository.
3. **A policy gate was crossed by relabelling.** POLICY-08 applies above 25 accounts.
   DECISION-0028 reached 28 by calling it a scope change. The readiness assessment the policy
   requires was opened afterwards and is still incomplete.
4. **An objection became a tick.** Rui Bastos's objection exists in writing (2026-08-08) and on the
   record (2026-08-19). The checklist row he owns reads Yes with no evidence. The process cannot
   tell "considered" from "resolved", which is exactly what Rui and Ana each said an automated
   process must not decide.
5. **Blocked has no next step.** BLOCKER-01 has no owner, no escalation path, and the same ask
   count for ten days.
6. **Decisions that were named were never assigned.** Whether the incidents block expansion
   (2026-08-04) and the end-of-August decision itself (2026-08-13) both reached a question or a
   deadline without anyone owning the answer.

## Unresolved contradictions

Reported as found. None is resolved here.

| Fact | Source A says | Source B says |
| :- | :- | :- |
| EXPERIMENT-02 outcome | Design document and workbook: both criteria met | Ana Fialho interview: one met, one missed, threshold then adjusted |
| Pilot performance | OPPORTUNITY-04: 22 min first response, 58% self-service | EXPERIMENT-02: 72 min, 36.9% |
| Nordkai baseline | Gabriela Rocha request: 112 min | No artifact records a Nordkai baseline. The brief's 94 min baseline is for the pilot overall |
| Review capacity confirmed | Checklist row 2: Yes | Rui Bastos request and interview: not confirmed, objects to widening first |
| Answer quality reviewed | Checklist row 1: Yes | Brief: an unproven risk. Design: untested |
| Number of decision records | Ana Fialho interview: four | Repository: two |
| Billing answers reach a human | Expansion design: billing routes to a human for Business and Enterprise | INCIDENT-01: a billing answer went out unread (account tier not recorded) |
| Who must agree to expansion | How-we-work doc and Ana interview: support and legal agree where affected | DECISION-0028: sole approver Ana Fialho |

## Missing controls observed (not built)

Recorded as observations only. Building them belongs to later modules.

- A review-by date or supersession link on briefs and decision evidence would have flagged
  OPPORTUNITY-04 as stale before DECISION-0028 cited it.
- An immutable record of experiment thresholds at registration would have preserved the original
  EXPERIMENT-02 value.
- A check of account count against POLICY-08 on any scope change would have refused DECISION-0028
  without a readiness decision.
- A checklist row that cannot read Yes without an evidence link would have kept rows 1, 2 and 8 at
  No. A check against superseded policies would have caught row 6.
- A blocker that must carry an owner and an escalation target would have prevented BLOCKER-01's
  stall.

## Proposed lifecycle

Rename stages when the domain requires it. Add waiting, failure, escalation, and terminal states.

| Common stage | Track-specific state | Entry conditions | Evidence produced | Next states | Owner | Stop or escalation condition |
| :- | :- | :- | :- | :- | :- | :- |
| Intake | TODO | TODO | TODO | TODO | TODO | TODO |
| Context | TODO | TODO | TODO | TODO | TODO | TODO |
| Route | TODO | TODO | TODO | TODO | TODO | TODO |
| Act | TODO | TODO | TODO | TODO | TODO | TODO |
| Verify | TODO | TODO | TODO | TODO | TODO | TODO |
| Approve | TODO | TODO | TODO | TODO | TODO | TODO |
| Handoff | TODO | TODO | TODO | TODO | TODO | TODO |
| Observe | TODO | TODO | TODO | TODO | TODO | TODO |
| Recover | TODO | TODO | TODO | TODO | TODO | TODO |

## Human judgment boundaries

| Decision | Why it is not mechanical | Decision owner | Evidence prepared by a skill |
| :- | :- | :- | :- |
| TODO | TODO | TODO | TODO |

## Failure and recovery

| Failure or blocked state | Detection signal | Recovery path | Retry limit | Escalation owner |
| :- | :- | :- | :- | :- |
| TODO | TODO | TODO | TODO | TODO |

## Terminal states

| State | Business outcome represented | Required final evidence |
| :- | :- | :- |
| TODO | TODO | TODO |

## Open questions

- TODO

