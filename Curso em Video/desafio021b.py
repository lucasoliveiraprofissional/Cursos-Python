# Tocar um mp3 com python
# VERSÃO ACOMPANHANDO PROF - não quis pegar tudo pronto no Youtube
# várias maneiras de fazer isso, é o mais fácil, o pygame, para criar jogos

from pygame import mixer, event
mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()
#esperar a musica terminar para encerrar o programa:
event.wait()
