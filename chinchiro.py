import random
import numpy as np
from matplotlib import pyplot as plt

def main():
  mochigane = 10000
  print("あなたの始めの持ち金は\\" + str(mochigane) + " です。")
  #規定外の入力があった場合、もう一度入力させるためのwhile文
  while(True):
    input_bocchinpo = input("ぼっちのちんぽ or ぼっちんぽ?： ")
    if input_bocchinpo == "ぼっちんぽ":
      cheating_flag = True
      break
    elif input_bocchinpo == "ぼっちのちんぽ":
      cheating_flag = False
      break
    else:
      #TODO: のちのちここでぼっちちゃん画像を出力させる。
      print("後藤さんちんぽでかいのね～")
  
  game_continue_flag = True
  asking_continue = True
  #game_continue_flagがTrueである限りゲームを続ける。
  while(game_continue_flag):
    print("掛け金は？")
    kakekin = kakekin()
    print("Game Start!!!")
    mochigane += chinchiro_game(cheating_flag, kakekin) - kakekin
    if mochigane < 0:
      print("持ち金がありません。ゲーム終了です。")
      game_continue_flag = False
      asking_continue = False

    print("あなたの持ち金は\\" + str(mochigane) + " です。")

    print("ゲームを続けますか？")
    #規定外の入力があった場合、もう一度入力させるためのwhile文
    while(asking_continue):
      continue_ = input("y/nを押してください。： ")
      if continue_ == "n":
        game_continue_flag = False
        print("ゲームを終了します。")
        asking_continue = False
      elif continue_ == "y":
        game_continue_flag = True
        print("ゲームを継続します。")
        asking_continue = False
      else:
        print("y/nを押してください。")
    plot_deme()
        
def kakekin():
  #規定外の入力があった場合、もう一度入力させるためのwhile文
  #数字以外入力でエラー出力
  while True:
    try:
        kakekin = int(input("掛け金は？"))
        return kakekin
        break
    except EOFError as e:
        print(e)
        break
    except ValueError as e:
        print(e)

def plot_deme():
  global deme_list
  x = [x for x in range(len(deme_list))]
  plt.plot(x,deme_list,'-')
  plt.fill_between(x,deme_list,-2,where=(deme_list > -3), facecplor='g', alpha=0.6)

  plt.title("配当倍率リスト")
  plt.show()
  return

#リターンがわかるような関数名にすること。
def chinchiro_game(cheating_flag, kakekin):
  if syonben():
    print("ションベンです。あなたの配当金は\\"+ str(kakekin * -1) +"です。")
    return kakekin * -1
  else:
    if cheating_flag:
      deme = [random.randint(4,6) for i in range(3)]
    else:
      deme = [random.randint(1,6) for i in range(3)]

    calc = kakekin * yaku(deme)
    print("あなたの配当金は\\"+ str(calc) +"です。")
    return calc
  
def syonben():
  global deme_list
  if random.random() > 0.9:
    deme_list.append(-1)
    return True
  return False

def yaku(deme): 
  #count[0]にはデメ[0]と一致している目が何個あるか代入される。なので1以上確定。
  #countの中に2があるならば、"通常の目"となる。3であるならば、"ゾロ目"となる。
  global deme_list
  count = [deme.count(deme[i]) for i in range(3)]
  
  if 3 in count: #ゾロ目
    if sum(deme) == 3: #ピンサロかどうか
      print("ピンゾロ：配当5倍です。")
      deme_list.append(5)
      return 5
    print("ゾロ目：配当3倍です。")
    deme_list.append(3)
    return 3
  elif 2 in count: #通常の目
    print("通常の目：配当1倍です。")
    deme_list.append(1)
    return 1
  else:
    if sum(deme) == 15: #シゴロであるかどうか。
      print("シゴロ：配当2倍です。")
      deme_list.append(2)
      return 2
    elif sum(deme) == 6:
      print("ヒフミ：配当-2倍です。")
      deme_list.append(-2)
      return -2
    print("あなたの負けです。")
    deme_list.append(-1)
    return -1

if __name__ == "__main__":
    deme_list
    main()
  