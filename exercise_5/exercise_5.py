import spacy
import re
from spacy.tokenizer import Tokenizer
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher
# import textacy


def separate(number: int):
    print(f"============ {number} ============")


nlp = spacy.load("pl_core_news_sm")

# separate(1)
# text = 'Ten program jest piątym zadaniem z przedmiotu Wstęp do uczenia maszynowego'
# doc = nlp(text)
# print([token.text for token in doc])
#
# separate(2)
# file_text = open('text.txt').read()
# file_doc = nlp(file_text)
# print([token.text for token in file_doc])
#
# separate(3)
# sentences_text = 'To jest pierwsze zdanie. To jest natomiast drugie zdanie. A dalej trzecie.'
# sentences_doc = nlp(sentences_text)
# sentences = list(sentences_doc.sents)
# for sentence in sentences:
#     print(sentence)
#
# separate(4)
# exclamation_text = 'To jest pierwsze zdanie! To jest natomiast drugie zdanie! A dalej trzecie!'
#
#
# def set_exclamation_boundary(doc):
#     for token in doc[:-1]:
#         if token.text == '!':
#             doc[token.i + 1].is_sent_start = True
#     return doc
#
#
# exclamation_nlp = spacy.load('pl_core_news_sm')
# exclamation_nlp.add_pipe(set_exclamation_boundary, before='parser')
# exclamation_doc = exclamation_nlp(exclamation_text)
# exclamation_sentences = list(exclamation_doc.sents)
#
# for sentence in exclamation_sentences:
#     print(sentence)

# separate(5)
# text_5 = 'Ten program jest piątym zadaniem z przedmiotu Wstęp do uczenia maszynowego'
# doc_5 = nlp(text_5)
# for token in doc_5:
#     print(token, token.idx, token.text_with_ws, token.is_alpha, token.is_punct, token.is_space, token.shape_, token.is_stop)

# separate(6)
# text_6 = 'To jest niebiesko-czarna farba'
# token_nlp = spacy.load('pl_core_news_sm')
# prefix_re = spacy.util.compile_prefix_regex(token_nlp.Defaults.prefixes)
# suffix_re = spacy.util.compile_suffix_regex(token_nlp.Defaults.suffixes)
# infix_re = re.compile(r'''[-~]''')
#
#
# def customize_tokenizer(nlp):
#     return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
#                      suffix_search=suffix_re.search,
#                      infix_finditer=infix_re.finditer,
#                      token_match=None
#                      )
#
#
# token_nlp.tokenizer = customize_tokenizer(token_nlp)
# token_doc = token_nlp(text_6)
# print([token.text for token in token_doc])

# separate(7)
# text_7 = 'Aby zrobić to zadanie, będą potrzebne dwie rzeczy, a nie jedna'
# doc_7 = nlp(text_7)
# stop_words_doc = [token for token in doc_7 if not token.is_stop]
# print(stop_words_doc)

# separate(8)
# text_8 = 'To jest piąte zadanie i takiego zadania nie widział żaden student robiący wiele zadań'
# doc_8 = nlp(text_8)
# for token in doc_8:
#     print(token, token.lemma_)

# separate(9)
# text_9 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# doc_9 = nlp(text_9)
# words = [token.text for token in doc_9 if not token.is_stop and not token.is_punct]
# frequency = Counter(words)
# common_words = frequency.most_common(7)
# print(common_words)
# unique_words = [word for (word, freq) in frequency.items() if freq == 1]
# print(unique_words)

# separate(10)
# text_10 = 'Ala ma kota, a kot to niemota'
# doc_10 = nlp(text_10)
# nouns = []
# for token in doc_10:
#     print(token, token.tag_, token.pos_, spacy.explain(token.tag_))
#     if (token.pos_ == 'NOUN'):
#         nouns.append(token)

# separate(11)
# text_11 = 'Ala ma kota, a kot to niemota'
# doc_11 = nlp(text_11)
# displacy.serve(doc_11, style='dep')

# separate(12)
# def is_token_allowed(token):
#     if not token or not token.string.strip() or token.is_stop or token.is_punct:
#         return False
#     return True
#
# def preprocess_token(token):
#     return token.lemma_.strip().lower()
#
# text_12 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# doc_12 = nlp(text_12)
# tokens_12 = [preprocess_token(token) for token in doc_12 if is_token_allowed(token)]
# print(tokens_12)

# separate(13)
# text_13 = 'Mój numer telefonu to 123 123 123'
# doc_13 = nlp(text_13)
# matcher = Matcher(nlp.vocab)
#
#
# def extract_phone_number(doc):
#     pattern = [{'SHAPE': 'ddd'}, {'ORTH': ' '},
#                {'SHAPE': 'ddd'}, {'ORTH': ' '},
#                {'SHAPE': 'ddd'}]
#     matcher.add('PHONE_NUMBER', None, pattern)
#     matches = matcher(doc)
#     for id, start, end in matches:
#         span = doc[start:end]
#         return span.text
#
# print(extract_phone_number(doc_13))

# separate(14)
# text_14 = 'Ola gra na komputerze'
# doc_14 = nlp(text_14)
# for token in doc_14:
#     print(token.text, token.tag_, token.head, token.dep_)
#
# separate(15)
# text_15 = 'Ala jest uczennicą, która posiada kota'
# doc_15 = nlp(text_15)
# print([token.text for token in doc_15[2].children])
# print(doc_15[2].nbor(-1))
# print(doc_15[2].nbor())
# print(doc_15[2].lefts)

# separate(16)
# text_16 = 'To jest piękny obraz, który został namalowany 21 stycznia w Gdyni'
# doc_16 = nlp(text_16)
# for chunk in doc_16.noun_chunks:
#     print(chunk)

# separate(17)
# text_17 = 'To jest zadanie dotyczące analizy tekstu'
# pattern = r'(<VERB>?<ADV>*<VERB>+)'
# doc_17 = textacy.make_spacy_doc(text_17, lang='pl_core_news_sm')
# verb_phrases = textacy.extract.pos_regex_matches(doc_17, pattern)
# for chunk in verb_phrases:
#     print(chunk.text)

separate(18)
# text_18 = 'Gliwice, Gdynia i Gorzów Wielkopolski to nazwy polskich miast, które zaczynają się na literę G'
# doc_18 = nlp(text_18)
# for entity in doc_18.ents:
#     print(entity.text, entity.start_char, entity.end_char, entity.label_, spacy.explain(entity.label_))
#
# displacy.serve(doc_18, style='ent')

text_18b = 'Jan Kowalski, Adam Nowak i Anna Wiśniewska to nasi najlepsi pracownicy'
doc_18b = nlp(text_18b)

def replace_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '*****'
    return token.string

def replace_names_in_doc(doc):
    for entity in doc.ents:
        entity.merge()
    tokens = map(replace_names, doc)
    return ''.join(tokens)

print(replace_names_in_doc(doc_18b))