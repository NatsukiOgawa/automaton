# coding:utf-8
import pygame


def dec2bin(n):
    # "decode to binary"
    # 10進数を2進数の01リストに変換

    bit_list = []
    for i in range(8):
        bit_list.append(n % 2)
        n = int(n // 2)

    return bit_list


def ca(width, height, rulenum):
    # 1次元セルオートマトンの図を描画
    results = []

    # 初期状態設定
    first_row = [0] * width
    list_id = int(width // 2)
    first_row[list_id] = 1
    results.append(first_row)

    # ルールの番号を２進数に変換
    rule = dec2bin(rulenum)

    for i in range(height - 1):
        old_row = results[-1]
        new_row = []
        for j in range(width):
            # 前後のインデックスの状態を参照し次のループの状態を決定する。
            n = int(4 * old_row[(j-1) % width] + 2 * old_row[j] + old_row[(j+1) % width])
            new_row.append(rule[n])
        results.append(new_row)
    return results


if __name__ == "__main__":
    width = 300
    height = 100
    rule_num = 150  # ここのルールを255までの値で指定することで様々なパターンが出力されます。
    pygame.init()
    screen = pygame.display.set_mode((width*2, height*2))
    pygame.display.set_caption("Cellular Automaton {}".format(rule_num))

    results = ca(width, height, rule_num)

    screen.fill((0, 0, 0,))
    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (j*2, i*2, 2, 2))
            else:
                pass
        pygame.display.update()

    # 一時的に処理を停止する。
    pygame.time.wait(10000)

    # 制作したイメージをPNGに変換し保存。cellular_automaton.pyと同じディレクトリにimgが出力される。
    pygame.image.save(screen, 'pic.png')
