---
title: "Experiment 5: Interior Attack with PPV"
layout: experiment
video:
experiment: experiment-5
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "06:53"
    name: Breaker Trip
    icon: circle
  -
    time: "20:32"
    name: Kitchen Door Open
    icon: circle
  -
    time: "22:31"
    name: West Living Room Window Open
    icon: circle
  -
    time: "23:02"
    name: East Living Room Window Open
    icon: circle
  -
    time: "23:42"
    name: Bedroom 2 Window Open
    icon: circle
  -
    time: "24:05"
    name: Den Window Open
    icon: circle
  -
    time: "24:41"
    name: Bedroom 3 Window Open
    icon: circle
floors:
  -
    floor_plan: Wapek_First_Floor.png
    sensors:
      temperature:
        -
          coords: "82%, 25%"
          plot: Rear_Entryroom_Temperature.pdf
  -
    floor_plan: Wapek_Second_Floor.png
    sensors:
      pressure:
        -
          coords: "72.5%, 24.5%"
          plot: Bedroom_3_Pressure.pdf
        -
          coords: "67%, 21%"
          plot: Rear_Stair_Landing_Pressure.pdf
      temperature:
        -
          coords: "82%, 24.5%"
          plot: Bedroom_3_Temperature.pdf
        -
          coords: "48%, 40%"
          plot: Bedroom_4_Temperature.pdf
        -
          coords: "65%, 10%"
          plot: Rear_Stair_Landing_Temperature.pdf
      gas:
        -
          coords: "65%, 12.5%"
          plot: Rear_Landing_Victim_Gas_3ft.pdf
        -
          coords: "48%, 42.5%"
          plot: Bedroom_4_Victim_Gas.pdf
      heat_flux:
        -
          coords: "67.5%, 11.5%"
          plot: Rear_Landing_Victim_Heat_Flux.pdf
        -
          coords: "50.5%, 41.5%"
          plot: Bedroom_2_Victim_Heat_Flux.pdf
training:
  -
    name: Training Link
    url: "https://www.google.com"
---

Experiment 5 was intended to evaluate the impact of positive pressure ventilation after an interior attack on a second floor bedroom fire (bedroom 3). The fire was ignited in the upholstered chair next to the bed and permitted to grow until it reached flashover and fire was venting from both open windows in the room. Suppression was conducted via an interior attack up the stairs.
