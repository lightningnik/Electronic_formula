I = ['H', 'He']
II = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
III = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
IV = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
V = ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']
VI = ['Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
VII = ['Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
print('', I,'\n',II,'\n',III,'\n',IV,'\n',V,'\n',VI,'\n',VII)
el = input("Input chemistry element:  ")
if el in I:
    print('Long electronic formula ' + str(el) + ': 1s^' + str(I.index(el) + 1))
elif el in II: 
    if II.index(el)+1 < 3: 
        print('Short electronic formula ' + str(el) + ': [' + str(I[len(I)-1]) + '] 2s^' + str(II.index(el) + 1))
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^' + str(II.index(el) + 1))
    else: 
        print('Short electronic formula ' + str(el) + ': [' + str(I[len(I)-1]) + '] 2s^2 2p^' + str(II.index(el) + 1 - 2))
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^' + str(II.index(el) + 1 - 2))
elif el in III: 
    if III.index(el)+1 < 3:
        print('Short electronic formula ' + str(el) + ': [' + str(II[len(II)-1]) + '] 3s^' + str(III.index(el) + 1))
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^' + str(III.index(el) + 1))
    elif   12 > III. index(el)+1 >= 3:
        print('Short electronic formula ' + str(el) + ': [' + str(II[len(II)-1]) + '] 3s^2 3p^' + str(III.index(el) + 1 - 2))
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^' + str(III.index(el) + 1 - 2))
elif el in IV: 
    if IV.index(el)+1 < 3:
        print('Short electronic formula ' + str(el) + ': [' + str(III[len(III)-1]) + '] 3s^' + str(IV.index(el) + 1)) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 4s^' + str(IV.index(el) + 1))
    elif 3 <= IV.index(el)+1 < 13:
        print('Short electronic formula ' + str(el) + ': [' + str(III[len(III)-1]) + '] 3d^' + str(IV.index(el) + 1 - 2) +' 4s^2' ) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^' + str(IV.index(el) + 1 - 2) + ' + 4s^2')
    elif IV.index(el)+1 >= 13:
        print('Short electronic formula ' + str(el) + ': [' + str(III[len(III)-1]) + '] 3d^10 4s^2 4p^' + str(IV.index(el) - 11))
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^' + str(IV.index(el) - 11))
elif el in V: 
    if V.index(el)+1 < 3:
        print('Short electronic formula ' + str(el) + ': [' + str(IV[len(IV)-1]) + '] 5s^' + str(V.index(el) + 1)) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 5s^' + str(V.index(el) + 1))
    elif 3 <= V.index(el)+1 < 13:
        print('Short electronic formula ' + str(el) + ': [' + str(IV[len(IV)-1]) + '] 4d^' + str(V.index(el) + 1 - 2) +' 5s^2' ) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^' + str(V.index(el) + 1 - 2) + ' 5s^2')
    elif V.index(el)+1 >= 13:
        print('Short electronic formula ' + str(el) + ': [' + str(IV[len(IV)-1]) + '] 4d^10 5s^2 5p^' + str(V.index(el) - 11))  
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^' + str(V.index(el) - 11))    
#elif el in VI: 
    
#elif el in VII: 