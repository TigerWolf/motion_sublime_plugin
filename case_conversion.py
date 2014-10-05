import sublime_plugin
import re



def to_ruby_case(text):
    callback = lambda pat: pat.group(1).upper()
    text = re.sub("_(\w)", callback, text)
    if text[0].islower():
        text = text[0].upper() + "::" + text[1:]
    return text


class ConvertToRuby(sublime_plugin.TextCommand):
    def run(self, edit):
        run_on_selections(self.view, edit, to_ruby_case)
