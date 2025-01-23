from translate import Translator

translator = Translator(to_lang="French")

translation = translator.translate('Hello!!! Welcome to my class')

print(translation)