import grab

g = grab()
g.setup(url='http://yandex.ru', log_file='out.html')
g.request()