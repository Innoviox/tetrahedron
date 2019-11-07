from rubix import *

def test():
    strs = {
        1: {1: """  Y  
 YYY 
RRRRR
  R  
 RRR 
GGGGG
  B  
 BBB 
BBBBB
  G  
 GGG 
YYYYY""", -1: """  G  
 GGG 
RRRRR
  Y  
 YYY 
GGGGG
  B  
 BBB 
BBBBB
  R  
 RRR 
YYYYY"""}, 2: {1: """  R  
 BRR 
BBBRR
  G  
 GGR 
GGRRR
  B  
 GBB 
GGGBB
  Y  
 YYY
YYYYY""", -1: """  R  
 GRR 
GGGRR
  G  
 GGB 
GGBBB
  B  
 RBB 
RRRBB
  Y  
 YYY 
YYYYY"""}, 4: {1: """  R  
 RRB 
RRBBB
  G  
 GGG 
GGGGG
  Y  
 YYY 
BBBBB
  Y  
 RYY 
RRRYY""", -1: """  R  
 RRY 
RRYYY
  G  
 GGG 
GGGGG
  R  
 RRR 
BBBBB
  Y  
 BYY 
BBBYY"""}, 3: {1: """  R  
 RRR 
RRRRR
  G  
 YGG 
YYYGG
  B  
 BBG 
BBGGG
  Y  
 YYB 
YYBBB""", -1: """  R  
 RRR 
RRRRR
  G  
 BGG 
BBBGG
  B  
 BBY 
BBYYY
  Y  
 YYG 
YYGGG"""}}
    for c in Color:
        for d in Dir:
            if d is 0: continue
            t = Tetra()
            t.move(c, 1, d)
            if c not in strs: continue
            if d not in strs[c]: continue
            
            if ''.join(str(t).strip().split()) == ''.join(strs[c][d].strip().split()):
                print(f"passed test {c} {d}")
            else:
                print(f"failed test {c} {d}")
                print(t)
                return
                # print(strs[c][d])

test()

def corkin_1():
    t = Tetra()

    t.move(2, 1, -1)
    t.move(4, 1, -1)
    t.move(2, 1, 1)
    t.move(4, 1, 1)
    t.move(2, 1, 1)
    t.move(1, 1, 1)
    t.move(2, 1, -1)
    t.move(1, 1, -1)
    t.move(2, 1, -1)
    t.move(4, 1, -1)
    t.move(2, 1, 1)
    t.move(4, 1, 1)
    t.move(2, 1, 1)
    t.move(1, 1, 1)
    t.move(2, 1, -1)
    t.move(1, 1, -1)

    print(t)

# corkin_1()
