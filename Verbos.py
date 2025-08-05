import tkinter as tk
from tkinter import *
from random import *
from pattern.text.fr import *


class JogoPika(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Jogo Pika")
        self.bind("<Escape>", lambda event: self.quit())
        self.bind("<Return>", lambda event: self.f_verificar())
        self.bind("<Control_L>", lambda event: self.f_sortear())
        self.config(bg='#1e1e2e', relief='raised', borderwidth=15)
        self.attributes("-fullscreen", True)
        altura = self.winfo_screenheight()
        largura = self.winfo_screenwidth()
        self.titulo = Label(self, font=('Arial', 50, 'bold'), text='Le Conjugame',bg ='#1e1e2e', fg = 'white', bd = 2)
        self.titulo.place(x=largura*0.33, y=altura*0.1)

        self.entrada_texto = tk.StringVar()
        self.entrada_tela = Entry(self, textvariable=self.entrada_texto, font=('Arial', 40, 'bold'), bg='#29293d',
                                  fg='white', width=25, relief='sunken', bd=4, justify = CENTER)
        self.entrada_tela.place(x=largura*0.25, y=altura*0.3)

        self.resposta_texto = tk.StringVar()
        self.resposta_label = Label(self, font=('Arial', 14, 'bold'), bd=2, relief=RIDGE, textvariable=self.resposta_texto, height=2,
                             width=25, bg='#2d2d3e', fg='#22B14C', justify=CENTER)
        self.resposta_label.place(x=largura * 0.387, y=altura * 0.45)

        self.b_verificar = Button(self, font=('Arial', 12, 'bold'),bd=2, relief=RIDGE, text='Verifier', height=2,
                                  width=10, bg='#2d2d3e', fg='white', activebackground='#404050',
                                  activeforeground='white', command=self.f_verificar)
        self.b_verificar.place(x=largura*0.6, y=altura*0.75)
        self.flag_verificar = 0

        self.b_sortear = Button(self, font=('Arial', 12, 'bold'),bd=2, relief=RIDGE, text='Choisir', height=2,
                                width=10, bg='#2d2d3e', fg='white', activebackground='#404050',
                                activeforeground='white', command=self.f_sortear)
        self.b_sortear.place(x=largura*0.3, y=altura*0.75)

        self.t_verbo = StringVar()
        self.l_verbo = Label(self, font=('Arial', 14, 'bold'), textvariable=self.t_verbo, height=2,
                             width=15, bg='#2d2d3e', fg='white', justify = CENTER)
        self.l_verbo.place(x=largura*0.2, y=altura*0.6)

        self.t_pessoa = StringVar()
        self.l_pessoa = Label(self, font=('Arial', 14, 'bold'), textvariable=self.t_pessoa, height=2,
                              width=15, bg='#2d2d3e', fg='white', justify = CENTER)
        self.l_pessoa.place(x=largura*0.35, y=altura*0.6)

        self.t_tempo = StringVar()
        self.l_tempo = Label(self, font=('Arial', 14, 'bold'), textvariable=self.t_tempo, height=2,
                             width=15, bg='#2d2d3e', fg='white', justify = CENTER)
        self.l_tempo.place(x=largura*0.5, y=altura*0.6)

        self.t_mood = StringVar()
        self.l_mood = Label(self, font=('Arial', 14, 'bold'), textvariable=self.t_mood, height=2,
                             width=15, bg='#2d2d3e', fg='white', justify = CENTER)
        self.l_mood.place(x=largura*0.65, y=altura*0.6)


        ###### Listas de verbos
        self.verbosimp_flag = 0
        self.verbosimp = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                                activebackground='#404050', command=self.fverbosimp)
        self.verbosimp.place(x=largura * 0.9, y=altura * 0.1)

        self.verbos1_flag = 0
        self.verbos1 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos1)
        self.verbos1.place(x=largura*0.9, y=altura*0.15)

        self.verbos2_flag = 0
        self.verbos2 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos2)
        self.verbos2.place(x=largura * 0.9, y=altura * 0.2)

        self.verbos3_flag = 0
        self.verbos3 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos3)
        self.verbos3.place(x=largura * 0.9, y=altura * 0.25)

        self.verbos4_flag = 0
        self.verbos4 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos4)
        self.verbos4.place(x=largura * 0.9, y=altura * 0.3)

        self.verbos5_flag = 0
        self.verbos5 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos5)
        self.verbos5.place(x=largura * 0.9, y=altura * 0.35)

        self.verbos6_flag = 0
        self.verbos6 = Button(self, bd=3, height=1, width=2, bg='#C2171D',
                              activebackground='#404050', command=self.fverbos6)
        self.verbos6.place(x=largura * 0.9, y=altura * 0.4)

        ###### Dificuldade
        self.dif_flag = 0
        self.dif_txt = StringVar()
        self.dif_txt.set('Facile')
        self.dif = Button(self, font=('Arial', 12, 'bold'),bd=2, relief=RIDGE, textvariable=self.dif_txt, height=2,
                                  width=7, bg='#2d2d3e', fg='#22B14C', activebackground='#404050',
                                  activeforeground='white', command=self.fdif)
        self.dif.place(x=largura * 0.925, y=altura * 0.9)


        ###### Labels
        for i in [1,2,3,4,5,6]:
            texto_lista = Label(self, text=f'List {i}', font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e')
            texto_lista.place(x=largura*0.85, y=altura*(0.05*i + 0.1))
        (Label(self, text=f'Imp', font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e').
         place(x=largura*0.85, y=altura*0.1))

        dic = {1:'Verbe:', 2:'Pronom:', 3:'Temps:', 4:'Mode:'}
        for i in dic.keys():
            texto_sorteados = Label(self, text=dic[i], font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e')
            texto_sorteados.place(x=largura*(0.15*i + 0.05), y=altura*0.55)


        self.pontuacao = IntVar()
        self.pontuacao.set(0)
        pontos = Label(self, text='Score:', font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e')
        pontos.place(x=largura*0.1, y=altura*0.1)
        pontos_numero = Label(self, textvariable=self.pontuacao, font=('Arial', 14, 'bold'), justify = LEFT,
                              bd=0, fg='white', bg='#1e1e2e', width=3)
        pontos_numero.place(x=largura*0.15, y=altura*0.1)

        self.pontuacao_max = IntVar()
        self.pontuacao_max.set(0)
        pontos_max = Label(self, text='Meilleur score:', font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e')
        pontos_max.place(x=largura * 0.05, y=altura * 0.15)
        pontos_max_numero = Label(self, textvariable=self.pontuacao_max, font=('Arial', 14, 'bold'), justify=LEFT,
                              bd=0, fg='white', bg='#1e1e2e', width=3)
        pontos_max_numero.place(x=largura * 0.15, y=altura * 0.15)

        self.taux = StringVar()
        self.taux.set('0 %')
        self.acertos_t = 0
        self.erros_t = 0
        taux_text = Label(self, text='Taux de réussite:', font=('Arial', 14, 'bold'), bd=0, fg='white', bg='#1e1e2e')
        taux_text.place(x=largura * 0.035, y=altura * 0.2)
        taux_numero = Label(self, textvariable=self.taux, font=('Arial', 14, 'bold'), justify=LEFT,
                              bd=0, fg='white', bg='#1e1e2e', width=6)
        taux_numero.place(x=largura * 0.15, y=altura * 0.2)

        self.lista_tempos = {'Passé':PAST, 'Présent': PRESENT, 'Futur': FUTURE}

        self.lista_moods = {'Indicatif': INDICATIVE, 'Impératif': IMPERATIVE,
                            'Conditionnel': CONDITIONAL, 'Subjonctif': SUBJUNCTIVE}

        self.lista_pessoas = {'Je': 'SG,1', 'Tu': 'SG,2', 'Il': 'SG,3',
                              'Nous': 'PL,1', 'Vous': 'PL,2', 'Ils': 'PL,3'}


        self.lista_verbos1 = ["Avoir", "Être", "Aimer", "Placer", #'Se méfier',
                              "Manger", "Peser", "Céder", "Jeter"]

        self.lista_verbos2 = ['Modeler', 'Créer', 'Apprécier', 'Payer', 'Envoyer',
                              'Finir', 'Haïr', 'Aller', 'Tenir', 'Acquérir']

        self.lista_verbos3 = ['Sentir', 'Vêtir', 'Couvrir', 'Cueillir', 'Bouillir',
                              'Dormir', 'Courir', 'Mourir', 'Servir', 'Fuir']

        self.lista_verbos4 = ['Recevoir', 'Voir', 'Pourvoir', 'Savoir', 'Devoir',
                              'Pouvoir','Mouvoir', 'Pleuvoir', 'Falloir', 'Valoir']

        self.lista_verbos5 = ["Vouloir", "Rendre", "Prendre", "Battre", #"Se asseoir",
                              "Mettre", "Peindre", "Joindre", "Craindre", "Vaincre"]

        self.lista_verbos6 = ["Faire", "Plaire", "Connaître", "Naître", "Croître", "Croire",
                              "Boire", "Conclure", "Coudre", "Suivre", "Vivre", "Lire",
                              "Dire", "Rire", "Écrire", "Cuire"]

        self.lista_verbosimp = ['Être', 'Avoir', 'Pouvoir', 'Aller', 'Finir',
                                'Venir', 'Faire', 'Savoir', 'Voir', 'Dire']

        self.lista_verbos = []


        self.verbo_t = ''
        self.verbo_m = ''
        self.verbo_p = ''
        self.verbo_v = ''



    def f_sortear(self):
        self.entrada_tela.delete(0, END)
        self.resposta_texto.set('')
        self.entrada_tela.config(fg='white')
        self.verbo_t = choice(['Passé', 'Présent', 'Présent', 'Futur'])

        if self.verbo_t == 'Présent':
            self.verbo_m = choice(list(self.lista_moods.keys()))
            self.verbo_p = choice(list(self.lista_pessoas))
            if self.verbo_m == 'Impératif':
                self.verbo_p = choice(['Tu', 'Nous', 'Vous'])

        if self.verbo_t == 'Passé':
            self.verbo_m = 'Indicatif'
            self.verbo_t = 'Imparfait'
            self.verbo_p = choice(list(self.lista_pessoas))

        if self.verbo_t == 'Futur':
            self.verbo_m = 'Indicatif'
            self.verbo_p = choice(list(self.lista_pessoas))


        self.lista_verbos = []
        flag = 0
        if self.verbosimp_flag == 1:
            self.lista_verbos += self.lista_verbosimp
            flag = 1
        if self.verbos1_flag == 1:
            self.lista_verbos += self.lista_verbos1
            flag = 1
        if self.verbos2_flag == 1:
            self.lista_verbos += self.lista_verbos2
            flag = 1
        if self.verbos3_flag == 1:
            self.lista_verbos += self.lista_verbos3
            flag = 1
        if self.verbos4_flag == 1:
            self.lista_verbos += self.lista_verbos4
            flag = 1
        if self.verbos5_flag == 1:
            self.lista_verbos += self.lista_verbos5
            flag = 1
        if self.verbos6_flag == 1:
            self.lista_verbos += self.lista_verbos6
            flag = 1
        if flag == 0:
            self.lista_verbos += self.lista_verbosimp

        self.verbo_v = choice(self.lista_verbos)

        flag = 1
        if self.dif_flag == 0:
            self.verbo_m = 'Indicatif'
            if self.verbo_t == 'Imparfait':
                flag = 0
        elif self.dif_flag == 1:
            if self.verbo_m == 'Conditionnel' or 'Subjonctif':
                flag = 0
            if self.verbo_t == 'Futur':
                flag = 0

        self.counter = 0
        if flag == 1:
            self.counter = choice([0,0,0,1])
            if self.dif_flag == 0:
                if self.verbo_t == 'Futur':
                    self.verbo_t = 'Présent'
                    self.counter = choice([0,0,0,1,1])
            #self.counter = choice([1])
        if self.counter == 1:
            if self.verbo_m == 'Impératif':
                self.verbo_m = 'Indicatif'
                self.verbo_t = choice(list(self.lista_tempos.keys()))
                if self.verbo_t == 'Passé':
                    self.verbo_t = 'Imparfait'
            if self.verbo_m == 'Indicatif':
                if self.verbo_t == 'Présent':
                    self.verbo_t = 'Passé composé'
                elif self.verbo_t == 'Imparfait':
                    self.verbo_t = 'Plus que parfait'
                elif self.verbo_t == 'Futur':
                    self.verbo_t = 'Futur antérieur'
            if self.verbo_m == 'Conditionnel':
                self.verbo_t = 'Passé'
            if self.verbo_m == 'Subjonctif':
                self.verbo_t = 'Passé'

        if self.verbo_v.capitalize() in ('Falloir', 'Pleuvoir'):
            self.verbo_p = 'Il'
            if self.verbo_m == 'Impératif':
                self.verbo_m = choice(['Indicatif', 'Conditionnel', 'Subjonctif'])
        if self.verbo_v.capitalize() in 'Pouvoir':
            if self.verbo_m == 'Impératif':
                self.verbo_m = choice(['Indicatif', 'Conditionnel', 'Subjonctif'])

        self.t_tempo.set(self.verbo_t)
        self.t_mood.set(self.verbo_m)
        self.t_pessoa.set(self.verbo_p)
        self.t_verbo.set(self.verbo_v)

        self.entrada_texto.set('')
        self.entrada_tela.focus_set()
        self.flag_verificar = 0

    def f_verificar(self):
        if self.flag_verificar == 0:
            if self.verbo_m == 'Indicatif':
                if self.verbo_t == 'Imparfait':
                    self.verbo_t = 'Passé'
                if self.verbo_t == 'Futur antérieur':
                    self.verbo_t = 'Futur'
                if self.verbo_t == 'Passé composé':
                    self.verbo_t = 'Présent'
                if self.verbo_t == 'Plus que parfait':
                    self.verbo_t = 'Passé'
            if self.verbo_m == 'Conditionnel' or self.verbo_m == 'Subjonctif':
                self.verbo_t = 'Présent'


            verbo = self.verbo_v.lower()
            tempo = self.lista_tempos[self.verbo_t]
            modo = self.lista_moods[self.verbo_m]
            pessoa_sing_plr = self.lista_pessoas[self.verbo_p]

            sing_plr, pessoa = pessoa_sing_plr.split(',')
            pessoa = int(pessoa)

            if sing_plr == 'SG':
                sing_plr = SG
            elif sing_plr == 'PL':
                sing_plr = PL

            nome = f'{self.verbo_p} '

            if modo == SUBJUNCTIVE:
                nome = self.verbo_p
                if nome == 'Il' or nome == 'Ils':
                    nome = f'''Qu'{nome.lower()} '''
                else:
                    nome = f'Que {nome.lower()} '
            if modo == IMPERATIVE:
                nome = ''


            if verbo[:2] == 'Se':
                verbo = verbo[3:]
                if sing_plr == SG:
                    if pessoa == 1:
                        nome = f'{nome}me '
                    if pessoa == 2:
                        nome = f'{nome}te '
                    if pessoa == 3:
                        nome = f'{nome}se '
                if sing_plr == PL:
                    if pessoa == 1:
                        nome = f'{nome}nous '
                    if pessoa == 2:
                        nome = f'{nome}vous '
                    if pessoa == 3:
                        nome = f'{nome}se '

            if self.counter == 0:
                if verbo[0] in ['a','e','i','o','u']:
                    if nome == 'Je ':
                        nome = "J'"
                    elif nome == 'Que je ':
                        nome = "Que j'"
                texto = f'{nome}{conjugate(verbo, tempo, pessoa, sing_plr, mood = modo)}'

            else:
                part_p = f'{conjugate(verbo, PAST, None, None, INDICATIVE, PROGRESSIVE)}'
                if nome == 'Je ':
                    nome = "J'"
                if verbo.capitalize() in ("Aller", "Venir", "Arriver", "Partir", "Entrer", "Sortir",
                    "Monter", "Descendre", "Naître", "Mourir", "Rester", "Devenir"):
                    verbo = 'Être'
                    if sing_plr == PL:
                        part_p = f'{part_p}s'
                else:
                    if nome == 'Que je ':
                        nome = "Que j'"
                    verbo = 'Avoir'
                texto = f'{nome}{conjugate(verbo, tempo, pessoa, sing_plr, mood = modo)} {part_p}'
            self.conjugacao_correta = texto.capitalize()

            self.flag_verificar = 1
            self.comparar()

    def comparar(self):
        entrada_usuario = self.entrada_texto.get().strip()
        if entrada_usuario == self.conjugacao_correta:
            ponto = self.pontuacao.get()+1
            self.pontuacao.set(ponto)
            self.resposta_texto.set("Correct!")
            self.acertos_t += 1
            if self.pontuacao.get() > self.pontuacao_max.get():
                self.pontuacao_max.set(self.pontuacao.get())
        else:
            self.pontuacao.set(0)
            self.entrada_tela.config(fg='#ED1C24')
            self.erros_t += 1
            self.resposta_texto.set(f"{self.conjugacao_correta}")
        if self.erros_t == 0:
            self.taux.set('100 %')
        else:
            taxa = self.acertos_t/(self.erros_t+self.acertos_t)*100
            self.taux.set(f'{int(taxa)} %')


    def fverbosimp(self):
        if self.verbosimp_flag == 0:
            self.verbosimp_flag = 1
            self.verbosimp.config(bg='green')
        else:
            self.verbosimp_flag = 0
            self.verbosimp.config(bg='#C2171D')

    def fverbos1(self):
        if self.verbos1_flag == 0:
            self.verbos1_flag = 1
            self.verbos1.config(bg='green')
        else:
            self.verbos1_flag = 0
            self.verbos1.config(bg='#C2171D')

    def fverbos2(self):
        if self.verbos2_flag == 0:
            self.verbos2_flag = 1
            self.verbos2.config(bg='green')
        else:
            self.verbos2_flag = 0
            self.verbos2.config(bg='#C2171D')

    def fverbos3(self):
        if self.verbos3_flag == 0:
            self.verbos3_flag = 1
            self.verbos3.config(bg='green')
        else:
            self.verbos3_flag = 0
            self.verbos3.config(bg='#C2171D')

    def fverbos4(self):
        if self.verbos4_flag == 0:
            self.verbos4_flag = 1
            self.verbos4.config(bg='green')
        else:
            self.verbos4_flag = 0
            self.verbos4.config(bg='#C2171D')

    def fverbos5(self):
        if self.verbos5_flag == 0:
            self.verbos5_flag = 1
            self.verbos5.config(bg='green')
        else:
            self.verbos5_flag = 0
            self.verbos5.config(bg='#C2171D')

    def fverbos6(self):
        if self.verbos6_flag == 0:
            self.verbos6_flag = 1
            self.verbos6.config(bg='green')
        else:
            self.verbos6_flag = 0
            self.verbos6.config(bg='#C2171D')

    def fdif(self):
        if self.dif_flag == 0:
            self.dif_flag = 1
            self.dif_txt.set('Moyen')
            self.dif.config(fg='yellow')
        elif self.dif_flag == 1:
            self.dif_flag = 2
            self.dif_txt.set('Difficile')
            self.dif.config(fg='#ED1C24')
        elif self.dif_flag == 2:
            self.dif_flag = 0
            self.dif_txt.set('Facile')
            self.dif.config(fg='#22B14C')

def main():
    jogo = JogoPika()
    jogo.mainloop()

if __name__ == '__main__':
    main()

### By Hugo B. Errera ###
