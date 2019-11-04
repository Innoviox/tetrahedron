from .rubix import *

def test():
    strs = {
        Color.RED: {Dir.LEFT: """  Y  
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
YYYYY""", Dir.RIGHT: """  G  
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
YYYYY"""}, Color.GREEN: {Dir.LEFT: """  R  
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
YYYYY""", Dir.RIGHT: """  R  
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
YYYYY"""}, Color.YELLOW: {Dir.LEFT: """  R  
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
RRRYY""", Dir.RIGHT: """  R  
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
BBBYY"""}, Color.BLUE: {Dir.LEFT: """  R  
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
YYBBB""", Dir.RIGHT: """  R  
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
            if d is Dir.TOP: continue
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

    t.move(Color.GREEN, 1, Dir.RIGHT)
    t.move(Color.YELLOW, 1, Dir.RIGHT)
    t.move(Color.GREEN, 1, Dir.LEFT)
    t.move(Color.YELLOW, 1, Dir.LEFT)
    t.move(Color.GREEN, 1, Dir.LEFT)
    t.move(Color.RED, 1, Dir.LEFT)
    t.move(Color.GREEN, 1, Dir.RIGHT)
    t.move(Color.RED, 1, Dir.RIGHT)
    t.move(Color.GREEN, 1, Dir.RIGHT)
    t.move(Color.YELLOW, 1, Dir.RIGHT)
    t.move(Color.GREEN, 1, Dir.LEFT)
    t.move(Color.YELLOW, 1, Dir.LEFT)
    t.move(Color.GREEN, 1, Dir.LEFT)
    t.move(Color.RED, 1, Dir.LEFT)
    t.move(Color.GREEN, 1, Dir.RIGHT)
    t.move(Color.RED, 1, Dir.RIGHT)

    print(t)

# corkin_1()
