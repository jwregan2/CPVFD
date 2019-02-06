---
title: "Experiment 4: Interior Attack"
layout: experiment
video:
experiment: experiment-4
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "06:17"
    name: Breaker 2 Trip
    icon: circle
  -
    time: "07:04"
    name: Breaker 3 Trip
    icon: circle
  -
    time: "08:01"
    name: Breaker 1 Trip
    icon: circle
  -
    time: "9:39"
    name: Breaker 4 Trip
    icon: circle
  -
    time: "11:02"
    name: Suppression
    icon: circle
  -
    time: "15:47"
    name: Open All Windows
    icon: circle
floors:
  -
    floor_plan: Wapek_First_Floor.png
    sensors:
      temperature:
        -
          coords: "20%, 80%"
          plot: Office_Temperature.pdf
        -
          coords: "70%, 80%"
          plot: Front_Entryroom_Temperature.pdf
        -
          coords: "82%, 25%"
          plot: Rear_Entryroom_Temperature.pdf
  -
    floor_plan: Wapek_Second_Floor.png
    sensors:
      pressure:
        -
          coords: "35.5%, 92%"
          plot: Bedroom_1_Pressure.pdf
        -
          coords: "42%, 85.5%"
          plot: Front_Stair_Landing_Pressure.pdf
        -
          coords: "62%, 92%"
          plot: Bedroom_2_Pressure.pdf
        -
          coords: "72.5%, 24.5%"
          plot: Bedroom_3_Pressure.pdf
        -
          coords: "67%, 21%"
          plot: Rear_Stair_Landing_Pressure.pdf
      temperature:
        -
          coords: "20%, 64%"
          plot: Bedroom_1_Temperature.pdf
        -
          coords: "87.50%, 75%"
          plot: Bedroom_2_Temperature.pdf
        -
          coords: "48%, 80%"
          plot: Front_Stair_Landing_Temperature.pdf
      gas:
        -
          coords: "48%, 82.5%"
          plot: Front_Landing_Victim_Gas_3ft.pdf
        -
          coords: "20%, 66.5%"
          plot: Bedroom_1_Victim_Gas.pdf
      heat_flux:
        -
          coords: "50.5%, 81.5%"
          plot: Front_Landing_Victim_Heat_Flux.pdf
        -
          coords: "22.5%, 65.5%"
          plot: Bedroom_1_Victim_Heat_Flux.pdf
training:
  -
    name: Training Link
    url: "https://www.google.com"
---

Experiment 4 was intended to evaluate the impact of additional horizontal ventilation after an interior attack on a second floor bedroom fire (bedroom 2). The fire was  ignited in the upholstered chair next to the bed and permitted to grow until it reached flashover and fire was venting from both open windows in the room. Suppression was conducted via an interior attack up the stairs. Ventilation occurred after the fire was considered under control.
