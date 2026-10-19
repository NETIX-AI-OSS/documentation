# NETIX.AI connector for Claude

The NETIX.AI connector lets [Claude](https://claude.ai) work with your NETIX.AI data. Ask questions in plain language and Claude looks up the answer in your organization's assets, work orders, complaints, compliance records, contracts and building telemetry. Available tools also support analysis, charts, document rendering and selected operational actions. Access depends on your deployment and permissions.

- **Server URL:** `https://ml-engine.api.netixai.com/mcp`
- **Sign-in:** your NETIX.AI account (OAuth)
- **Clients:** Claude web, mobile, Desktop and Claude Code, subject to client availability and organization policy
- **Support:** [support@netix.ai](mailto:support@netix.ai)

## Before you start

You need:

- A NETIX.AI account in an organization that uses the NETIX.AI platform. Ask your NETIX administrator if you don't have one.
- A Claude account with access to connectors. Your Claude organization administrator may need to enable the connector first.

## Connect from Claude on the web or Claude Desktop

1. Open [Customize > Connectors](https://claude.ai/customize/connectors) in Claude.
2. Add a custom connector and enter the server URL `https://ml-engine.api.netixai.com/mcp`.
3. Select **Connect**. Claude opens the NETIX.AI sign-in page.
4. Sign in with your NETIX.AI account (password, MFA or single sign-on, as you normally would), then approve access on the consent screen.
5. Back in Claude, the connector shows **Connected** under **Your connectors**.

To use it in a conversation, turn it on from **+ > Connectors**, then ask a question such as *"How many open complaints do we have, grouped by status?"*

## Connect from Claude Code

```bash
claude mcp add --transport http netix-ai https://ml-engine.api.netixai.com/mcp
```

Then run `/mcp` inside Claude Code, choose `netix-ai`, and sign in with your NETIX.AI account in the browser window that opens.

If you'd rather authenticate with a NETIX API key than sign in through the browser, install the [NETIX AI plugin for Claude Code](https://github.com/NETIX-AI-OSS/netix-claude-plugin) instead. It bundles this connection plus a skill that teaches Claude the platform's conventions.

## What Claude can access

For a regular organization account, signing in ties the connector to that NETIX.AI organization. Supplying a different organization ID does not grant access to another tenant. Platform superadministrator accounts require separate administrator configuration and should not be used for routine connector access.

Your NETIX administrator may limit the connector to organization administrators, or cap the number of tool calls per month. If a call is refused for either reason, Claude shows the reason it received.

## Tools

Tool names start with their area, for example `work_orders_reactive_work_order_list`. **Read** tools retrieve data or render supplied content. **Write** tools can change NETIX.AI records. Review a write call and its arguments before allowing it in your client. A connector call does not guarantee a separate NETIX approval card; a permitted write may execute immediately. Permission-gated features may refuse a call.

### Facilities and telemetry

| Tool | Type | What it does |
| --- | --- | --- |
| `facilities_realtime_data_retrieve` | Read | Latest real-time sensor values for the given tags |
| `facilities_data_query_retrieve` | Read | Historical time-series data and summary statistics for tags |
| `facilities_analytics_query_retrieve` | Read | Analytics for one tag: thresholds, comparisons and predictions |
| `facilities_asset_data_card_retrieve` | Read | Latest telemetry snapshot for one asset, with every tag on it |
| `facilities_iot_asset_status_list` | Read | Current online, degraded or offline status of monitored assets |
| `facilities_iot_offline_log_list` | Read | History of connectivity status changes |
| `facilities_alarm_log_list` | Read | Alarm firing history |
| `facilities_alarm_rule_template_list` | Read | Reusable alarm rule templates |
| `facilities_recommendation_list` | Read | Your organization's published recommendations |
| `facilities_prediction_model_benchmark` | Compute | Accuracy of a trained prediction model, plus a forward forecast |
| `facilities_alarm_rule_template_apply` | Write | Applies an alarm rule template to an asset, creating alarm rules |
| `facilities_ai_alarm_config` | Write | Generates alarm and fault-detection rules for an asset from a week of its data |
| `facilities_prediction_model_train` | Write | Trains prediction models for an asset's tags |
| `facilities_recommendation_feedback` | Write | Records your accept or dismiss decision on a recommendation |

### Work orders

| Tool | Type | What it does |
| --- | --- | --- |
| `work_orders_service_request_list` | Read | Service requests |
| `work_orders_reactive_work_order_list` | Read | Reactive work orders |
| `work_orders_ppm_work_order_list` | Read | Planned preventive maintenance (PPM) work orders |
| `work_orders_ctamp_occurrence_list` | Read | Scheduled PPM occurrences |
| `work_orders_fault_list` | Read | Fault definitions and codes |
| `work_orders_fault_category_list` | Read | Fault categories |
| `work_orders_service_category_list` | Read | Service categories |
| `work_orders_material_inventory_list` | Read | Spare parts, materials and stock |
| `work_orders_user_resolve` | Read | Names and emails for user IDs found on records |
| `work_orders_recommendation_list` | Read | Your organization's published recommendations |
| `work_orders_service_request_create` | Write | Raises a new service request |
| `work_orders_reactive_work_order_create` | Write | Raises a new reactive work order |
| `work_orders_reactive_work_order_comment_create` | Write | Adds a comment to a work order |
| `work_orders_recommendation_feedback` | Write | Records your accept or dismiss decision on a recommendation |

### Complaints

| Tool | Type | What it does |
| --- | --- | --- |
| `complaints_complaint_list` | Read | Complaints and their status |
| `complaints_complaint_activity_list` | Read | Timeline of actions taken on a complaint |
| `complaints_complaint_escalation_list` | Read | Complaint escalations and their level |
| `complaints_complaint_follow_up_list` | Read | Scheduled and completed follow-ups |
| `complaints_complaint_work_order_list` | Read | Work orders linked to complaints |
| `complaints_cafm_analytics` | Read | Aggregates, time series and raw rows across CAFM records |
| `complaints_building_type_list` | Read | Building types |
| `complaints_client_list` | Read | Clients (tenants and customers) |

### Compliance

| Tool | Type | What it does |
| --- | --- | --- |
| `compliance_work_permit_list` | Read | Safety work permits and their status |
| `compliance_audit_inspection_list` | Read | Scheduled and routine inspections |
| `compliance_access_card_list` | Read | Access cards and their approval status |
| `compliance_access_permit_list` | Read | Visitor and contractor access permits |
| `compliance_access_parking_list` | Read | Parking access records |

### Commercial

| Tool | Type | What it does |
| --- | --- | --- |
| `commercial_contract_list` | Read | Contracts |
| `commercial_contract_sla_list` | Read | Service level agreements for a contract |
| `commercial_quotation_list` | Read | Quotations |
| `commercial_vendor_list` | Read | Vendors and suppliers |

### Assets

| Tool | Type | What it does |
| --- | --- | --- |
| `asset_asset_list` | Read | Assets in your facility hierarchy |
| `asset_asset_class_list` | Read | Asset classes, such as HVAC, electrical or plumbing |
| `asset_asset_level_list` | Read | Hierarchy levels, such as site, building, floor or room |
| `asset_asset_map_list` | Read | Asset maps for a site or building layout |
| `asset_recommendation_list` | Read | Your organization's published recommendations |
| `asset_recommendation_feedback` | Write | Records your accept or dismiss decision on a recommendation |

### Documents

| Tool | Type | What it does |
| --- | --- | --- |
| `documents_list_document_templates` | Read | NETIX document and email templates |
| `documents_preview_document_template` | Read | Renders a template with sample data to preview its layout |
| `documents_render_document` | Read | Renders a template into branded, email-ready HTML |

### Analysis and charts

Every area except Documents also has these two tools, for example `work_orders_execute_code` and `asset_generate_chart`:

| Tool | Type | What it does |
| --- | --- | --- |
| `<area>_execute_code` | Compute | Runs Python (pandas, NumPy) in a NETIX sandbox to analyse results from earlier tool calls. Available where your deployment enables it. |
| `<area>_generate_chart` | Compute | Builds a chart from data |

**Compute** tools perform analysis or produce chart configurations. Code execution depends on the deployment's sandbox setting. Chart generation needs analysis results in a shared execution context and can be unavailable in stateless sessions.

## Example prompts

- *How many assets are offline right now, and since when?*
- *List reactive work orders created this week for HVAC, grouped by priority.*
- *Chart service requests per month for the last year.*
- *Which contracts expire in the next 90 days, and who are the vendors?*
- *Show the alarm history for chiller 2 over the last 7 days.*

## Data handling

- **What NETIX receives:** your authentication information and each tool call's name and arguments. The connector does not automatically forward your whole Claude conversation; relevant text can be included in tool arguments.
- **Operational data:** NETIX processes calls against the connected organization's services. Usage accounting and operational logging support service operation and tool-call limits. Ask NETIX for the data handling and retention terms applicable to your deployment.
- **What Claude receives:** the results of each tool call, which become part of your conversation in Claude. Anthropic's handling of conversation data is covered by your Claude plan's terms.
- **Revoking access:** disconnect the connector in Claude under **Customize > Connectors**. To revoke access from the NETIX side, contact your NETIX administrator or [support@netix.ai](mailto:support@netix.ai).

See the [published NETIX.AI privacy policy](https://www.netix.ai/privacy-policy). For questions about connector data handling or retention, contact [support@netix.ai](mailto:support@netix.ai).

## Troubleshooting

| Symptom | What to do |
| --- | --- |
| The connector shows **Connect** or **Reconnect** | Sign-in didn't finish. Select it again and complete the NETIX.AI sign-in and consent screens. |
| A tool says the integration is limited to organization administrators | Your deployment restricts the connector to administrators. Ask an administrator in your organization. |
| A tool says the organization has reached its monthly tool-call allowance | Your organization has used its tool calls for the month. Contact your NETIX administrator. |
| A tool is refused or returns an error | Verify your permissions and organization configuration. Retry a bounded read query; if it still fails, contact support with the tool name and time. |
| Results are empty | Check that the data exists in NETIX.AI for your organization, for example that IoT monitoring is configured for the asset. |

For anything else, email [support@netix.ai](mailto:support@netix.ai) with the time of the problem and the tool name Claude showed.

## More information

- [NETIX.AI brochures and guides](https://www.netix.ai/brochures-and-guides)
- [NETIX.AI website](https://www.netix.ai)
- [Documentation source](https://github.com/NETIX-AI-OSS/documentation)

Last updated: 19 October 2026. Tool availability and permissions depend on your deployment.
