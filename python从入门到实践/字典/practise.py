favorite_language={
    'xie':'java',
    'liu':'c++',
    'li':'python',
}
names=['li','liu','liao']
for name in favorite_language.keys():
    if name in names:
        print(name+",thanks for joining.")
    elif name not in names:
        print(name+",please join us.")