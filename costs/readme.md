# Tapuino costs

This file gives an indication of the costs for making a Tapuino.


## Components

- [Arduino Nano](https://www.aliexpress.com/item/4000310677263.html)
  with micro USB (maybe I should have gotten USB C). 1 for €2.94.

- [Edge connector](https://www.aliexpress.com/item/33015746310.html);
  3 for €1.96.

- [16x2 LCD with I2C adapter](https://www.aliexpress.com/item/1005006964073869.html).
  I took the blue one. 1 for €2.62.

- [SD card reader module](https://www.aliexpress.com/item/1005006457603056.html)
  with 3v3 LDO and level shifters. 1 for €1.08.

- [BC547 transistor](https://www.aliexpress.com/item/1005007339082012.html);
  100 for €1.33.

- [LEDs in blue, green, red](https://www.aliexpress.com/item/1005005708510866.html);
  100 for €1.83.
  
- [Passive Buzzer](https://www.aliexpress.com/item/1005007548587680.html)
  ("passive" means it is like a speaker driven by AC, "active" means
  it contains an oscillator driven at DC and it makes one fixed beep tone).
  10 pieces for €1.76.

- [Clicky blue Cherry MX switches](https://www.aliexpress.com/item/1005007052759423.html)
  30 for €3.63. I hope they are 1 unit wide (0.75 inch or 19.05mm).

- [Key caps](https://www.aliexpress.com/item/1005006477890497.html)
  for the Cherry MX switches. 30 pieces for €10.94.

- [Mute button](https://www.aliexpress.com/item/32699676258.html).
  I used the "self locking" (blue) with 2mm pitch.
  It is a double pole, double throw; 40 switches for €2.49.

- [Resistors](https://www.aliexpress.com/item/1005008240285872.html);
  1280 for €7.09.

- [Opto coupler](https://www.aliexpress.com/item/1005006281381268.html);
  20 for €1.09.

- [capacitors](https://www.aliexpress.com/item/1005007426523574.html);
  120 for €2.66.


## Cost

The table below lists the cost.
Be aware that this table is overly positive; it does not include shipping
for the bulk goods and it assumes the overshoot parts are useful for another project.


| Name                  | Designator                  | Quantity  |  Price  |
|:----------------------|:----------------------------|:---------:|--------:|
| Arduino nano          | U1                          | 1         | €  2.94 |
| Edge connector to C64 | J1C64                       | 1         | €  0.65 |
| LCD module            | J2LCD                       | 1         | €  2.62 |
| Micro SD Card-module  | J3SD                        | 1         | €  1.08 |
| BC547B                | Q1,Q2                       | 2  [0]    | €  0.03 |
| LED 3mm               | L1MOT, L2REC, L3POW         | 3  [0]    | €  0.05 |
| Passive buzzer        | B1R,B2W                     | 2  [0]    | €  0.35 |
| Cherry MX keys        | SW0NXT,SW1PRV,SW2ABT,SW3SEL | 4         | €  0.48 |
| Key caps              | SW0NXT,SW1PRV,SW2ABT,SW3SEL | 4  [0]    | €  1.46 |
| Switch DPDT           | SW4MUT                      | 1  [0]    | €  0.06 |
| Resistor 330Ω         | R5,R6,R7,R8                 | 4  [1]    | €  0.02 |
| Opto coupler PC817C   | U2                          | 1         | €  0.05 |
| Resistor 1kΩ          | R2,R1                       | 2  [0]    | €  0.01 |
| Resistor 220Ω         | R3,R4                       | 2  [0]    | €  0.01 |
| 10u                   | C1                          | 1         | €  0.02 |
|                       |                             |           |         |
| PCB                   | (5 piecs with shipping)     | 1         | €  2.13 |
| Casing 3 parts        | (with shipping)             | 1         | € 18.78 |
|                       |                             |           |         |
| SD card               |                             | 1         | €  2.28 |
|                       |                             |           |         |
|                       |                             |           | € 33.02 |

The casing is by far the most expensive part, which you don't need. 
If you want to reduce more, you could consider removing all three LEDs, 
the buzzer and its driver circuit. But this is all cents range.
The biggest saving is replacing the cherry switches and caps 
with cheaper switches.
The optional PCB cost reductions are tagged with [ ] in the cost overview.


(end)
