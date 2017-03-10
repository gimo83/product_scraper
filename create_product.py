#!./venv/bin/python 
from app import Product

p1 = Product()
p1['name'] = 'skill screw driver with 35 accessories, F 015 243 6AC'
p1['brand'] = 'Skill'
p1['description'] = "Automatic spindle lock to manually tighten or loosen screws and bolts Screwdriving in narrow places because of compact design with softgrip Easy-to-operate forward/reverse trigger Nickel Metal Hydride batteries have reduced 'memory' effect and are more environment friendly Voltage: 3,6 ... "
p1['barcode'] = '2724309486751'
p1.save()

p2 = Product()
p2['name'] = 'Black & Decker - Screwdriver Set - A7073'
p2['brand'] = 'Black & Decker'
p2['description'] = 'controls variable speed and direction saves time and effort Simply grip the trigger to activate and twist right for forward and twist left for reverse works on Battery'
p2['barcode'] = '5035048010396'
p2.save()
