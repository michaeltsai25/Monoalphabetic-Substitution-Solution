import sys
sys.path.append("./Code/lib")
from guess import Guess
from constants import *
from utils import *

class Runner:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        guess = Guess(self.ct)
        div = MAX_KL_DIV
        exc_max_iter = False
        count = 0
        c = 0
        last  = ""
        prev_fit=0
        while not guess.decrypted() or guess.guess == "butiftheofficialsfoundouthewouldhavebeenpubliclyexecutedforincitingarebellionmostofthepeacekeepersturnablindeyetothefewofuswhohuntbecausetheyreashungryforfreshmeatasanybodyisinfacttheyreamongourbestcustomersbuttheideathatsomeonemightbearmingtheseamwouldneverhavebeenallowedinthefallafewbravesoulssneakintothewoodstoharvestapplesbutalwaysinsightofthemeadowalwayscloseenoughtorunbacktothesafetyofdistrictiftroublearisesdistricttwelvewhereyoucanstarvetodeathinsafetyimuttertheniglancequicklyovermyshoulderevenhereeveninthemiddleofnowhereyouworrysomeonemightoverhearyouwheniwasyoungeriscaredmymothertodeaththethingsiwouldblurtoutaboutdistrictaboutthepeoplewhoruleourcountrypanemfromthefaroffcitycalledthecapitoleventuallyiunderstoodthiswouldonlyleadustomoretroublesoilearnedtoholdmytongueandtoturnmyfeaturesintoanindifferentmasksothatnoonecouldeverreadmythoughtsdomyworkquietlyinschoolmakeonlypolitesmalltalkinthepublicmarketdiscusslittlemorethantradesinthehobwhichistheblackmarketwhereimakemostofmymoneyevenathomewhereiamlesspleasantiavoiddiscussingtrickytopicslikethereapingorfoodshortagesorthehungergamesprimmightbegintorepeatmywordsandthenwherewouldwebeinthewoodswaitstheonlypersonwithwhomicanbemyself":
            n = guess.num_words()
            x = guess.random_swap_neigh_chars()
            freq = [value for value in calcFreq(guess.guess).values()]
            if guess.fitness() < prev_fit: #guess.num_words() < n or kl_divergence(freq) > div: #loosen constraints
                guess.swap_general(x)
            if count > MAX_ITER and guess.num_words() < MIN_WORDS:
                guess.reset()
                exc_max_iter = True
            prev_fit=guess.fitness()
            count += 1
            c += 1
            if c >= 5000:
                break
            if exc_max_iter:
                div += 0.01
            if not guess.guess == last:
                print(guess.guess) #just to track the evolution of the algorithm's guesses, may remove if desired
                print(guess.ct_to_pt)
                last = guess.guess
        return guess.guess

if __name__ == "__main__":
    r = Runner("lvmkbmyujbbkzkgicbjvxojvmyutjvioygauluuxqvlikzipusuzvmuobjdkxzkmkxegduluiikjxwjcmjbmyuqugzuhuuqudcmvdxglikxoupumjmyubutjbvctyjyvxmluzgvcumyupdugcyvxedpbjdbducywugmgcgxpljopkckxbgzmmyupdugwjxejvdlucmzvcmjwudclvmmyukougmygmcjwujxuwkeymlugdwkxemyucugwtjvioxuaudygauluuxgiijtuokxmyubgiigbutldgaucjviccxughkxmjmyutjjocmjygdaucmgqqiuclvmgitgpckxckeymjbmyuwugojtgitgpczijcuuxjveymjdvxlgzhmjmyucgbumpjbokcmdkzmkbmdjvliugdkcucokcmdkzmmtuiautyudupjvzgxcmgdaumjougmykxcgbumpkwvmmudmyuxkeigxzunvkzhipjaudwpcyjviouduauxyuduuauxkxmyuwkooiujbxjtyudupjvtjddpcjwujxuwkeymjaudyugdpjvtyuxktgcpjvxeudkczgduowpwjmyudmjougmymyumykxecktjviolivdmjvmgljvmokcmdkzmgljvmmyuqujqiutyjdviujvdzjvxmdpqgxuwbdjwmyubgdjbbzkmpzgiiuomyuzgqkmjiuauxmvgiipkvxoudcmjjomykctjviojxipiugovcmjwjdumdjvliucjkiugdxuomjyjiowpmjxevugxomjmvdxwpbugmvduckxmjgxkxokbbuduxmwgchcjmygmxjjxuzjviouauddugowpmyjveymcojwptjdhnvkumipkxczyjjiwghujxipqjikmucwgiimgihkxmyuqvlikzwgdhumokczvccikmmiuwjdumygxmdgouckxmyuyjltykzykcmyuligzhwgdhumtyudukwghuwjcmjbwpwjxupuauxgmyjwutyudukgwiuccqiugcgxmkgajkookczvcckxemdkzhpmjqkzcikhumyudugqkxejdbjjocyjdmgeucjdmyuyvxeudegwucqdkwwkeymluekxmjduqugmwptjdocgxomyuxtyudutjviotulukxmyutjjoctgkmcmyujxipqudcjxtkmytyjwkzgxluwpcuib")
    r.main()
    #use larger text