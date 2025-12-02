from modeltranslation.translator import translator, TranslationOptions
from .models import Yangiliklar, Elonlar, Yunalishlar

class YangiliklasTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class ElonlarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class YunalishlarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Yunalishlar, YunalishlarTranslationOptions)
translator.register(Elonlar, ElonlarTranslationOptions)
translator.register(Yangiliklar, YangiliklasTranslationOptions)
