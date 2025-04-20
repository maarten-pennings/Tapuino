# Tapuino case

This directory contains the 3D printing files.


## Sleeve

I bought a 2x6 pins [PCB connector](https://www.aliexpress.com/item/33015746310.html).
I designed a sleeve for that, that is supposed to look a bit like the original:

![original](sleeve-orig.jpg)

This is my version.
The [stl](sleeve-square.stl) is in the repo.


![mine front](sleeve-square.jpg) ![mine back](sleeve-square-back.jpg) 



## Tapuino Case

I also made a casing for the Tapuino itself.
I wanted it to look like the original datasette.

This is the result of a couple of evenings with Fusion 360.

![shell](shell.png)

It consists of a [top half](ShellTop.stl) and a [bottom half](ShellBot.stl).
The top half has a black [inlay](Inlay.stl).

I made prototypes with my 3D printer, but then ordered at [JLCPCB](https://jlcpcb.com/DMP).
I did go for low(est) cost in material and shipping: €17.30.

![total cost](totalcost.png)


Unfortunately, I got a mail from JLCPCB:

> Due to the geometry of this workpiece, there is a high risk of deformation.
> Usually, for flat parts, frame parts, enclosures with no strong ribs inside, and large unoccupied areas parts, long parts and the models could shrink to the center and warping to the diagonal lines and edges.
> Could you please confirm if the risks are acceptable for you?

I decided to add some ribs; to the [top half](ShellTop2.stl), the [bottom half](ShellBot2.stl), and even to the [inlay](Inlay2.stl),
and to resubmit my order.

Again, I did got for low(est) cost in material and shipping, but more plastic, €1.50 higher cost:

![total cost v2](totalcost2.png)



## Result


![Tapuino alone](alone.jpg)

![Tapuino side by side with datasette](sidebyside.jpg)

(end)
