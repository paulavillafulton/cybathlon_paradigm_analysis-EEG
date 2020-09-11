<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="xdf to csv" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(120.0, 200.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="0f47faf3-c9fd-42be-b0cf-ee93da69dd17" version="1.0.0" />
		<node id="1" name="Export to CSV" position="(434.0, 230.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owexportcsv.OWExportCSV" title="Export to CSV" uuid="1b311ada-0262-4050-a063-bf4ac8f91d43" version="1.0.0" />
		<node id="2" name="Export Markers to CSV" position="(404.0, 414.0)" project_name="NeuroPype" qualified_name="widgets.markers.owexportmarkers.OWExportMarkers" title="Export Markers to CSV" uuid="1c3ce1eb-f14c-4b55-9f08-96496466fd3c" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="literal" node_id="0">{'cloud_account': '', 'cloud_bucket': '', 'cloud_credentials': '', 'cloud_host': 'Default', 'filename': '', 'handle_clock_resets': True, 'handle_clock_sync': True, 'handle_jitter_removal': True, 'retain_streams': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'verbose': False}</properties>
		<properties format="literal" node_id="1">{'axis_description': '', 'cloud_account': '', 'cloud_bucket': '', 'cloud_credentials': '', 'cloud_host': 'Default', 'col_axis': 'space', 'column_header': True, 'filename': 'untitled.csv', 'output_root': '', 'row_axis': 'frequency', 'row_header': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAgAAABmaWxlbmFtZXEBWAsAAABtYXJrZXJzLmNzdnECWAsAAABvdXRwdXRfcm9vdHED
WAAAAABxBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgM
AAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAAAAMEAAABlwAABHsA
AAJiAAADDAAAAbYAAARzAAACWgAAAAEAAHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtwb2ludHEN
iVgGAAAAc3RyZWFtcQ5YDQAAACh1c2UgZGVmYXVsdClxD3Uu
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node1",
            "data",
            "node3",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0f47faf3-c9fd-42be-b0cf-ee93da69dd17"
        },
        "node2": {
            "class": "ExportCSV",
            "module": "neuropype.nodes.file_system.ExportCSV",
            "params": {
                "axis_description": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "untitled.csv"
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "frequency"
                },
                "row_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1b311ada-0262-4050-a063-bf4ac8f91d43"
        },
        "node3": {
            "class": "ExportMarkers",
            "module": "neuropype.nodes.markers.ExportMarkers",
            "params": {
                "filename": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "markers.csv"
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                }
            },
            "uuid": "1c3ce1eb-f14c-4b55-9f08-96496466fd3c"
        }
    },
    "version": 1.1
}</patch>
</scheme>
