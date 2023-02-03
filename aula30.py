velocidade = 60
local_carro = 90

RADAR_1 = 60
LOCAL_1 =  100
RADAR_RANGE = 1

#velocidade > RADAR_1

vel_no_radar1 = velocidade > RADAR_1

if vel_no_radar1:
    print('Sua velocidade esta acima do Radar 1.')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)\
    and vel_no_radar1:
    print('Carro multado no radar 1')