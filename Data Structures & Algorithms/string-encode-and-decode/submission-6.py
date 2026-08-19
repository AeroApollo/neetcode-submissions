class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_msg = ""
        for word in strs:
            enc_msg += str(len(word)) +"#" +word
        return enc_msg

    def decode(self, s: str) -> List[str]:
        #print(s)
        dec_msg = []
        i = 0
        while i < len(s):
            if s[i] == "#": 
                hash_ind = s.index('#') #get index of #
                #print(s[:hash_ind],s[hash_ind:])
                str_len = int(s[:hash_ind]) #anything behind # should be len of string
                s = s[hash_ind+1:] 
                word = s[:str_len]
                #print(word)
                dec_msg.append(word)
                s = s[str_len:]
                #print(s)
                i = 0
            i += 1

        return dec_msg

