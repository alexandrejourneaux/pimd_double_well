import constants as cst

def write_out(suffix, position, speed, pot_energy, kin_energy, energy, mean_pot_energy, mean_kin_energy):
    #Writes results in files
    f = open('positions'+suffix.strip()+'.dat','a')
    for i in range(len(position)):
        for j in range(len(position[0][:])):
            f.write(str(position[i][j])+" ")
        f.write("\n")
    f.close()
        
    f = open('velocities'+suffix.strip()+'.dat','a')
    for i in range(len(speed)):
        for j in range(len(speed[0][:])):
            f.write(str(speed[i][j])+" ")
        f.write("\n")
    f.close()
        
    f = open('pot_ener'+suffix.strip()+'.dat','a')
    for i in range(len(pot_energy)):
        f.write(str(pot_energy[i])+"\n")
    f.close()
    
    f = open('kin_ener'+suffix.strip()+'.dat','a')
    for i in range(len(kin_energy)):
        f.write(str(kin_energy[i])+"\n")
    f.close()
    
    f = open('tot_ener'+suffix.strip()+'.dat','a')
    for i in range(len(energy)):
        f.write(str(energy[i])+"\n")
    f.close()
    
    f = open('av_pot_ener'+suffix.strip()+'.dat','a')
    for i in range(len(mean_pot_energy)):
        f.write(str(mean_pot_energy[i])+"\n")
    f.close()
    
    f = open('av_kin_ener'+suffix.strip()+'.dat','a')
    for i in range(len(mean_kin_energy)):
        f.write(str(mean_kin_energy[i])+" "+str(2.0*mean_kin_energy[i]/cst.kb)+"\n")
    f.close()
    
    f = open('av_tot_ener'+suffix.strip()+'.dat','a')
    for i in range(len(mean_kin_energy)):
        f.write(str(mean_pot_energy[i]+mean_kin_energy[i])+"\n")
    f.close()
