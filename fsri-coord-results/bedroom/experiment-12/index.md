---
title: "Experiment 12: Transitional Attack with Horizontal Ventilation"
layout: experiment
video:
experiment: experiment-12
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "05:14"
    name: Breaker 3 Trip
    icon: circle
  -
    time: "05:49"
    name: Front Door Self Closed
    icon: circle
  -
    time: "06:09"
    name: Front Door Open and Breaker 2 Trip
    icon: circle
  -
    time: "09:17"
    name: Breaker 1 Open
    icon: circle
  -
    time: "09:32"
    name: Suppression Living Room Window/td>
    icon: circle
  -
    time: "10:31"
    name: Kitchen Doors Open
    icon: circle
  -
    time: "11:52"
    name: Master Bedroom Window Open
    icon: circle
floors:
  -
    floor_plan: North_Walnut_First_Floor.png
    icon_width: 3%
    sensors:
      pressure:
        -
          coords: "50%, 73%"
          plot: Kitchen_Pressure.pdf
        -
          coords: "67%, 63%"
          plot: Dining_Room_Pressure.pdf
      temperature:
        -
          coords: "78%, 20%"
          plot: Stairwell_Temperature.pdf
        -
          coords: "38%, 22%"
          plot: Living_Room_Temperature.pdf
        -
          coords: "24%, 50%"
          plot: Family_Room_Temperature.pdf
        -
          coords: "72%, 50%"
          plot: Dining_Room_Temperature.pdf
        -
          coords: "28%, 79%"
          plot: Kitchen_Temperature.pdf
  -
    floor_plan: North_Walnut_Second_Floor.png
    icon_width: 3%
    sensors:
      pressure:
        -
          coords: "60%, 4.5%"
          plot: Bedroom_1_Pressure.pdf
        -
          coords: "36%, 60%"
          plot: Bedroom_2_Pressure.pdf
        -
          coords: "68%, 61%"
          plot: Bedroom_3_Pressure.pdf
        -
          coords: "72.5%, 17.5%"
          plot: Hallway_Pressure.pdf
      temperature:
        -
          coords: "40%, 11.5%"
          plot: Bedroom_1_Temperature.pdf
        -
          coords: "18%, 48%"
          plot: Bedroom_2_Temperature.pdf
        -
          coords: "78%, 48%"
          plot: Bedroom_3_Temperature.pdf
        -
          coords: "44%, 68%"
          plot: Hallway_Temperature.pdf
        -
          coords: "69%, 19%"
          plot: Hallway_Victim_Temperature.pdf
      gas:
        -
          coords: "69%, 21.5%"
          plot: Hallway_Victim_Gas_3ft.pdf
        -
          coords: "40%, 14%"
          plot: Bedroom_1_Victim_Gas.pdf
      heat_flux:
        -
          coords: "72.5%, 20%"
          plot: Hallway_Victim_Heat_Flux.pdf
        -
          coords: "43.5%, 13%"
          plot: Bedroom_1_Victim_Heat_Flux.pdf
training:
  -
    name: Training Link
    url: "https://www.google.com"
---

Experiment 12 was intended to evaluate the impact of additional horizontal ventilation after a transitional attack on a second floor bedroom fire (bedroom 3). The fire was ignited in the upholstered chair next to the bed and permitted to grow until it reached flashover and fire was venting from both open windows in the room. Suppression was conducted via a transitional attack. Ventilation occurred at transitional attack.
