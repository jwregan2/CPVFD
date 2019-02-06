---
title: "Experiment 7: Interior Attack with Vertical Ventilation Above Fire"
layout: experiment
video:
experiment: experiment-7
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "04:58"
    name: Breaker 2 and 3 Trip
    icon: circle
  -
    time: "08:13"
    name: Breaker 4 Off
    icon: circle
  -
    time: "08:22"
    name: Suppression
    icon: circle
  -
    time: "10:20"
    name: Kitchen Door Open
    icon: circle
  -
    time: "11:45"
    name: Master Bedroom Window Open
    icon: circle
floors:
  -
    floor_plan: Water_Street_Second_Floor_Plain.png
    sensors:
      pressure:
        -
          coords: "30%, 4%"
          plot: Bedroom_2_Pressure.pdf
        -
          coords: "50%, 12%"
          plot: Bedroom_2_Hallway_Pressure.pdf
        -
          coords: "59%, 42%"
          plot: Bedroom_1_Hallway_Pressure.pdf
        -
          coords: "66%, 54%"
          plot: Bedroom_1_Pressure.pdf
      temperature:
        -
          coords: "22%, 43%"
          plot: Bedroom_2_Temperature.pdf
        -
          coords: "72%, 75%"
          plot: Bedroom_1_Temperature.pdf
        -
          coords: "55.5%, 52%"
          plot: Bedroom_1_Hallway_Temperature.pdf
        -
          coords: "45%, 49%"
          plot: Landing_Temperature.pdf
        -
          coords: "45%, 56%"
          plot: Front_Door_Temperature.pdf
      gas:
        -
          coords: "72%, 72%"
          plot: Bedroom_1_Victim_Gas.pdf
        -
          coords: "55.5%, 49%"
          plot: Bedroom_1_Doorway_Victim_Gas_3ft.pdf
      heat_flux:
        -
          coords: "74.5%, 73.5%"
          plot: Bedroom_1_Victim_Heat_Flux.pdf
        -
          coords: "58%, 50.5%"
          plot: Bedroom_1_Doorway_Victim_Heat_Flux.pdf
training:
  -
    name: Training Link
    url: "https://www.google.com"
---

Experiment 7 was intended to evaluate the effectiveness of vertical ventilation above the fire compartment just prior to the suppression crew ascending the stairs on a second floor bedroom fire. The fire was ignited in the upholstered chair next to the bed and permitted to grow until it reached flashover and fire was venting from both open windows in the room. Suppression was conducted via an interior attack up the stairs. Ventilation was coordinated with entry to the structure.
