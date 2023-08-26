english_pirate_dict = {"hello":"ahoy", "to":"ta", "was":"be", "cheat":"hornswaggle", "cheating":"hornswaggle'n",
"toilet":"head", "hi":"yo-ho-ho", "man":"matey","pardon":"avast", "excuse":"arrrgh", "yes":"aye", "my":"me", 
"friend":"matey", "sir":"matey", "miss":"comely wench", "stranger":"scurvy dog", "officer":"foul blaggart", 
"where":"whar", "is":"be", "for":"fer", "are":"be", "am":"be", "the":"th", "going":"goin", "you":"ye", 
"your":"yer", "tell":"be tellin", "know":"be knowin", "far":"many leagues", "old":"barnacle-covered", 
"attractive":"comely", "happy":"grog-filled", "quickly":"smartly", "nearby":"broadside", "restroom":"head", 
"restaurant":"galley", "hotel":"fleabag inn", "bar":"Skull & Scuppers", "mall":"market", "bank":"buried treasure", 
"die":"visit Davey Jones Locker", "died":"visited Davey Jones Locker", "kill":"keel-haul", "killed":"keel-hauled", 
"sleep":"take a caulk", "stupid":"addled", "after":"aft", "stop":"belay", "nonsense":"bilge", "ocean":"briny deep", 
"go":"get ye", "song":"shanty", "money":"doubloons", "drunk":"three sheets to the wind", "food":"grub", "nose":"prow", 
"leave":"weigh anchor", "cheat":"hornswaggle", "forward":"fore", "child":"sprog", "children":"sprogs", "sailor":"swab", 
"lean":"careen", "find":"come across", "mother":"dear ol mum, bless her black soul", 
"mom":"dear ol mum, bless her black soul", "drink":"barrel o rum", "of":"o", "there":"thar", "my":"me", "mine":"me", 
"gun":"cannon", "monkey":"tailed imp", "expert":"old smartly", "flag":"Jolly Roger", "dad":"capn", "teacher":"wise sage", 
"phone":"cursed device", "computer":"magic box", "speak":"parley", "person":"landlubber", "people":"landlubbers", 
"sir":"matey", "hotel":"fleabag", "student":"swabbie", "boy":"matey", "professor":"foul blaggart", "restaurant":"galley", 
"students":"swabbies", "bathroom":"head"}

import string
english = input("Enter the English words you want it to be translated: ").lower()
only_string = ''.join(ch for ch in english if ch not in set(string.punctuation))
eng_trans = only_string.split()

pirate = ""
for word in eng_trans:
    if word in english_pirate_dict:
        pirate += english_pirate_dict[word] + " "
    else:
        pirate += word + " "
        
print(pirate)