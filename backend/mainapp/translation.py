from modeltranslation.translator import translator, TranslationOptions
from .models import Yangiliklar, Elonlar, Yunalishlar, Haqimizda, Rahbariyat

class YangiliklasTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class ElonlarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class YunalishlarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class HaqimizdaTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('ism_familya', 'sohasi', 'mutaxassis', 'haqida', 'yutuqlar', 'maqsadlarim')

translator.register(Yunalishlar, YunalishlarTranslationOptions)
translator.register(Elonlar, ElonlarTranslationOptions)
translator.register(Yangiliklar, YangiliklasTranslationOptions)
translator.register(Haqimizda, HaqimizdaTranslationOptions)
translator.register(Rahbariyat, RahbariyatTranslationOptions)