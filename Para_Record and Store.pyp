<?xml version='1.0' encoding='utf-8'?>
<scheme description="You can recored and store datasets with this pipeline. The marker stream should be sent as an LSL stream." title="Record ans Store" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(56.0, 237.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="784726fd-a4df-4153-abf0-f8d25f448de5" version="1.0.0" />
		<node id="1" name="Dejitter Timestamps" position="(218.0, 240.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="42163767-848e-45ea-a981-ce63da1a1a97" version="1.0.0" />
		<node id="2" name="Record to XDF" position="(686.0, 83.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="906d73ca-8dcb-4849-960b-1f182d1c515d" version="1.0.0" />
		<node id="3" name="Time Series Plot" position="(693.0, 412.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="29f1cde6-905a-4aef-970d-aff91649b63a" version="1.0.0" />
		<node id="4" name="Merge Streams" position="(381.0, 240.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" title="Merge Streams" uuid="4e8fe1db-7876-454a-9eac-24533b6b1d99" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data1" sink_node_id="4" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Outdata" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="2" source_channel="Outdata" source_node_id="4" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgTAAAAbmFtZT0nRXJyUC1NYXJrZXJzJ3EFWAwAAABtYXhfYmxvY2tsZW5xBk0A
BFgKAAAAbWF4X2J1ZmxlbnEHSx5YDAAAAG1heF9jaHVua2xlbnEISwBYDAAAAG5vbWluYWxfcmF0
ZXEJWA0AAAAodXNlIGRlZmF1bHQpcQpYBQAAAHF1ZXJ5cQtYDwAAAG5hbWU9J0VFR19kYXRhJ3EM
WAcAAAByZWNvdmVycQ2IWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEORz/gAAAAAAAAWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENv
cmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAP//+6UAAAE////9HAAAAqz///utAAABXv//
/RQAAAKkAAAAAAAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
///+iAAAAYz/////AAACbP///pAAAAGr////9wAAAmQAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWAAAAABxA1gN
AAAAY2xvdWRfYWNjb3VudHEEaANYDAAAAGNsb3VkX2J1Y2tldHEFaANYEQAAAGNsb3VkX2NyZWRl
bnRpYWxzcQZoA1gKAAAAY2xvdWRfaG9zdHEHWAcAAABEZWZhdWx0cQhYDgAAAGNsb3VkX3BhcnRz
aXplcQlLHlgMAAAAZGVsZXRlX3BhcnRzcQqIWAgAAABmaWxlbmFtZXELWAkAAAB0ZXN0Mi54ZGZx
DFgLAAAAb3V0cHV0X3Jvb3RxDVgoAAAAQzovVXNlcnMvY3liYXRobG9uL0Rlc2t0b3AvQXJvdXNh
bF9ncm91cHEOWAsAAAByZXRyaWV2YWJsZXEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3Np
cApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDQuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0Mu
AdnQywABAAD///2+AAABqv///zUAAANZ///9xgAAAcn///8tAAADUQAAAAAAAHEUhXEVh3EWUnEX
WA0AAABzZXNzaW9uX25vdGVzcRhoA1gOAAAAc2V0X2JyZWFrcG9pbnRxGYlYBwAAAHZlcmJvc2Vx
Gol1Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgJAAAAYXV0b3NjYWxlcQSIWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNG
RkZGRkZxBlgQAAAAZGVjb3JhdGlvbl9jb2xvcnEHWAcAAAAjMDAwMDAwcQhYCwAAAGRvd25zYW1w
bGVkcQmJWAwAAABpbml0aWFsX2RpbXNxCl1xCyhLMksyTbwCTfQBZVgKAAAAbGluZV9jb2xvcnEM
WAcAAAAjMDAwMDAwcQ1YCgAAAGxpbmVfd2lkdGhxDkc/6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9y
cQ9YBwAAACNGRjAwMDBxEFgMAAAAbmFuc19hc196ZXJvcRGJWA4AAABvdmVycmlkZV9zcmF0ZXES
WA0AAAAodXNlIGRlZmF1bHQpcRNYDAAAAHBsb3RfbWFya2Vyc3EUiFgLAAAAcGxvdF9taW5tYXhx
FYlYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxFmNzaXAKX3VucGlja2xlX3R5cGUKcRdYDAAAAFB5
UXQ0LlF0Q29yZXEYWAoAAABRQnl0ZUFycmF5cRlDLgHZ0MsAAQAA///9ygAAAND///9BAAADRf//
/dIAAADv////OQAAAz0AAAAAAABxGoVxG4dxHFJxHVgFAAAAc2NhbGVxHkc/8AAAAAAAAFgOAAAA
c2V0X2JyZWFrcG9pbnRxH4lYDAAAAHNob3dfdG9vbGJhcnEgiVgLAAAAc3RyZWFtX25hbWVxIWgT
WAoAAAB0aW1lX3JhbmdlcSJHQBQAAAAAAABYBQAAAHRpdGxlcSNYEAAAAFRpbWUgc2VyaWVzIHZp
ZXdxJFgKAAAAemVyb19jb2xvcnElWAcAAAAjN0Y3RjdGcSZYCAAAAHplcm9tZWFucSeIdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBEAAAByZXBsYWNlX2lmX2V4aXN0c3EBiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEC
Y3NpcApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRlQXJyYXlx
BUMuAdnQywABAAD///uEAAABr////PsAAAJH///7jAAAAc7///zzAAACPwAAAAAAAHEGhXEHh3EI
UnEJWA4AAABzZXRfYnJlYWtwb2ludHEKiXUu
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
            "node2",
            "data",
            "node5",
            "data1"
        ],
        [
            "node5",
            "outdata",
            "node4",
            "data"
        ],
        [
            "node5",
            "outdata",
            "node3",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "Fz",
                        "F7",
                        "F8",
                        "FC1",
                        "FC2",
                        "Cz",
                        "C3",
                        "C4",
                        "T7",
                        "T8",
                        "CPz",
                        "CP1",
                        "CP2",
                        "CP5",
                        "CP6",
                        "M1",
                        "M2",
                        "Pz",
                        "P3",
                        "P4",
                        "O1",
                        "O2"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='ErrP-Markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 250.0
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='EEG_data'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "784726fd-a4df-4153-abf0-f8d25f448de5"
        },
        "node2": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "42163767-848e-45ea-a981-ce63da1a1a97"
        },
        "node3": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": true,
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
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "test2.xdf"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/cybathlon/Desktop/Arousal_group"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "906d73ca-8dcb-4849-960b-1f182d1c515d"
        },
        "node4": {
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
            "uuid": "29f1cde6-905a-4aef-970d-aff91649b63a"
        },
        "node5": {
            "class": "MergeStreams",
            "module": "neuropype.nodes.formatting.MergeStreams",
            "params": {
                "replace_if_exists": {
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
            "uuid": "4e8fe1db-7876-454a-9eac-24533b6b1d99"
        }
    },
    "version": 1.1
}</patch>
</scheme>
