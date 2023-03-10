I = ['H', 'He']
II = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
III = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
IV = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
V = ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe']
VI = ['Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
VII = ['Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
print('', I,'\n',II,'\n',III,'\n',IV,'\n',V,'\n',VI,'\n',VII)
el = input("Input chemistry element:  ")
while el not in I and el not in II and el not in III and el not in IV and el not in V and el not in VI and el not in VII:
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
elif el in VI: 
    if VI.index(el)+1 < 3:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 6s^' + str(VI.index(el) + 1)) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6 6s^' + str(VI.index(el) + 1))
    elif VI.index(el) + 1 == 3:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 5d^1 6s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6 5d^1 6s^2')
    elif 4 <= VI.index(el) + 1 <= 9:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^' + str(VI.index(el) - 1) + ' 6s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^'+ str(VI.index(el) - 1) +' 5s^2 5p^6 6s^2')
    elif VI.index(el) + 1 == 10:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^7 5d^1 6s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^7 5d^1 5s^2 5p^6 6s^2')
    elif 11 <= VI.index(el) + 1 <=16:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^' + str(VI.index(el) - 1) + ' 6s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^'+ str(VI.index(el) - 1) +' 5s^2 5p^6 6s^2')
    elif 17 <= VI.index(el) + 1 <=23:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^' + str(VI.index(el) - 1) + ' 6s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^' + str(VI.index(el) - 15) + ' 6s^2')
    elif VI.index(el) + 1 == 24:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^14 5d^9 6s^1') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5d^9 5s^2 5p^6 6s^1')
    elif 25 <= VI.index(el) + 1 <=26:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^14 5d^10 6s^' + str(VI.index(el) - 23) + '') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^' + str(VI.index(el) - 23) + '')
    elif 27 <= VI.index(el) + 1 <=32:
        print('Short electronic formula ' + str(el) + ': [' + str(V[len(V)-1]) + '] 4f^14 5d^10 6s^2 6p^' + str(VI.index(el) - 25) + '') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^' + str(VI.index(el) - 25) + '')
elif el in VII: 
    if VII.index(el) + 1 < 3:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 4f^14 5d^10 6s^2 6p^6 7s^' + str(VII.index(el) + 1)) 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^6 7s^' + str(VII.index(el) + 1))
    elif VII.index(el) + 1 == 3:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + ']6d^1 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^6 6d^1 7s^2')
    elif VII.index(el) + 1 == 4:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 6d^2 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^6 6d^1 7s^2')
    elif 5 <= VII.index(el) + 1 <= 8 or 10 <= VII.index(el) + 1 <= 11:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 5f^' + str(VII.index(el) - 2) + ' 6d^1 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 5f^' + str(VII.index(el) - 2) + ' 6s^2 6p^6 6d^1 7s^2')
    elif VII.index(el) + 1 == 9:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 6d^2 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 5f^7 6s^2 6p^6 6d^1 7s^2')
    elif 12 <= VII.index(el) + 1 <= 16:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 5f^' + str(VII.index(el) - 1) + ' 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 5f^' + str(VII.index(el) - 1) + ' 6s^2 6p^6 7s^2')
    elif 17 <= VII.index(el) + 1 <= 20:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 5f^14 6d^' + str(VII.index(el) - 15) + ' 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 5f^14 6s^2 6p^6 6d^10 7s^2 7p^' + str(VII.index(el) - 15) + '')
    elif 19 <= VII.index(el) + 1:
        print('Short electronic formula ' + str(el) + ': [' + str(VI[len(VI)-1]) + '] 5f^14 6d^' + str(VII.index(el) - 15) + ' 7s^2') 
        print('Long electronic formula ' + str(el) + ': 1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 5f^14 6s^2 6p^6 6d^10 7s^2 7p^' + str(VII.index(el) - 25) + '')