import random

def main():
  print("ぼっちのちんぽ or ぼっちんぽ")
  cheating_flag = input()
  print("掛け金は？")
  kakekin = int(input())

  if syonben():
    print("ションベンです。あなたの配当金は"+ str(kakekin * -1) +"です。")
    return

  if cheating_flag == "ぼっちんぽ":
    saikoro1 = random.randint(4,6)
    saikoro2 = random.randint(4,6)
    saikoro3 = random.randint(4,6)
  else:
      saikoro1 = random.randint(1,6)
      saikoro2 = random.randint(1,6)
      saikoro3 = random.randint(1,6)

  deme = [saikoro1,saikoro2,saikoro3]
  print("あなたの配当金は"+str(kakekin * yaku(deme))+"です。")

def syonben():
  if random.random() > 0.9:
    return True
  return False

def yaku(deme): 
  #count[0]にはデメ[0]と一致している目が何個あるか代入される。なので1以上確定。
  #countの中に2があるならば、"通常の目"となる。3であるならば、"ゾロ目"となる。
  count = [deme.count(deme[0]), deme.count(deme[1]), deme.count(deme[2])]
  
  if 3 in count: #ゾロ目
    if sum(deme) == 3: #ピンサロかどうか
      print("ピンゾロ：配当5倍です。")
      return 5
    print("ゾロ目：配当3倍です。")
    return 3
  elif 2 in count: #通常の目
    print("通常の目：配当1倍です。")
    return 1
  else:
    if sum(deme) == 15: #シゴロであるかどうか。
      print("シゴロ：配当2倍です。")
      return 2
    elif sum(deme) == 6:
      print("ヒフミ：配当-2倍です。")
      return -2
    print("あなたの負けです。")
    return 0

if __name__ == "__main__":
    main()