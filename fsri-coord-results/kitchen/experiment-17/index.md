---
title: "Experiment 17: Interior Attack with PPV"
layout: experiment
comments: true
video: https://player.vimeo.com/video/291944941
experiment: experiment-17
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "13:01"
    name: Front Door Open
    icon: circle
  -
    time: "13:11"
    name: PPV Fan Turned In
    icon: circle
  -
    time: "13:23"
    name: Attack Crew Entered
    icon: circle
  -
    time: "17:24"
    name: Fire Knocked Down
    icon: circle 
  -
    time: "22:30"
    name: End Experiment
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
      gas:
        -
          coords: "72%, 48%"
          plot: Dining_Room_Victim_Gas.pdf
      heat_flux:
        -
          coords: "75.5%, 49.25%"
          plot: Dining_Room_Victim_Heat_Flux.pdf
      skin_temp:
        -
          coords: "75.5%, 51.5%"
          plot: Dining_Room_Victim.pdf
      moisture:
        -
          coords: "79%, 50.75%"
          plot: Dining_Room_Victim_Moisture.pdf
  -
    floor_plan: North_Walnut_Second_Floor.png
    icon_width: 3%
    sensors:
      temperature:
        -
          coords: "40%, 12%"
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
          plot: Hallway_Victim_Gas.pdf
      heat_flux:
        -
          coords: "72.5%, 20%"
          plot: Hallway_Victim_Heat_Flux.pdf
      skin_temp:
        -
          coords: "72.5%, 22.5%"
          plot: Hallway_Victim.pdf
      moisture:
        -
          coords: "70%, 24%"
          plot: Hallway_Victim_Moisture.pdf 
---

Experiment 17 was intended to evaluate the impact of positive pressure attack on a kitchen fire. The fire was ignited on the counter top with a bag of chips, paper towels and paper cups and was permitted to grow until it reached flashover and fire was venting from both open windows in the kitchen. Suppression was conducted via an interior attack.  

#### Side A

{% img kitchen/experiment-17/A-Side.JPG %}

#### Side B

{% img kitchen/experiment-17/B-Side.JPG %}

#### Side C

{% img kitchen/experiment-17/C-Side.JPG %}

#### Side D

{% img kitchen/experiment-17/D-Side.JPG %}

### Suppression Method #5
Kitchen fire with fire venting from two windows. Suppression was conducted via an interior attack. Ventilation used a positive pressure attack where the fan was started prior to the crew entering.
 - Front door opened on conditions.
 - Door read (5 seconds).
 - Perform positive pressure ventilation.
 - Suppression crew entered, 'Wall Ceiling Wall' method of suppression was made on approach kitchen with a 150 gpm straight stream.
