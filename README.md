# InSAR2.5dim

input
- Deformation in Ascending (⊿a)：delta_A
- Local incidence angle in Ascending (θa)：theta_A
- Azimuth in Ascending (φa)：phi_A
- Deformation in Descending (⊿d)：delta_D
- Local incidence angle in Descending (θd)：theta_D
- Azimuth in Decending (φd)：phi_D

output 
- Deformation in east-west directions (⊿x)：delta_X
- Deformation in vertical directions (⊿z)：delta_Z

## 2.5 dimension equation
- ⊿x = (⊿a*cosθd - ⊿d*cosθa)/(sinθa*cosφa - sinθd*cosφd)
- ⊿y = 0
- ⊿z = (⊿a*sinθd*cosφd - ⊿d*sinθa*cosφa)/(cosθa*sinθd*cosφd - cosθd*sinθa*cosφa)

## Raster calculation (example)
deltaX = ("2.5dim\pair1_north\delta_A.tif"*Cos("2.5dim\pair2_south\delta_thetaD.tif") - "2.5dim\pair2_south\delta_D.tif"*Cos("2.5dim\pair1_north\delta_thetaA.tif")) /(Cos("2.5dim\pair2_south\delta_thetaD.tif")*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif") -Cos("2.5dim\pair1_north\delta_thetaA.tif")*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif"))

deltaZ = ("2.5dim\pair1_north\delta_A.tif"*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif") - 2.5dim\pair2_south\delta_D.tif"*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif")) / (Cos("2.5dim\pair1_north\delta_thetaA.tif")*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif") -Cos("2.5dim\pair2_south\delta_thetaD.tif")*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif"))

## Python program
- delta_X = ( delta_A*cos(theta_D) - delta_D*cos(theta_A) ) / ( sin(theta_A)*cos(phi_A) - sin(theta_D)*cos(phi_D) )
- delta_Z = ( delta_A*sin(theta_D)*cos(phi_D) - delta_D*sin(theta_A)*cos(phi_A) ) / ( cos(theta_A)*sin(theta_D)*cos(phi_D) - cos(theta_D)*sin(theta_A)*cos(phi_A) )


