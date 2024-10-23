class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse ={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        l = []
        for word in words:
            wr = []
            for x in word:
                wr.append(morse[x])
            l.append(''.join(wr))
        return len(set(l))
        