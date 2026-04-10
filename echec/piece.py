def position_deplacement(echequier):
    pos_x = 0
    pos_y = 0

    for x in range(8):
        for y in range(8):
            if echequier[x][y] == "T_B":
                pos_x = x
                pos_y = y


    ##Droite 
    for i in range(pos_y+1,8):
        if echequier[pos_x][i] != ' ':
            if echequier[pos_x][i].find("_N") != -1:
                echequier[pos_x][i] = "O"
                break
            else:
                break
        else:
            echequier[pos_x][i] = "L"
    
    ##Gauche 
    for i in range(pos_y-1,-1,-1):
        if echequier[pos_x][i] != ' ':
            if echequier[pos_x][i].find("_N") != -1:
                echequier[pos_x][i] = "O"
                break
            else:
                break
        else:
            echequier[pos_x][i] = "L"

    ##haut
    for i in range(pos_x-1,-1,-1):
        if echequier[i][pos_y] != ' ':
            if echequier[i][pos_y].find("_N") != -1:
                echequier[i][pos_y] = "O"
                break
            else:
                break
        else:
            echequier[i][pos_y] = "L"
    
    ##bas
    for i in range(pos_x+1,8):
        if echequier[i][pos_y] != ' ':
            if echequier[i][pos_y].find("_N") != -1:
                echequier[i][pos_y] = "O"
                break
            else:
                break
        else:
            echequier[i][pos_y] = "L"