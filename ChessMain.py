import os
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #8x8 board
SQ_SIZE = HEIGHT / DIMENSION
MAX_FPS = 15
IMAGES = {}

#init... global images

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


#handle usr input and update graphics

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #flag variable for when a move is made

    loadImages()
    running = True
    sqSelected =() #keeps track of last clicks
    playerClicks =[] #keep track of clicks (two tuples: [(6,4), (4,4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse handlers
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = int(location[0]//SQ_SIZE)
                row = int(location[1]//SQ_SIZE)
                if sqSelected == (row, col): #checks if same square is selected for the move
                    sqSelected=() # deselects
                    playerClicks=[] # deselects
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #appends sqselected one after the other
                if len(playerClicks) == 2:
                    move = ChessEngine.move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())

                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True

                    sqSelected = () #reset user clicks
                    playerClicks = []
                
            #key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True
        
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)        
        p.display.update()
        #p.display.flip()
        clock.tick(MAX_FPS)

def drawGameState(screen, gs):
    drawBoard(screen) #draws squares
    drawPieces(screen, gs.board) #draws pieces

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range (DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()