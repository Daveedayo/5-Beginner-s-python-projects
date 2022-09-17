from translate import Translator

translator = Translator(from_lang="english", to_lang="chinese")
translation = translator.translate("How are you doing")

print(translator)