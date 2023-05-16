# DAILY CHALLENFE - TRANSLATOR

# I DID THE EXERCICE BUT IT DOES NOT WORK! 
# EVERYTIME, IT SAID :
# ModuleNotFoundError: No module named 'translate'
# ModuleNotFoundError: No module named 'googletrans'
# ModuleNotFoundError: No module named 'translate_api'
# AND I KNOW THAT I CORRECTLY INSTALLED ALL BECAUSE IT WAS WRITEN "SUCCESFULY INSTALED" IN COMMAND


# First version -----------------------------------------------------------
from translate import Translator
translator = Translator(to_lang="fr") 
translation = translator.translate("Hello, how are you?")  
print(translation) 


# Second version -----------------------------------------------------------
from googletrans import Translator
translator = Translator()
translation = translator.translate("Hello, how are you?", dest="fr")
print(translation.text)



# Third version -------------------------------------------------------------
from translate_api import TranslateAPI
translator = TranslateAPI()
translation = translator.translate("Hello, how are you?", target_language="fr")
print(translation)
