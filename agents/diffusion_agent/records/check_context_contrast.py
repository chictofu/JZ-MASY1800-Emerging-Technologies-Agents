"""Validate saved assistant-executed synthetic test artifacts; does not call a model."""
from pathlib import Path
import json
import jsonschema
root=Path(__file__).resolve().parents[3]
agent=root/'agents/diffusion_agent'
read=lambda p: json.loads(p.read_text())
cases=[read(agent/'cases'/f'{n}.json') for n in ['primary','contrast_1']]
responses=[read(agent/'responses'/f'{n}_response.json') for n in ['primary','contrast_1']]
for case in cases:
    jsonschema.Draft202012Validator(read(root/'core/input_schema.json')).validate(case)
for response in responses:
    jsonschema.Draft202012Validator(read(root/'core/output_schema.json')).validate(response)
changed=[k for k in set(cases[0])|set(cases[1]) if cases[0].get(k)!=cases[1].get(k)]
assert changed==['adoption_posture'], changed
for key in ['general_et_finding','application_finding','evidence']:
    assert responses[0][key]==responses[1][key], key
for response in responses:
    assert 'no justified formal Rogers stage' in response['organization_specific_finding']
    for field in ['general_et_finding','application_finding','organization_specific_finding']:
        for characteristic in ['Relative advantage:', 'Compatibility:', 'Complexity:', 'Trialability:', 'Observability:']:
            assert characteristic in response[field], (field,characteristic)
assert responses[0]['recommendation_management_implication']!=responses[1]['recommendation_management_implication']
assert 'PILOT_NOW_AFTER_SAFEGUARDS' in responses[0]['recommendation_management_implication']
assert 'DEFER_OPERATIONAL_TRIAL' in responses[1]['recommendation_management_implication']
print('PASS: both inputs and outputs satisfy full JSON schemas')
print('PASS: adoption_posture is the only changed input')
print('PASS: general/application findings and evidence remain identical')
print('PASS: five characteristics present in each finding scope')
print('PASS: timing changes from safeguarded pilot to conditional deferral')
print('LIMIT: structural and saved-output checks; qualitative review is recorded separately; no independent model execution')
