import random
import os
import time

def clear_screen():
    # Ekranı temizler
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    # 3x3'lük bir matris oluşturur ve içini harflerle doldurur
    characters = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E']
    random.shuffle(characters)
    return [characters[i*3:(i+1)*3] for i in range(3)]

def display_board(board, revealed):
    # Tahtayı gösterir
    for i in range(3):
        for j in range(3):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('*', end=' ')
        print()
    print()

def get_user_input():
    # Kullanıcıdan giriş alır
    while True:
        try:
            row, col = map(int, input("Satır ve sütun seçin (0-2) arası, örn: 0 1: ").split())
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Lütfen 0 ile 2 arasında bir değer girin.")
        except ValueError:
            print("Geçerli bir giriş yapın.")

def check_for_match(board, revealed):
    # Eğer iki açık kart eşleşirse true döner
    open_cards = [(i, j) for i in range(3) for j in range(3) if revealed[i][j]]
    if len(open_cards) == 2:
        (r1, c1), (r2, c2) = open_cards
        if board[r1][c1] == board[r2][c2]:
            return True
        else:
            revealed[r1][c1] = False
            revealed[r2][c2] = False
            return False
    return None

def check_for_three_in_a_row(board):
    # Eğer 3 aynı karakter yan yana ise true döner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def remove_three_in_a_row(board):
    # 3 aynı karakter yan yana ise onları siler
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            board[i] = [' ' for _ in range(3)]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            for j in range(3):
                board[j][i] = ' '
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        for i in range(3):
            board[i][i] = ' '
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        for i in range(3):
            board[i][2-i] = ' '

def play_game():
    board = create_board()
    revealed = [[False]*3 for _ in range(3)]
    turns = 0
    pairs_found = 0

    while pairs_found < 4:
        clear_screen()
        display_board(board, revealed)
        row1, col1 = get_user_input()
        revealed[row1][col1] = True
        clear_screen()
        display_board(board, revealed)
        row2, col2 = get_user_input()
        revealed[row2][col2] = True
        clear_screen()
        display_board(board, revealed)
        
        match = check_for_match(board, revealed)
        if match:
            pairs_found += 1
        else:
            time.sleep(1)
        
        if check_for_three_in_a_row(board):
            remove_three_in_a_row(board)
        
        turns += 1

    clear_screen()
    print(f"Tebrikler! {turns} turda tüm eşleşmeleri buldunuz.")

if __name__ == "__main__":
    play_game()
