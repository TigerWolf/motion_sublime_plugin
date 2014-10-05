import sublime_plugin
import re



def to_ruby_case(text):
    callback = lambda pat: pat.group(1).upper()
    text = re.sub("_(\w)", callback, text)
    if text[0].islower():
        text = text[0].upper() + "::" + text[1:]
    return text
    
def to_snake_case(text):
    text = re.sub('[-. _]+', '_', text)
    if text.isupper():
        # Entirely uppercase; assume case is insignificant.
        return text.lower()
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text).lower()

def to_snake_case_graceful(text):
    text = re.sub('[-. _]+', '_', text)
    if text.isupper():
        # Entirely uppercase; assume case is insignificant.
        return text;
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text)    
    
def strip_wrapping_underscores(text):
    return re.sub("^(_*)(.*?)(_*)$", r'\2', text)    

def run_on_selections(view, edit, func, no_lower=False):
    for s in view.sel():
        region = s if s else view.word(s)
        if no_lower:
            text = to_snake_case_graceful(view.substr(region))
        else:
            text = to_snake_case(view.substr(region))
        text = strip_wrapping_underscores(text)
        view.replace(edit, region, func(text))

class ConvertToRuby(sublime_plugin.TextCommand):
    def run(self, edit):
        run_on_selections(self.view, edit, to_ruby_case)
