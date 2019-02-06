---
title: "Experiment 19: Transitional Attack with Serious Ventilation"
layout: experiment
comments: true
video: https://player.vimeo.com/video/291983549
experiment: experiment-19
timeline:
  -
    time: "00:00"
    name: Ignition
    icon: icon-flame
  -
    time: "11:00"
    name: Suppression Kitchen Window
    icon: circle
  -
    time: "11:15"
    name: Front Door Open
    icon: circle
  -
    time: "11:22"
    name: Ventilation - All 1st Floor Windows
    icon: circle
  -
    time: "12:17"
    name: Attack Crew Entered
    icon: circle
  -
    time: "15:04"
    name: Fire Knocked Down
    icon: circle
  -
    time: "20:10"
    name: End Experiment
    icon: circle
floors:
  -
    floor_plan: Broadway_Street_First_Floor.png
    icon_width: 4%
    sensors:
      pressure:
        -
          coords: "30%, 54%"
          plot: Target_Room_1_Pressure.pdf
        -
          coords: "40%, 63%"
          plot: Kitchen_Pressure.pdf
      temperature:
        -
          coords: "48%, 20%"
          plot: Entryroom_Temperature.pdf
        -
          coords: "25%, 38%"
          plot: Target_Room_1_Temperature.pdf
        -
          coords: "75%, 38%"
          plot: Target_Room_2_Temperature.pdf
        -
          coords: "75%, 71%"
          plot: Kitchen_Temperature.pdf
      gas:
        -
          coords: "8.3%, 29%"
          plot: Target_Room_1_Victim_Gas.pdf
      heat_flux:
        -
          coords: "8.3%, 31.5%"
          plot: Target_Room_1_Victim_Heat_Flux.pdf
      skin_temp:
        -
          coords: "8.3%, 34%"
          plot: Target_Room_Victim.pdf
      moisture:
        -
          coords: "13.5%, 31.5%"
          plot: Target_Room_1_Victim_Moisture.pdf
  -
    floor_plan: Broadway_Street_Second_Floor.png
    icon_width: 5%
    sensors:
      temperature:
        -
          coords: "40%, 20%"
          plot: Front_Bedroom_Temperature.pdf
        -
          coords: "38%, 47%"
          plot: Rear_Bedroom_Temperature.pdf
      gas:
        -
          coords: "39%, 50%"
          plot: Rear_Bedroom_Victim_Gas.pdf
      heat_flux:
        -
          coords: "44%, 48%"
          plot: Rear_Bedroom_Victim_Heat_Flux.pdf
      skin_temp:
        -
          coords: "44%, 51%"
          plot: Rear_Bedroom_Victim.pdf
      moisture:
        -
          coords: "50%, 50%"
          plot: Rear_Bedroom_Victim_Moisture.pdf
---
Experiment 19 was intended to evaluate the impact of additional horizontal ventilation after a transitional attack on a kitchen fire. The fire was ignited on the counter top with a bag of chips, paper towels and paper cups and was permitted to grow until it reached flashover and fire was venting from both open windows in the kitchen. Suppression was conducted via a transitional attack.

#### Side A

{% img kitchen/experiment-19/A-Side.JPG %}

#### Side B

{% img kitchen/experiment-19/B-Side.JPG %}

#### Side C

{% img kitchen/experiment-19/C-Side.JPG %}

#### Side D

{% img kitchen/experiment-19/D-Side.JPG %}

### Suppression Method #6
Kitchen Fire with fire venting from two windows. Suppression was conducted via a transitional attack. 
 - Transitional hit on conditions through kitchen window.
 - Front door open.
 - Horizontal ventilation applied.
 - Suppression crew advanced directly to compartment.
 - Once at kitchen, steep angle off ceiling, followed by entry for surface suppression. 
 - Check for exterior extension.
