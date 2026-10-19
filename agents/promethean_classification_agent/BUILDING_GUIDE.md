# Assignment 04 — Promethean Technology Classification Agent: building guide

## 1. Purpose
Answer the Assignment 4 governing question: is the technology incremental, breakthrough
or potentially civilization-changing, and what should that imply for this organization's
application today? Read specialist_instructions.md for the challengeable decision criteria.
Broad importance and local adoption suitability must remain separate.

## 2. What was used and what is editable
Inputs: the uploaded Assignment 4 memo, Lab 5 learning document and frozen scaffold v1.0.
Only this new agent folder is specialized. The uploaded ZIP, template, core instructions,
common input/output schemas and tools remain unchanged. Missing baseline files were
restored byte-for-byte from the verified uploaded ZIP.

This branch starts from main and keeps Assignment 3 on its separate branch.
No new API account or API key is needed. Use the existing checkout; tasks already run
in isolated environments, so no Git worktree is needed unless explicitly requested.

## 3. Lab 5 concepts translated into behavior
| Lab 5 lesson/question | Agent rule |
|---|---|
| Investment/media attention is weak evidence | Demand capability, breadth, depth and durable mechanisms; hype cannot supply a label |
| Broad potential can coexist with a poor local fit | Keep general, application and organization findings separate |
| Can investment/adoption enable transformation? | Trace financing -> infrastructure/skills -> capability/use -> structural outcomes; verify each link |
| When should managers stop an unsuccessful implementation? | Pre-agree measurable cost/outcome/safety/learning/time gates; stop or redesign local work while retaining technology monitoring |

The notes' AI and metaverse examples are not treated as independently verified facts.

## 4. Prepare and inspect
From the repository root:

```sh
python tools/check_frozen_core.py
sha256sum -c PACKAGE_SHA256.txt
```

The new agent was created with:

```sh
python tools/new_agent.py promethean_classification_agent "Promethean Technology Classification Agent" --specialty "Technological significance, evidence calibration, and separation from local adoption"
```

Do not repeat new_agent.py when the folder already exists.

## 5. Select and document the case
The starter keeps continuity with Assignment 3: a hypothetical D1 ranking system for
programmatic advertising deals at a fictional agency. This is a narrow technology scope;
do not infer all AI is incremental from it. The primary is a cautious human-approved
pilot. contrast_1 changes only posture; contrast_2 changes organizational readiness.
Additional cases test hype pressure and a separate hypothetical broad-capability technology.
These are labeled scenario assumptions, not observed market facts.

For a real case, replace assumptions in cases/ while retaining common input fields.
Include dated original evidence in additional_context: technology/version, technical
baseline, comparative capability, deployment breadth, enabling infrastructure and
counterevidence. Current sources must be checked before actual-market claims are made.

## 6. Build a complete prompt packet
From the repository root:

```sh
python tools/build_prompt.py --agent agents/promethean_classification_agent --case agents/promethean_classification_agent/cases/primary.json
```

Repeat with contrast_1.json, contrast_2.json, hype_pressure.json and broad_potential.json.
Generated files appear under work/promethean_classification_agent_<case>_prompt.txt.
Committed copies are preserved under records/prompts/ so GitHub users can open them.

## 7. Run in ChatGPT and save the result
Open the complete prompt packet, paste its entire contents into a fresh ChatGPT conversation,
and request only the common JSON object. Save the reply as responses/<case>_chatgpt.json.
Do not overwrite supplied Codex example responses; preserve runtime and prompt provenance.
No API calls are made by the scaffold scripts.

```sh
python tools/validate_response.py agents/promethean_classification_agent/responses/primary_chatgpt.json
```

Repeat for each response. The supplied validator checks basic fields/types, not all JSON
Schema constraints or analytical validity. Full-schema checks in this build use the
environment's existing jsonschema package; the standard reference workflow needs no pip install.

## 8. Assess the contrasts
The same technology and general evidence should produce a stable broad classification
under cautious and aggressive postures. Poor data/skills should change local implications,
not technology facts. Hype should not change the classification. The broad_potential
case intentionally uses a different hypothetical technology and is a boundary test,
not evidence that changing organization changes D1's significance.

Check both supporting and opposing evidence, uncertainty, missing information and the
three output levels. Preserve any overclaim, diagnose it and revise student instructions.
Constructed failure fixtures are labeled as such; they are not failed live model runs.

## 9. Evidence, record and handoff
See records/agent_record.md, test_record.md, lab5_traceability.md and revision_log.md.
Codex-generated structured examples are illustrative same-assistant evaluations, not
independent ChatGPT runs or empirical technology validation. Real-world classification
remains unverified where no original evidence is supplied.

Team rule: long-term importance never supplies automatic approval for near-term adoption.
Hand actual adoption decisions to adoption, implementation capacity to readiness,
uptake patterns to diffusion, business-model exposure to innovation/disruption and
vendor/competitor evidence to landscape specialists.

## 10. Git workflow
Branch: assignment-4-promethean-technology-classification.
Save the agent folder and baseline restoration, review the diff, commit and push this branch.
Do not merge into main as part of this build. Record the commit and links in the Agent Record.
Keep course effort bounded; unresolved factual/model validation stays explicit rather
than being hidden by architectural changes or fabricated evidence.
