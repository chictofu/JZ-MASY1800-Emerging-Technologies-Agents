# Application-to-business-model map

Organization: fictional Northstar Media Agency. Primary application: hypothetical D1
AI/ML deal scoring with trader approval in a cautious pilot. Agency details below
are supplied assumptions; proposed effects are analytical hypotheses, not verified
real-world outcomes. Self-service is the contrasting proposed application.

| Dimension | Current baseline (scenario assumption) | Proposed change (hypothesis) | Evidence needed to judge the change |
|---|---|---|---|
| Value proposition | Accountable managed campaigns and expert trading | Recommendations may improve deal selection while preserving oversight; self-service may offer direct control | Comparable advertiser outcomes, error/incident rates, customer interviews and observed willingness to pay |
| Activities | Manual/fixed-rule review, trader approval and campaign management | Add scoring, exception review, monitoring and data maintenance; self-service also needs separate execution integration | Workflow records, trader time, exception rates, controller feasibility, permissions and rollback tests |
| Capabilities | Trader expertise, relationships and stipulated historical campaign data | Add data-quality management, model evaluation and ranking; implementation capability remains unverified | Data provenance/rights, skills inventory, technical integration and model evaluation |
| Economics | Managed-service fees; actual fee/margin and cost breakdown unknown | Potential screening savings offset by model, integration, review, monitoring and support costs; self-service may add subscription revenue or cannibalize fees | Full cost-to-serve, contribution margin, customer switching, pricing and existing/new customer segmentation |
| Channels/intermediation | Agency-managed service and trader decisions; acquisition channel unknown | Internal pilot retains agency intermediation; self-service could shift delivery and bypass routine curation | Channel behavior, customer retention, support needs and attribution of losses or new demand |
| Competitive position | Expertise and client relationships are assumed differentiators, not measured advantages | Efficiency might strengthen service; widely available ranking could commoditize routine curation while expertise remains valuable | Verified competitor offerings, customer choice, access to comparable tools, switching costs and defensibility |

## Value creation versus displacement
Internal recommendations could complement the existing business model: ranking ->
less screening effort -> more expert capacity -> better service or lower delivery
cost, only if outcome and cost evidence support those links.

Self-service could instead change value capture: ranking plus a separate delivery/
execution layer -> customer self-service -> reduced routine agency demand -> fee
pressure. Subscription or advisory revenue may offset this loss, but no demand,
margin replacement or customer substitution has been demonstrated.

No actual job loss, performance lift, customer migration, competitor adoption or
commercial launch is asserted. Low pilot impact and potentially substantial
self-service exposure are conditional interpretations, not market observations.

## Verified external facts and their limits
Source S1: IAB Tech Lab, OpenRTB 2.6 specification, sections 3.2.11 (Pmp) and 3.2.12
(Deal), retrieved from the official InteractiveAdvertisingBureau repository:
https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md

Verified from the retrieved text:
- Pmp is a private-marketplace container for direct buyer/seller deals applicable
  to an impression; specific deals are represented by Deal objects.
- Deal fields include an identifier, bid floor and currency, and optional buyer-seat
  and advertiser-domain restrictions.

These facts establish protocol context and relevant eligibility/price information,
not D1 capability, optimizer effectiveness, universal platform implementation,
commercialization history or business-model disruption. It is an analytical
implication, not a quote from S1, that a real integration should check applicable
deal terms and permissions rather than rank on predicted outcomes alone.

The exact retrieved source and SHA-256 metadata are retained in source_verification/.
The upstream main branch can change; the retained snapshot identifies what was checked.
Google's Authorized Buyers deal documentation could not be retrieved because the
network proxy returned 403. It is not used as supporting evidence.

## Claims requiring further verification
- Actual technology/vendor/model: D1 is fictional. Use original technical documents
  and implementation evidence if choosing a real product.
- Performance: require controlled campaign evidence; vendor marketing or ranking
  accuracy alone cannot verify advertiser-value improvement.
- Commercialization history: require dated original launch/availability records.
- Competitors/market events: require identifiable original announcements, filings
  or relevant customer adoption evidence; triangulate consequential claims.
- Business-model shifts: require actual customer switching, contracts/pricing,
  revenue/margin changes and credible attribution, not hypothetical substitution alone.

## Decision implication and boundaries
This map supports a bounded investigation, not deployment approval. With no verified
outcomes, economics or competitor adoption, the larger timing risk remains
Undetermined. Test outcomes/costs and monitor genuine alternatives without inventing urgency.
Hand actual market mapping to landscape, uptake to diffusion, implementation capacity
to organizational-readiness, adoption approval to adoption and stakeholder ethics to
Promethean. Retain innovation and value-creation/displacement analysis here.
