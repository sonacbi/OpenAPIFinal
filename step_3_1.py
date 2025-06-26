import deepl

DEEPL_KEY = "API_KEY" # 복사한 API 키를 붙여 넣으세요
tran = deepl.Translator(DEEPL_KEY)
resp = tran.translate_text("HELLO WORLD", source_lang="EN", trage_lang="KO")
resp.text