from .namespaces import TAG, BRICK


command_definitions = {
    "Command": {
        "tags": [TAG.Command],
        "subclasses": {
            "Cooling_Command": {
                "tags": [TAG.Cool, TAG.Command],
                "subclasses": {
                    "Highest_Zone_Cooling_Command": {},
                },
            },
            "Heating_Command": {
                "tags": [TAG.Heat, TAG.Command],
            },
            "Luminance_Command": {
                "tags": [TAG.Luminance, TAG.Command],
            },
            "Damper_Command": {
                "tags": [TAG.Damper, TAG.Command],
                "subclasses": {
                    "Damper_Position_Command": {
                        "tags": [TAG.Damper, TAG.Position, TAG.Command],
                        "parents": [BRICK.Position_Command],
                    },
                },
            },
            "Position_Command": {
                "tags": [TAG.Position, TAG.Command],
            },
            "Direction_Command": {
                "tags": [TAG.Direction, TAG.Command],
            },
            "Pump_Command": {
                # TODO: position?
                "tags": [TAG.Pump, TAG.Command],
            },
            "Valve_Command": {
                # TODO: position?
                "tags": [TAG.Valve, TAG.Command],
            },
            "Reset_Command": {
                "tags": [TAG.Reset, TAG.Command],
                "subclasses": {
                    "Fault_Reset_Command": {},
                    "Filter_Reset_Command": {},
                    "Speed_Reset_Command": {},
                    "Fan_Speed_Reset_Command": {},
                },
            },
            "Shutdown_Command": {
                "tags": [TAG.Shutdown, TAG.Command],
            },
            "Enable_Command": {
                "tags": [TAG.Enable, TAG.Command],
                "subclasses": {
                    "VFD_Enable_Command": {
                        "tags": [TAG.Enable, TAG.Command, TAG.VFD],
                    },
                    "System_Enable_Command": {
                        "tags": [TAG.Enable, TAG.Command, TAG.System],
                        "subclasses": {
                            "Chilled_Water_System_Enable_Command": {
                                "tags": [TAG.Enable, TAG.Command, TAG.Chilled, TAG.Water, TAG.System],
                            },
                            "Hot_Water_System_Enable_Command": {
                                "tags": [TAG.Enable, TAG.Command, TAG.Hot, TAG.Water, TAG.System],
                                "subclasses": {
                                    "Domestic_Hot_Water_System_Enable_Command": {
                                        "tags": [TAG.Enable, TAG.Command, TAG.Domestic, TAG.Hot, TAG.Water, TAG.System],
                                    },
                                },
                            },
                        },
                    },
                    "Exhaust_Fan_Enable_Command": {
                        "tags": [TAG.Enable, TAG.Command, TAG.Fan, TAG.Exhaust],
                    },
                    "Run_Enable_Command": {
                        "tags": [TAG.Enable, TAG.Command, TAG.Run],
                    },
                },
            },
            "Disable_Command": {
                "tags": [TAG.Disable, TAG.Command],
                "subclasses": {
                    "Exhaust_Fan_Disable_Command": {
                        "tags": [TAG.Disable, TAG.Command, TAG.Fan, TAG.Exhaust],
                    },
                },
            },
            "Lead_Lag_Command": {
                "tags": [TAG.Lead, TAG.Lag, TAG.Command],
            },
            "Load_Shed_Command": {
                "tags": [TAG.Load_Shed, TAG.Command],
                "subclasses": {
                    "Standby_Load_Shed_Command": {
                        "subclasses": {
                            "Zone_Standby_Load_Shed_Command": {},
                        },
                    },
                    "Unoccupied_Load_Shed_Command": {
                        "subclasses": {
                            "Zone_Unoccupied_Load_Shed_Command": {},
                        },
                    },
                },
            },
            "Mode_Command": {
                "tags": [TAG.Mode, TAG.Command],
                "subclasses": {
                    "Automatic_Mode_Command": {},
                    "Maintenance_Mode_Command": {},
                    "Box_Mode_Command": {},
                },
            },
            "Frequency_Command": {
                "tags": [TAG.Fequency, TAG.Command],
            },
            "On_Off_Command": {
                "tags": [TAG.OnOff, TAG.Command],
                "subclasses": {
                    "Steam_On_Off_Command": {},
                    "Start_Stop_Command": {},
                },
            },
            "Override_Command": {
                "tags": [TAG.Override, TAG.Command],
                "subclasses": {
                    "Curtailment_Override_Command": {
                        "tags": [TAG.Curtailment, TAG.Override, TAG.Command],
                    },
                },
            },
        },
    }
}
