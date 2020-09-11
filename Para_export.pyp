<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="para_export" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(297.0, 399.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="e38a34ae-ada5-45d9-8933-f072881663ee" version="1.0.0" />
		<node id="1" name="Export MAT" position="(512.0, 389.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owexportmat.OWExportMAT" title="Export MAT" uuid="f0a5bb04-f7ff-4fa5-81fc-8cc895d520fc" version="0.5.0" />
		<node id="2" name="Time Series Plot" position="(503.0, 231.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="dda152bf-9bda-47e6-9eb5-b77e9028b01f" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWEgAAABDOi9Vc2Vycy9jeWJhdGhsb24vRGVza3RvcC9QYXJhZGlnbSBncm91
cC9yZWNvcmRlZF9kYXRhL1BBX3BhYmxvMjYwMS54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jlc2V0
c3EJiFgRAAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3ZhbHEL
iFgOAAAAcmV0YWluX3N0cmVhbXNxDFgNAAAAKHVzZSBkZWZhdWx0KXENWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQ5jc2lwCl91bnBpY2tsZV90eXBlCnEPWAwAAABQeVF0NC5RdENvcmVxEFgKAAAA
UUJ5dGVBcnJheXERQy4B2dDLAAEAAP//++4AAAG6///9ZQAAAyH///v2AAAB2f///V0AAAMZAAAA
AAAAcRKFcROHcRRScRVYDgAAAHNldF9icmVha3BvaW50cRaJWAcAAAB2ZXJib3NlcReJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWA4AAABwYXJhX3BhYmxvLm1hdHEIWAsAAABvdXRwdXRfcm9vdHEJWDcAAABD
Oi9Vc2Vycy9jeWJhdGhsb24vRGVza3RvcC9QYXJhZGlnbSBncm91cC9yZWNvcmRlZF9kYXRhcQpY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAAAFB5UXQ0
LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAA///7hAAAAXL///z7AAAChf//+4wA
AAGR///88wAAAn0AAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4l1Lg==
</properties>
		<properties format="literal" node_id="2">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': '#FF0000', 'nans_as_zero': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 5.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': True}</properties>
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
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/cybathlon/Desktop/Paradigm group/recorded_data/PA_pablo2601.xdf"
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
            "uuid": "e38a34ae-ada5-45d9-8933-f072881663ee"
        },
        "node2": {
            "class": "ExportMAT",
            "module": "neuropype.nodes.file_system.ExportMAT",
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
                    "customized": true,
                    "type": "StringPort",
                    "value": "para_pablo.mat"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/cybathlon/Desktop/Paradigm group/recorded_data"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f0a5bb04-f7ff-4fa5-81fc-8cc895d520fc"
        },
        "node3": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "dda152bf-9bda-47e6-9eb5-b77e9028b01f"
        }
    },
    "version": 1.1
}</patch>
</scheme>
