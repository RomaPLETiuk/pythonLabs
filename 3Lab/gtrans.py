# gtrans.py

from translation_package.module1 import TransLate, LangDetect, CodeLang, LanguageList

print(TransLate("Hello", "en", "es"))
print(LangDetect("Bonjour"))
print(CodeLang("en"))
print(LanguageList("screen", "import"))