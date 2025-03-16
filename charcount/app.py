# This script looks at a list of over 40k C64 game titles.
# It finds the best "first" character and the best "next" character.
# Best as is "fewest button clicks on the Tapuino << >> keys" to statistically type a game name.

# List of chars that are allowed in a title
okchars = " abcdefghijklmnopqrstuvwxyz0123456789_-"  #  "{}[]().'&+,#!$;%~^"


# Checks the frequency of fst (first, starting) character of all titles
# Rejects (ignores) the characters that are not in `okchars`
# - prints histogram
# - prints steps requires to key up/down to other fst chars
# - prints best first char
def bestfst(titles) :
    # collect count of all first chars
    fstfreq={}
    rejected=""
    rejectcount=0
    for title in titles :
        fst=title[0].lower()
        if not fst in okchars : 
            rejectcount+=1
            if not fst in rejected : rejected+=fst
            continue
        if fst in fstfreq :
            fstfreq[fst]+=1
        else :
            fstfreq[fst]=1
    # print the first char freq
    #print( f"fst {rejectcount} chars rejected: {rejected}")
    #for ch in fstfreq :
    #    print( f"fst '{ch}' count {fstfreq[ch]:4}")
    # which first char gives least amount of up/down clicks
    mod = len(okchars)
    minaver= mod
    minchar= None
    for fix,fst in enumerate(okchars) :
        #print( f"dist to '{fst}'" )
        steps= 0
        count= 0
        for aix,alt in enumerate(okchars) :
            d1= (mod+fix-aix) % mod
            d2= (mod+aix-fix) % mod
            d=min(d1,d2)
            freq= fstfreq[alt] if alt in fstfreq else 0
            #print( f"  for '{alt}' {d:2}: {freq}*{d}={freq*d} " )
            steps += d*freq
            count+=freq
        aver = steps/count
        if aver<minaver :
            minaver= aver
            minchar= fst
        #print( f"fst '{fst}' requires {steps} for all others; {aver:5.2f} on average" )
    print( f"fst '{minchar}' has best average {minaver:5.2f}" )
        

# Checks the frequency of all nxt (non-first) character of all titles
# Rejects (ignores) the characters that are not in `okchars`
def bestnxt(titles) :
    # collect count of all nxt chars
    nxtfreqs={}
    rejected=""
    rejectcount=0
    for rawtitle in titles :
        title = [c for c in rawtitle if c in okchars]
        for prv,nxt in zip(title,title[1:]) :
            if prv in nxtfreqs: 
                if nxt in nxtfreqs[prv]:
                    nxtfreqs[prv][nxt] += 1
                else :
                    nxtfreqs[prv][nxt] = 1
            else :
                nxtfreqs[prv] = { nxt: 1 }                
    # print the nxt chars
    #for prv in nxtfreqs :
    #    print( f"nxt '{prv}': ", end='')
    #    for nxt in nxtfreqs[prv] :
    #        print( f" {nxt}/{nxtfreqs[prv][nxt]}", end='')
    #    print()
    # which nxt char gives least amount of up/down clicks from prv
    mod = len(okchars)
    for prv in okchars :
        #print( f"prv '{prv}'" )
        minaver= mod
        minchar= None
        for nix,nxt in enumerate(okchars) :
            #print( f"  nxt '{nxt}'" )
            steps= 0
            count= 0
            for char in nxtfreqs[prv]:
                cix = okchars.find(char)
                d1= (mod+cix-nix) % mod
                d2= (mod+nix-cix) % mod
                d=min(d1,d2)
                freq=nxtfreqs[prv][char]
                count+=freq
                #print( f"    '{char}' {d:2}: {freq}*{d}={freq*d} " )
                steps += d*freq
            aver = steps/count
            if aver<minaver :
                minaver= aver
                minchar= nxt
            #print( f"  '{nxt}' requires {steps} for all others; {aver:5.2f} on average" )
        print( f"nxt '{prv}': '{minchar}' has best average {minaver:5.2f}" )

       
            
        

def main() :
    titles=[]
    with open('titles.txt', 'r') as file:
        for line in file:
            title = line[0:-1]
            if len(title)>1 : titles.append(title)
            else : print(f"'{title}'")
    print( f"num titles {len(titles)}" )
    
    bestfst(titles)
    bestnxt(titles)


if __name__ == "__main__":
    main()
