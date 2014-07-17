from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
import random

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

@dajaxice_register
def refresh_words(request, word_bank_size):
    word_list = []
    for i in range(0,word_bank_size):
        word_list.append(random.choice(WORDS))

    dajax = Dajax()
    render = render_to_string('pamplesneak/wordbox.html', {'word_list': word_list})
    dajax.assign('#words_box', 'innerHTML', render)
    print "grrrr"
    return dajax.json()