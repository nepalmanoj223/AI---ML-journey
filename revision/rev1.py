# # dit ={
# #     "name":"Manoj",
# #     "age" : 12,
# #     "occupation" : "teacher"
# #     }
# # print(dit["name"])
# # print(dit["age"])
# # print(dit["occupation"])


# import pygame
# import chess
# import sys

# # --- Config ---
# TILE = 80
# BOARD_SIZE = TILE * 8
# MARGIN = 0
# WIDTH, HEIGHT = BOARD_SIZE, BOARD_SIZE
# FPS = 60

# # Colors
# LIGHT = (240, 217, 181)
# DARK  = (181, 136, 99)
# HIGHLIGHT = (246, 246, 105)
# MOVE_HINT = (120, 180, 120)
# TEXT = (20, 20, 20)
# BG = (245, 245, 245)


# UNICODE = {
#     chess.PAWN:   ("♙","♟"),
#     chess.KNIGHT: ("♘","♞"),
#     chess.BISHOP: ("♗","♝"),
#     chess.ROOK:   ("♖","♜"),
#     chess.QUEEN:  ("♕","♛"),
#     chess.KING:   ("♔","♚"),
# }

# def piece_to_unicode(piece):
#     if piece is None: return ""
#     chars = UNICODE[piece.piece_type]
#     return chars[0] if piece.color == chess.WHITE else chars[1]

# def square_to_coords(square):
#     # chess A1 is bottom-left (from white’s view) => file (x), rank (y)
#     file = chess.square_file(square)  # 0..7 (a..h)
#     rank = chess.square_rank(square)  # 0..7 (1..8)
#     # Pygame y=0 is top; we want rank 7 at y=0
#     x = file * TILE
#     y = (7 - rank) * TILE
#     return x, y

# def coords_to_square(x, y):
#     file = x // TILE
#     rank_from_top = y // TILE
#     rank = 7 - rank_from_top
#     if 0 <= file <= 7 and 0 <= rank <= 7:
#         return chess.square(file, rank)
#     return None

# def legal_destinations(board, from_sq):
#     moves = []
#     for mv in board.legal_moves:
#         if mv.from_square == from_sq:
#             moves.append(mv.to_square)
#     return moves

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Python Chess (pygame + python-chess)")
#     clock = pygame.time.Clock()
#     font = pygame.font.SysFont(None, 56)
#     small = pygame.font.SysFont(None, 28)

#     board = chess.Board()
#     selected_sq = None
#     legal_to = []

#     def draw():
#         screen.fill(BG)
#         # draw board
#         for r in range(8):
#             for f in range(8):
#                 x = f * TILE
#                 y = r * TILE
#                 color = LIGHT if (r + f) % 2 == 0 else DARK
#                 pygame.draw.rect(screen, color, (x, y, TILE, TILE))

#         # highlight selected square
#         if selected_sq is not None:
#             sx, sy = square_to_coords(selected_sq)
#             pygame.draw.rect(screen, HIGHLIGHT, (sx, sy, TILE, TILE), 6)

#         # hint possible moves
#         for sq in legal_to:
#             x, y = square_to_coords(sq)
#             pygame.draw.circle(screen, MOVE_HINT, (x + TILE // 2, y + TILE // 2), 10)

#         # draw pieces
#         for sq in chess.SQUARES:
#             pc = board.piece_at(sq)
#             if pc:
#                 x, y = square_to_coords(sq)
#                 txt = piece_to_unicode(pc)
#                 img = font.render(txt, True, TEXT)
#                 rect = img.get_rect(center=(x + TILE // 2, y + TILE // 2))
#                 screen.blit(img, rect)

#         # status text
#         status = ""
#         if board.is_checkmate():
#             status = "Checkmate! " + ("Black wins" if board.turn == chess.WHITE else "White wins")
#         elif board.is_stalemate():
#             status = "Stalemate"
#         elif board.is_insufficient_material():
#             status = "Draw (insufficient material)"
#         elif board.is_check():
#             status = "Check!"

#         if status:
#             surf = small.render(status, True, (0,0,0))
#             # draw a banner at top
#             banner = pygame.Surface((WIDTH, 26))
#             banner.fill((255, 255, 200))
#             screen.blit(banner, (0, 0))
#             screen.blit(surf, (8, 4))

#         pygame.display.flip()

#     running = True
#     while running:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 mx, my = event.pos
#                 sq = coords_to_square(mx, my)
#                 if sq is None:
#                     selected_sq, legal_to = None, []
#                 else:
#                     pc = board.piece_at(sq)
#                     if selected_sq is None:
#                         # select a piece of the side to move
#                         if pc and pc.color == board.turn:
#                             selected_sq = sq
#                             legal_to = legal_destinations(board, selected_sq)
#                     else:
#                         # attempt a move from selected_sq to sq
#                         move = chess.Move(from_square=selected_sq, to_square=sq)
#                         # try to infer promotion (promote to queen by default if needed)
#                         if move in board.legal_moves:
#                             board.push(move)
#                             selected_sq, legal_to = None, []
#                         else:
#                             # If promotion is required, add queen promotion
#                             if chess.square_rank(sq) in (0, 7) and board.piece_at(selected_sq) and \
#                                board.piece_at(selected_sq).piece_type == chess.PAWN:
#                                 promo = chess.Move(selected_sq, sq, promotion=chess.QUEEN)
#                                 if promo in board.legal_moves:
#                                     board.push(promo)
#                                     selected_sq, legal_to = None, []
#                                     continue
#                             # else maybe clicked own piece to reselect
#                             pc2 = board.piece_at(sq)
#                             if pc2 and pc2.color == board.turn:
#                                 selected_sq = sq
#                                 legal_to = legal_destinations(board, selected_sq)
#                             else:
#                                 # invalid — keep selection or clear
#                                 pass

#         draw()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
    # main()
