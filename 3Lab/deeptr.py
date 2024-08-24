# deeptr.py
from translation_package.module2 import TransLate, LangDetect, CodeLang, LanguageList

print(TransLate("Hello", "en", "es"))
print(LangDetect("Bonjour", "all"))
print(CodeLang("uk"))
print(LanguageList("screen", "Петро"))