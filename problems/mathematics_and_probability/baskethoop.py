#Which games is best for different probabilties of scoring (p)

#Game 1: 1 shoot 1 hit
#Game 2: 3 shoots at least 2 hits

#p(game_1) = p 
#and 
#p(game_2=sum{X_i}>=2) = p(sum{X_i}=3) + p(sum{X_i}=2) = p^3 + 3p^2(1-p)

#p(game_1)>p(game_2) => p > p(p^2+3p(1-p) => 1 > p^2+3p-3p^2 = 3p-2p^2
#1 + 2p^2 -3p > 0 => p^2 - 3p/2 + 1/2 > 0 => 
#p = +3/4+-sqrt(9/16-8/16) = 3/4 +-sqrt(1/16) = 3/4+-1/4 = {1,1/2}
#And since p \in [0,1], game_1 if p<1/2 else game_2

