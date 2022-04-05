DIMENSAO = 9

board = [
    [0,0,1,0,0,0,0,0,0],
    [0,0,2,0,3,0,0,0,4],
    [0,0,0,5,0,0,6,0,7],
    [5,0,0,1,4,0,0,0,0],
    [0,7,0,0,0,0,0,2,0],
    [0,0,0,0,7,8,0,0,9],
    [8,0,7,0,0,9,0,0,0],
    [4,0,0,0,6,0,3,0,0],
    [0,0,0,0,0,0,5,0,0]
]

def checar_numero_coluna(board, numero, coluna):
    for i in range(0,DIMENSAO,1):
        if board[i][coluna] == numero:
            return True
    return False

def checar_numero_linha(board, numero, linha):
    for i in range(0, DIMENSAO, 1):
        if board[linha][i] == numero:
            return True
    return False

def checar_numero_3x3(board, numero, linha, coluna):
    linha_caixa = linha - int(linha % 3)
    coluna_caixa = coluna - int(coluna % 3)
    for i in range(linha_caixa, linha_caixa+3, 1):
        for j in range(coluna_caixa, coluna_caixa+3, 1):
            if board[i][j] == numero:
                return True
    return False

def numero_valido(board, numero, linha, coluna):
    if ((not checar_numero_linha(board, numero, linha)) and (not checar_numero_coluna(board, numero, coluna)) and (not checar_numero_3x3(board, numero, linha, coluna))):
        return True
    else:
        return False

def resolver_sudoku(board):

    for i in range(0, DIMENSAO, 1):
        for j in range(0, DIMENSAO, 1):
            if board[i][j] == 0:
                for k in range(1, 10, 1):
                    if numero_valido(board, k, i, j):
                        board[i][j] = k
                        if resolver_sudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True

def printar_board(board):
    for linha in range(0, DIMENSAO, 1):
        if linha % 3 == 0:
            print("-----------")
            for coluna in range(0, DIMENSAO, 1):
                if coluna % 3 == 0:
                    print("|")
                print(board[linha][coluna])

if resolver_sudoku(board):
    print("Resolvido")
else:
    print("Nao resolvido")

printar_board(board)