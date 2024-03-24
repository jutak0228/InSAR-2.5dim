# InSAR2.5dim

input
- 北行軌道の変動量図(⊿a)：delta_A
- 北行軌道の局所入射角(θa)：theta_A
- 北行軌道の方位角(φa)：phi_A
- 南行軌道の変動量図(⊿d)：delta_D
- 南行軌道の局所入射角(θd)：theta_D
- 南行軌道の方位角(φd)：phi_D

output 
- 東西方向の変動量図(⊿x)：delta_X
- 鉛直方向の変動量図(⊿z)：delta_Z

■2.5次元解析式
- ⊿x = (⊿a*cosθd - ⊿d*cosθa)/(sinθa*cosφa - sinθd*cosφd)
- ⊿y = 0
- ⊿z = (⊿a*sinθd*cosφd - ⊿d*sinθa*cosφa)/(cosθa*sinθd*cosφd - cosθd*sinθa*cosφa)

■ラスタ演算式（例）
deltaX = ("2.5dim\pair1_north\delta_A.tif"*Cos("2.5dim\pair2_south\delta_thetaD.tif") - "2.5dim\pair2_south\delta_D.tif"*Cos("2.5dim\pair1_north\delta_thetaA.tif")) /(Cos("2.5dim\pair2_south\delta_thetaD.tif")*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif") -Cos("2.5dim\pair1_north\delta_thetaA.tif")*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif"))

deltaZ = ("2.5dim\pair1_north\delta_A.tif"*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif") - 2.5dim\pair2_south\delta_D.tif"*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif")) / (Cos("2.5dim\pair1_north\delta_thetaA.tif")*Sin("2.5dim\pair2_south\delta_thetaD.tif")*Cos("2.5dim\pair2_south\delta_phyD.tif") -Cos("2.5dim\pair2_south\delta_thetaD.tif")*Sin("2.5dim\pair1_north\delta_thetaA.tif")*Cos("2.5dim\pair1_north\delta_phyA.tif"))

■python program
- delta_X = ( delta_A*cos(theta_D) - delta_D*cos(theta_A) ) / ( sin(theta_A)*cos(phi_A) - sin(theta_D)*cos(phi_D) )
- delta_Z = ( delta_A*sin(theta_D)*cos(phi_D) - delta_D*sin(theta_A)*cos(phi_A) ) / ( cos(theta_A)*sin(theta_D)*cos(phi_D) - cos(theta_D)*sin(theta_A)*cos(phi_A) )


