# Ranking PTD #20 — as 5 plataformas digitais por onde mais chegam tentativas de golpe no Brasil (2026).
# Base: Global Anti-Scam Alliance (GASA) com a Opinium, "O Estado dos Golpes no Brasil 2026" (pesquisa nacional com 1.170
# adultos, 16/03 a 13/04/2026), divulgado em ago/2026, via Mobile Time (06/08/2026), Correio (ago/2026) e outros:
# plataformas citadas por quem recebeu tentativas de golpe: WhatsApp 64%, Gmail 32%, Instagram 22%, Facebook 17%,
# Google 13% (Telegram 12% fica de fora). Respostas múltiplas: a soma passa de 100% (dito na narração).
# Mesmo relatório: 81% dos adultos tiveram contato com algum golpe em 12 meses (gancho).
# "O dobro do 2º lugar" = 64 / 32 = 2,0, CÁLCULO do canal.
# Visual: tema NOVO laranja/ciano com o gráfico "phones" (tela do celular enche; escala absoluta, piso 0).
# Dia COM longo (EP18), mas às 12:00 o EP18 ainda não está no ar: o Short aponta para o EP17 (golpe do Pix).
TITLE = "As 5 plataformas por onde mais chega golpe no Brasil (o nº 1 está em 64%) #shorts"
THEME = {"accent": (255, 150, 60), "accent2": (80, 210, 240), "bar_col": (110, 60, 24), "hl_col": (255, 150, 60),
         "glow": (60, 30, 14), "bar": "O ESTADO DOS GOLPES NO BRASIL 2026", "chart": "phones", "floor": 0}
HOOK = {"say": "Oito em cada dez brasileiros adultos tiveram contato com algum golpe no último ano. Mas por onde eles chegam? As cinco plataformas mais citadas. E o primeiro lugar tem o dobro do segundo.",
        "top": "Por onde chega o golpe", "sub": "% de quem recebeu tentativas", "tease": "81% tiveram contato com golpe"}
SRC = "GASA, O Estado dos Golpes no Brasil 2026"
ITEMS = [
 {"rank": 5, "name": "Google", "short": "Google", "tag": "anúncios e resultados falsos", "num": 13.0, "suffix": "%", "dec": 0,
  "unit": "de quem recebeu tentativas", "source": SRC,
  "say": "Número cinco: o Google, com anúncios e páginas falsas. Treze por cento."},
 {"rank": 4, "name": "Facebook", "short": "Facebook", "tag": "lojas e perfis falsos", "num": 17.0, "suffix": "%", "dec": 0,
  "unit": "de quem recebeu tentativas", "source": SRC,
  "say": "Número quatro: o Facebook. Dezessete por cento."},
 {"rank": 3, "name": "Instagram", "short": "Instagram", "tag": "a loja que não existe", "num": 22.0, "suffix": "%", "dec": 0,
  "unit": "de quem recebeu tentativas", "source": SRC,
  "say": "Número três: o Instagram, terra da loja com preço bom demais. Vinte e dois por cento."},
 {"rank": 2, "name": "Gmail", "short": "Gmail", "tag": "o e-mail com link falso", "num": 32.0, "suffix": "%", "dec": 0,
  "unit": "de quem recebeu tentativas", "source": SRC,
  "say": "Número dois: o e-mail do Gmail, com boleto e link falsos. Trinta e dois por cento. E uma pessoa pode citar mais de uma plataforma."},
 {"rank": 1, "name": "WhatsApp", "short": "WhatsApp", "tag": "o dobro do 2º lugar", "num": 64.0, "suffix": "%", "dec": 0,
  "unit": "de quem recebeu tentativas", "source": SRC,
  "say": "E o número um: o WhatsApp. Sessenta e quatro por cento de quem recebeu tentativas de golpe citou o aplicativo. O dobro do segundo lugar. É ali que chegam o falso parente e a falsa central."},
]
OUTRO = {"say": "Caiu no golpe e fez o Pix? Para onde vai o dinheiro em segundos, e quem tem que devolver, está no vídeo completo. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
